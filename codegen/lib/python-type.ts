// Maps blueprint parameter and property formats to Python types.

import type { Parameter, Property } from '@seamapi/blueprint'

type ScalarFormat = Exclude<(Parameter | Property)['format'], 'list'>

type ListItemFormat = Extract<
  Parameter | Property,
  { format: 'list' }
>['itemFormat']

type RecordValueType = NonNullable<
  Extract<Parameter, { format: 'record' }>['valueTypes']
>[number]

export const mapParameterToPythonType = (parameter: Parameter): string => {
  if (parameter.format === 'list') {
    return `List[${mapListItemFormatToPythonType(parameter.itemFormat)}]`
  }

  if (parameter.format === 'number') {
    return parameter.isInt ? 'int' : 'float'
  }

  if (parameter.format === 'boolean') {
    return mapBooleanToPythonType(parameter.values)
  }

  if (parameter.format === 'record') {
    return mapRecordToPythonType(parameter.valueTypes)
  }

  return mapScalarFormatToPythonType(parameter.format)
}

// from_dict reads every property with dict.get, so a property the API may omit
// or send as null arrives as None. Declaring those fields Optional keeps the
// dataclass honest about what a caller can actually find on it.
export const mapPropertyToPythonType = (
  property: Property,
  nestedClassName?: string,
  isOptional = false,
): string => {
  const type = mapRequiredPropertyToPythonType(property, nestedClassName)
  return isOptional || property.isOptional || property.isNullable
    ? `Optional[${type}]`
    : type
}

// The type a property has before optionality is taken into account. Callers
// that match on the shape of the type, rather than render it, want this one.
export const mapRequiredPropertyToPythonType = (
  property: Property,
  nestedClassName?: string,
): string => {
  if (property.format === 'list') {
    return `List[${
      nestedClassName ?? mapListItemFormatToPythonType(property.itemFormat)
    }]`
  }

  if (property.format === 'number') {
    return property.isInt ? 'int' : 'float'
  }

  if (property.format === 'boolean') {
    return mapBooleanToPythonType(property.values)
  }

  // Batch resource properties are lists of the named resource on the wire,
  // though the blueprint types them as records.
  if (property.format === 'record' && 'resourceType' in property) {
    return 'List[Dict[str, Any]]'
  }

  if (property.format === 'record' && 'valueTypes' in property) {
    return mapRecordToPythonType(property.valueTypes)
  }

  if (property.format === 'object' && nestedClassName != null) {
    return nestedClassName
  }

  return mapScalarFormatToPythonType(property.format)
}

const mapBooleanToPythonType = (values?: boolean[]): string =>
  values == null || values.length === 0
    ? 'bool'
    : `Literal[${values.map((value) => (value ? 'True' : 'False')).join(', ')}]`

const mapRecordToPythonType = (valueTypes?: RecordValueType[]): string => {
  const types = valueTypes?.map(mapJsonSchemaTypeToPythonType) ?? []
  const valueType =
    types.length === 0
      ? 'Any'
      : types.length === 1
        ? (types[0] ?? 'Any')
        : `Union[${types.join(', ')}]`
  return `Dict[str, ${valueType}]`
}

const mapJsonSchemaTypeToPythonType = (type: RecordValueType): string => {
  switch (type) {
    case 'string':
      return 'str'
    case 'number':
      return 'float'
    case 'integer':
      return 'int'
    case 'boolean':
      return 'bool'
    case 'object':
      return 'Dict[str, Any]'
    case 'array':
      return 'List[Any]'
    default:
      throw new Error(`Unsupported JSON Schema type: ${type}`)
  }
}

const mapScalarFormatToPythonType = (format: ScalarFormat): string => {
  switch (format) {
    case 'string':
    case 'datetime':
    case 'id':
    case 'enum':
      return 'str'
    // List items have no isInt flag, so numbers in lists stay floats.
    case 'number':
      return 'float'
    case 'boolean':
      return 'bool'
    case 'record':
    case 'object':
      return 'Dict[str, Any]'
  }
}

const mapListItemFormatToPythonType = (itemFormat: ListItemFormat): string =>
  itemFormat === 'discriminated_object'
    ? 'Dict[str, Any]'
    : mapScalarFormatToPythonType(itemFormat)
