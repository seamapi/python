// TEMPORARY: Verbatim port of @seamapi/nextlove-sdk-generator
// lib/openapi/flatten-obj-schema.ts (with the lodash intersectionWith(isEqual)
// call replaced by a plain string-array intersection; required arrays only
// ever contain strings, so the semantics are identical). This is a frozen
// output-parity workaround: it exists only so the generated output stays
// byte-identical to the previous generator. Do not review, refactor, or
// improve it.
// TODO: Delete this file and use resource properties from @seamapi/blueprint
// once generated output is allowed to change.

import type {
  AllOfSchema,
  ArraySchema,
  ObjSchema,
  PrimitiveSchema,
  PropertySchema,
} from './types.js'

const intersection = (a: string[], b: string[]): string[] =>
  a.filter((x) => b.includes(x))

export const flattenObjSchema = (
  s: ObjSchema | { oneOf: ObjSchema[] } | { allOf: ObjSchema[] },
): ObjSchema => {
  if ('type' in s && s.type === 'object') return s

  if ('oneOf' in s) {
    if (s.oneOf[0] == null) {
      throw new Error('oneOf must have at least one element')
    }

    const superObj: ObjSchema = {
      type: 'object',
      properties: {},
      required: [...s.oneOf[0].required],
    }
    for (const obj of s.oneOf) {
      for (const [k, v] of Object.entries(obj.properties)) {
        superObj.properties[k] = v
      }
      superObj.required = intersection(superObj.required, obj.required)
    }
    return superObj
  }

  if ('allOf' in s) {
    return deepFlattenAllOfSchema(s) as ObjSchema
  }

  throw new Error(`Unknown schema type "${(s as { type: string }).type}"`)
}

export const deepFlattenAllOfSchema = (
  s: AllOfSchema,
): Exclude<PropertySchema, AllOfSchema> | undefined => {
  if (s.allOf.length === 1 && s.allOf[0] != null) {
    const recursive = s.allOf[0]

    if ('allOf' in recursive) {
      return deepFlattenAllOfSchema(recursive)
    }

    return recursive as Exclude<PropertySchema, AllOfSchema>
  }

  const properties: Record<string, PropertySchema[]> = {}
  const required = new Set<string>()
  const primitives: Array<PrimitiveSchema | ArraySchema> = []

  for (let subschema of s.allOf) {
    if ('allOf' in subschema) {
      const recursive = deepFlattenAllOfSchema(subschema as AllOfSchema)
      if (recursive == null) continue

      subschema = recursive
    }

    if ('oneOf' in subschema) {
      subschema = flattenObjSchema(subschema as { oneOf: ObjSchema[] })
    }

    if ('$ref' in subschema) {
      // eslint-disable-next-line no-console
      console.error('$ref not currently supported when flattening allOf')
      continue
    }

    if (subschema.type === 'object') {
      const objSchema = subschema as ObjSchema
      for (const [k, v] of Object.entries(objSchema.properties)) {
        if (properties[k] == null) properties[k] = []
        properties[k]?.push(v)

        if (objSchema.required?.includes(k) ?? false) required.add(k)
      }

      continue
    }

    primitives.push(subschema as PrimitiveSchema | ArraySchema)
  }

  if (Object.keys(properties).length > 0 && primitives.length > 0) {
    // eslint-disable-next-line no-console
    console.error(
      'Found invalid allOf schema with both properties and primitives',
      new Error(JSON.stringify(s, null, 2)),
    )
  }

  if (primitives.length > 0) {
    // TODO: check that all primitives are the same, then merge nullability/unions
    return primitives[0]
  }

  if (Object.keys(properties).length > 0) {
    return {
      type: 'object',
      required: [...required],
      properties: Object.fromEntries(
        Object.entries(properties)
          .map(([k, v]) => [k, deepFlattenAllOfSchema({ allOf: v })])
          .filter(([, v]) => v != null),
      ),
    }
  }

  return undefined
}
