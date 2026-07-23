// Maps blueprint parameter and property formats to Python types.

import type { Parameter, Property } from '@seamapi/blueprint'

type ScalarFormat = Exclude<(Parameter | Property)['format'], 'list' | 'number'>

type ListItem = Extract<Parameter | Property, { format: 'list' }>

export const mapParameterToPythonType = (parameter: Parameter): string => {
  if (parameter.format === 'list') {
    return `List[${mapListItemToPythonType(parameter)}]`
  }

  if (parameter.format === 'number') {
    return parameter.isInt ? 'int' : 'float'
  }

  return mapScalarFormatToPythonType(parameter.format)
}

export const mapPropertyToPythonType = (property: Property): string => {
  if (property.format === 'list') {
    return `List[${mapListItemToPythonType(property)}]`
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

const mapListItemToPythonType = (list: ListItem): string => {
  if (list.itemFormat === 'number') {
    return list.isItemInt ? 'int' : 'float'
  }

  if (list.itemFormat === 'discriminated_object') {
    return 'Dict[str, Any]'
  }

  return mapScalarFormatToPythonType(list.itemFormat)
}

const mapScalarFormatToPythonType = (format: ScalarFormat): string => {
  switch (format) {
    case 'string':
    case 'datetime':
    case 'id':
    case 'enum':
      return 'str'
    case 'boolean':
      return 'bool'
    case 'record':
    case 'object':
      return 'Dict[str, Any]'
  }
}
