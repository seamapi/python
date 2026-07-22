// Maps blueprint parameter and property formats to Python types.

import type { Parameter, Property } from '@seamapi/blueprint'

type ScalarFormat = Exclude<(Parameter | Property)['format'], 'list'>

type ListItemFormat = Extract<
  Parameter | Property,
  { format: 'list' }
>['itemFormat']

export const mapParameterToPythonType = (parameter: Parameter): string =>
  parameter.format === 'list'
    ? `List[${mapListItemFormatToPythonType(parameter.itemFormat)}]`
    : mapScalarFormatToPythonType(parameter.format)

export const mapPropertyToPythonType = (property: Property): string => {
  if (property.format === 'list') {
    return `List[${mapListItemFormatToPythonType(property.itemFormat)}]`
  }

  // Batch resource properties are lists of the named resource on the wire,
  // though the blueprint types them as records.
  if (property.format === 'record' && 'resourceType' in property) {
    return 'List[Dict[str, Any]]'
  }

  return mapScalarFormatToPythonType(property.format)
}

const mapScalarFormatToPythonType = (format: ScalarFormat): string => {
  switch (format) {
    case 'string':
    case 'datetime':
    case 'id':
    case 'enum':
      return 'str'
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
