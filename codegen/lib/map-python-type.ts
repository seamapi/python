// Ported from @seamapi/nextlove-sdk-generator lib/generate-python-sdk/map-python-type.ts.
// TODO: Derive types from @seamapi/blueprint parameter and property formats
// once generated output is allowed to change. Blueprint collapses the OpenAPI
// integer type into its number format, but the generated output distinguishes
// int from float, so the raw OpenAPI schema is used here instead.

import { deepFlattenOneOfAndAllOfSchema } from './openapi/deep-flatten-one-of-and-all-of-schema.js'
import type { PrimitiveSchema, PropertySchema } from './openapi/types.js'

// TODO literals?
export const mapPythonType = (propertySchema: PropertySchema): string => {
  if (typeof propertySchema !== 'object') {
    return 'Any'
  }

  if ('type' in propertySchema && propertySchema.type === 'string') {
    // TODO handle format="date-time"
    return 'str'
  }
  if ('type' in propertySchema && propertySchema.type === 'integer') {
    return 'int'
  }
  if ('type' in propertySchema && propertySchema.type === 'boolean') {
    return 'bool'
  }
  if ('type' in propertySchema && propertySchema.type === 'number') {
    return 'float'
  }
  if ('type' in propertySchema && propertySchema.type === 'array') {
    const arrayItemType: string =
      'type' in propertySchema.items
        ? mapPythonType({ type: propertySchema.items.type } as PrimitiveSchema)
        : mapPythonType(deepFlattenOneOfAndAllOfSchema(propertySchema.items))

    return `List[${arrayItemType}]`
  } // TODO, make more specific
  if ('type' in propertySchema && propertySchema.type === 'object') {
    return 'Dict[str, Any]' // TODO, make more specific
  }

  return 'Any'
}
