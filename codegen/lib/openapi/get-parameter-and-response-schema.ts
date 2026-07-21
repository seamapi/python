// TEMPORARY: Verbatim port of @seamapi/nextlove-sdk-generator
// lib/openapi/get-parameter-and-response-schema.ts. This OpenAPI parsing is a
// frozen output-parity workaround: it exists only so the generated output
// stays byte-identical to the previous generator. Do not review, refactor, or
// improve it.
// TODO: Delete this file and use endpoint.request.parameters and
// endpoint.response from @seamapi/blueprint once generated output is allowed
// to change.

import { deepFlattenOneOfAndAllOfSchema } from './deep-flatten-one-of-and-all-of-schema.js'
import { flattenObjSchema } from './flatten-obj-schema.js'
import type { ObjSchema, Route } from './types.js'

export const getParameterAndResponseSchema = (
  route: Route,
): {
  parameterSchema?: ObjSchema
  responseObjType?: string | undefined
  responseArrType?: string | undefined
} => {
  const responseSchema =
    route.post.responses['200']?.content?.['application/json']?.schema

  if (responseSchema == null) {
    return {}
  }

  if (route.post.requestBody == null) {
    route.post.requestBody = {
      content: {
        'application/json': { schema: { type: 'object', properties: {} } },
      },
    }
  }

  if (route.post.requestBody.content?.['application/json'] == null) {
    return {}
  }

  const parameterSchema = processParameterSchema(
    route.post.requestBody.content['application/json'].schema,
  )

  const resReturnSchema =
    responseSchema.properties?.[route.post['x-response-key'] ?? '']

  const responseObjRef = resReturnSchema?.$ref
  const responseArrRef = resReturnSchema?.items?.$ref

  if (route.post['x-response-key'] === 'batch') {
    return {
      responseObjType: route.post['x-response-key'],
      responseArrType: undefined,
      parameterSchema,
    }
  } else if (responseObjRef == null && responseArrRef == null) {
    return {
      responseObjType: undefined,
      responseArrType: undefined,
      parameterSchema,
    }
  } else {
    return {
      responseObjType: responseObjRef?.split('/')?.pop(),
      responseArrType: responseArrRef?.split('/')?.pop(),
      parameterSchema,
    }
  }
}

function processParameterSchema(
  schema: ObjSchema | { oneOf: ObjSchema[] } | { allOf: ObjSchema[] },
): ObjSchema {
  const parameterSchema = flattenObjSchema(schema)

  for (const [paramName, paramValue] of Object.entries(
    parameterSchema.properties,
  )) {
    if ('oneOf' in paramValue || 'allOf' in paramValue) {
      parameterSchema.properties[paramName] =
        deepFlattenOneOfAndAllOfSchema(paramValue)
    }
  }

  return stripUndocumentedProperties(parameterSchema)
}

function stripUndocumentedProperties(schema: ObjSchema): ObjSchema {
  const properties = Object.fromEntries(
    Object.entries(schema.properties).flatMap(([name, propertySchema]) => {
      const filteredProperty = stripUndocumentedPropertySchema(propertySchema)

      return filteredProperty != null ? [[name, filteredProperty]] : []
    }),
  )

  return {
    ...schema,
    properties,
    required: (schema.required ?? []).filter((name) => name in properties),
  }
}

function stripUndocumentedPropertySchema(propertySchema: any): any {
  if (propertySchema?.['x-undocumented'] != null) {
    return undefined
  }

  if (propertySchema?.type === 'object' && propertySchema.properties != null) {
    const properties = Object.fromEntries(
      Object.entries(propertySchema.properties).flatMap(
        ([name, nestedSchema]) => {
          const filteredProperty = stripUndocumentedPropertySchema(nestedSchema)

          return filteredProperty != null ? [[name, filteredProperty]] : []
        },
      ),
    )

    return {
      ...propertySchema,
      properties,
      required: (propertySchema.required ?? []).filter(
        (name: string) => name in properties,
      ),
    }
  }

  if (propertySchema?.type === 'array' && propertySchema.items != null) {
    const items = stripUndocumentedPropertySchema(propertySchema.items)

    return {
      ...propertySchema,
      items: items ?? propertySchema.items,
    }
  }

  return propertySchema
}
