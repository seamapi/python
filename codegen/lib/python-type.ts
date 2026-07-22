// Maps blueprint parameter and property formats to Python types.

import type { Parameter, Property } from '@seamapi/blueprint'

type ScalarFormat = Exclude<(Parameter | Property)['format'], 'list'>

type ListItemFormat = Extract<
  Parameter | Property,
  { format: 'list' }
>['itemFormat']

export const mapParameterToPythonType = (parameter: Parameter): string => {
  if (parameter.format === 'list') {
    return `List[${mapListItemFormatToPythonType(parameter.itemFormat)}]`
  }

  if (parameter.format === 'number') {
    return parameter.isInt ? 'int' : 'float'
  }

  return mapScalarFormatToPythonType(parameter.format)
}

export const mapPropertyToPythonType = (property: Property): string => {
  if (property.format === 'list') {
    return `List[${mapListItemFormatToPythonType(property.itemFormat)}]`
  }

  if (property.format === 'number') {
    return property.isInt ? 'int' : 'float'
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
