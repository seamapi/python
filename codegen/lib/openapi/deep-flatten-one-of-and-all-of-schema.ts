// Ported from @seamapi/nextlove-sdk-generator lib/openapi/deep-flatten-one-of-and-all-of-schema.ts.
// TODO: Use parameter formats from @seamapi/blueprint once generated output is
// allowed to change.

import type {
  AllOfSchema,
  ArraySchema,
  ObjSchema,
  OneOfSchema,
  PrimitiveSchema,
  PropertySchema,
} from './types.js'

export function deepFlattenOneOfAndAllOfSchema(
  schema: PropertySchema,
): PropertySchema {
  if ('oneOf' in schema) {
    return flattenOneOf(schema)
  } else if ('allOf' in schema) {
    return flattenAllOf(schema)
  } else if (
    'type' in schema &&
    schema.type === 'object' &&
    schema.properties != null
  ) {
    return flattenObject(schema)
  } else if (
    'type' in schema &&
    schema.type === 'array' &&
    schema.items != null
  ) {
    return flattenArray(schema)
  } else {
    // For primitive types, return the schema as is
    return schema
  }
}

function flattenOneOf(oneOfSchema: OneOfSchema): ObjSchema | PrimitiveSchema {
  const flattenedSchema: ObjSchema = {
    type: 'object',
    properties: {},
    required: [],
  }

  for (const subSchema of oneOfSchema.oneOf) {
    const flattenedSubSchema = deepFlattenOneOfAndAllOfSchema(subSchema)

    // Check if the sub-schema is a primitive schema
    if ('type' in flattenedSubSchema && !('properties' in flattenedSubSchema)) {
      return { type: flattenedSubSchema.type } as PrimitiveSchema
    }

    if ('$ref' in flattenedSubSchema) {
      // eslint-disable-next-line no-console
      console.error('$ref not currently supported when flattening oneOf')
      continue
    }

    const subObj = flattenedSubSchema as ObjSchema

    // Merge properties
    Object.assign(flattenedSchema.properties, subObj.properties)

    // Update required array with common properties
    flattenedSchema.required =
      flattenedSchema.required.length === 0
        ? subObj.required
        : flattenedSchema.required.filter((prop) =>
            subObj.required.includes(prop),
          )
  }

  return flattenedSchema
}

function flattenAllOf(allOfSchema: AllOfSchema): ObjSchema | PrimitiveSchema {
  const flattenedSchema: ObjSchema = {
    type: 'object',
    properties: {},
    required: [],
  }

  for (const subSchema of allOfSchema.allOf) {
    const flattenedSubSchema = deepFlattenOneOfAndAllOfSchema(subSchema)

    // Check if the sub-schema is a primitive schema
    if ('type' in flattenedSubSchema && !('properties' in flattenedSubSchema)) {
      return { type: flattenedSubSchema.type } as PrimitiveSchema
    }

    if ('$ref' in flattenedSubSchema) {
      // eslint-disable-next-line no-console
      console.error('$ref not currently supported when flattening allOf')
      continue
    }

    const subObj = flattenedSubSchema as ObjSchema

    // Merge properties
    Object.assign(flattenedSchema.properties, subObj.properties)

    // Merge required array
    flattenedSchema.required = [
      ...new Set([...flattenedSchema.required, ...subObj.required]),
    ]
  }

  return flattenedSchema
}

function flattenObject(objSchema: ObjSchema): ObjSchema {
  const flattenedSchema: ObjSchema = {
    type: 'object',
    properties: {},
    required: objSchema.required ?? [],
  }

  for (const prop in objSchema.properties) {
    const propSchema = objSchema.properties[prop]
    if (propSchema == null) continue
    flattenedSchema.properties[prop] =
      deepFlattenOneOfAndAllOfSchema(propSchema)
  }

  return flattenedSchema
}

function flattenArray(arraySchema: ArraySchema): ArraySchema {
  return {
    type: 'array',
    items: deepFlattenOneOfAndAllOfSchema(arraySchema.items),
  }
}
