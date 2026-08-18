// Builds the template context for the seam/resources modules.
// Each blueprint resource, along with events, action attempts, and pagination,
// becomes a dataclass in its own module, re-exported from seam/resources/__init__.py.

import type { Blueprint, Property } from '@seamapi/blueprint'
import { pascalCase, snakeCase } from 'change-case'

import { convertCustomResourceName } from '../custom-resource-name-conversions.js'
import {
  mapPropertyToPythonType,
  mapRequiredPropertyToPythonType,
} from '../python-type.js'

export interface ResourceLayoutContext extends ResourceClassLayoutContext {
  moduleName: string
  isDeprecated: boolean
  deprecationMessage: string
}

interface ResourceClassLayoutContext {
  className: string
  description: string
  classIndent: string
  memberIndent: string
  docIndent: number
  nestedClasses: ResourceClassLayoutContext[]
  properties: ResourcePropertyLayoutContext[]
}

interface ResourcePropertyLayoutContext {
  name: string
  description: string
  isDeprecated: boolean
  deprecationMessage: string
  type: string
  nestedClassName: string
  isDictParam: boolean
  isObject: boolean
  isObjectList: boolean
}

export interface ResourcesIndexLayoutContext {
  resources: Array<{ className: string; moduleName: string }>
}

// The action attempt and event variants each generate a single dataclass with
// the union of the variant properties.
const mergeResourceProperties = (
  resources: Array<{ properties: Property[] }>,
): Property[] =>
  mergePropertyLists(resources.map(({ properties }) => properties))

const formatKey = (property: Property): string =>
  property.format === 'list' ? `list<${property.itemFormat}>` : property.format

const isScalar = (property: Property): boolean =>
  property.format !== 'list' && property.format !== 'object'

interface MergedDocs {
  description: string
  isDeprecated: boolean
  deprecationMessage: string
}

// Each variant documents a property for its own case, which is accurate there
// but not for the single dataclass the variants merge into. Some are merely
// narrow ("Previous code configuration" on a shape that also covers names);
// others contradict each other outright ("the error is not a device error"
// against "the error is a device error"). No description beats a wrong one, so
// keep one only when every variant that documents the property agrees.
const mergeDocs = (occurrences: Property[]): MergedDocs => {
  const descriptions = [
    ...new Set(
      occurrences
        .map((occurrence) => occurrence.description.trim())
        .filter((description) => description !== ''),
    ),
  ]
  const deprecated = occurrences.find(({ isDeprecated }) => isDeprecated)

  return {
    description: descriptions.length === 1 ? (descriptions[0] ?? '') : '',
    // Deprecating in any variant deprecates the merged property, so a warning
    // is never dropped just because another variant omits it.
    isDeprecated: deprecated != null,
    deprecationMessage: deprecated?.deprecationMessage ?? '',
  }
}

// The variants of a discriminated union collapse into a single dataclass, so a
// property carried by more than one variant has to end up with every field any
// variant gives it. Keeping only the first occurrence silently drops the rest,
// which loses data once from_dict reads the merged shape field by field.
const mergeOccurrences = (occurrences: Property[], path: string): Property => {
  const [first, ...rest] = occurrences
  if (first == null) throw new Error(`Nothing to merge at ${path}.`)
  if (rest.length === 0) return first

  const docs = mergeDocs(occurrences)

  const formats = new Set(occurrences.map(formatKey))
  if (formats.size > 1) {
    // Scalars all map to the same Python type, so any of them stands in.
    if (occurrences.every(isScalar)) return { ...first, ...docs }
    throw new Error(
      `Cannot merge ${path}: variants disagree on its shape (${[...formats].join(', ')}).`,
    )
  }

  if (first.format === 'boolean') {
    const booleans = occurrences as Array<
      Extract<Property, { format: 'boolean' }>
    >
    const values = booleans.some(({ values }) => values == null)
      ? undefined
      : [...new Set(booleans.flatMap(({ values }) => values ?? []))]
    const merged = { ...first, ...docs }
    if (values == null) delete merged.values
    else merged.values = values
    return merged
  }

  if (first.format === 'record' && 'valueTypes' in first) {
    const valueTypes = occurrences.some(
      (occurrence) =>
        !('valueTypes' in occurrence) || occurrence.valueTypes == null,
    )
      ? undefined
      : [
          ...new Set(
            occurrences.flatMap((occurrence) =>
              'valueTypes' in occurrence ? (occurrence.valueTypes ?? []) : [],
            ),
          ),
        ]
    const merged = { ...first, ...docs }
    if (valueTypes == null) delete merged.valueTypes
    else merged.valueTypes = valueTypes
    return merged
  }

  if (first.format === 'object') {
    return {
      ...first,
      ...docs,
      properties: mergePropertyLists(
        occurrences.map(
          (occurrence) => (occurrence as typeof first).properties,
        ),
        path,
      ),
    }
  }

  if (first.format === 'list' && first.itemFormat === 'object') {
    return {
      ...first,
      ...docs,
      itemProperties: mergePropertyLists(
        occurrences.map(
          (occurrence) => (occurrence as typeof first).itemProperties,
        ),
        `${path}[]`,
      ),
    }
  }

  if (first.format === 'list' && first.itemFormat === 'discriminated_object') {
    // Keep every variant. Whoever consumes this list merges them in turn.
    return {
      ...first,
      ...docs,
      variants: occurrences.flatMap(
        (occurrence) => (occurrence as typeof first).variants,
      ),
    }
  }

  return { ...first, ...docs }
}

const withOptionality = (property: Property, isOptional: boolean): Property =>
  isOptional ? { ...property, isOptional: true } : property

const mergePropertyLists = (
  propertyLists: Property[][],
  path = '',
): Property[] => {
  const occurrences = new Map<string, Property[]>()
  for (const properties of propertyLists) {
    for (const property of properties) {
      const group = occurrences.get(property.name)
      if (group == null) {
        occurrences.set(property.name, [property])
      } else {
        group.push(property)
      }
    }
  }

  return [...occurrences.entries()].map(([name, group]) =>
    // A property only some variants carry is absent whenever the merged
    // dataclass holds one of the variants that omits it, so it is optional on
    // the merged shape no matter how each variant declares it.
    withOptionality(
      mergeOccurrences(group, path === '' ? name : `${path}.${name}`),
      group.length < propertyLists.length,
    ),
  )
}

// Resource dataclasses are declared at module level.
const rootIndentation = 0

// Nested classes are named after their property, so an unusually deep shape is
// far more likely to be an accidental cycle than a real schema.
const maxNestingDepth = 16

// Names a nested class must not claim, since it would shadow something the
// generated module resolves from an enclosing scope.
const reservedClassNames = new Set([
  'Any',
  'DeepAttrDict',
  'Dict',
  'List',
  'Optional',
  'ResourceMapping',
  'Union',
  'dataclass',
])

const getNestedProperties = (property: Property): Property[] | undefined => {
  if (property.format === 'object') return property.properties
  if (property.format === 'list' && property.itemFormat === 'object') {
    return property.itemProperties
  }
  if (
    property.format === 'list' &&
    property.itemFormat === 'discriminated_object'
  ) {
    return mergeResourceProperties(property.variants)
  }
  return undefined
}

const buildClass = (
  className: string,
  description: string,
  classProperties: Property[],
  path: string,
  indentation: number,
): ResourceClassLayoutContext => {
  if (indentation > rootIndentation + 4 * maxNestingDepth) {
    throw new Error(
      `Nested resource classes exceeded a depth of ${maxNestingDepth} at ${path}. This usually means the schema is cyclic.`,
    )
  }

  const nestedClasses: ResourceClassLayoutContext[] = []
  const takenClassNames = new Set<string>()

  const properties = classProperties.map((property) => {
    const nestedProperties = getNestedProperties(property)
    const nestedPath = `${path}.${property.name}`
    let nestedClassName: string | undefined

    if (nestedProperties != null) {
      // Each class scopes its own nested classes, so the property name alone
      // names them unambiguously.
      nestedClassName = pascalCase(property.name)

      if (reservedClassNames.has(nestedClassName)) {
        throw new Error(
          `The ${nestedPath} property would generate a nested class named ${nestedClassName}, which shadows a name the generated module depends on.`,
        )
      }

      if (takenClassNames.has(nestedClassName)) {
        throw new Error(
          `The ${nestedPath} property would generate a second nested class named ${nestedClassName} inside ${className}.`,
        )
      }
      takenClassNames.add(nestedClassName)

      nestedClasses.push(
        buildClass(
          nestedClassName,
          property.description,
          nestedProperties,
          nestedPath,
          indentation + 4,
        ),
      )
    }

    const isObject = nestedClassName != null && property.format === 'object'
    // A nested object is read as None whenever the payload omits it, and the
    // schema is not a reliable guide to when that happens: an action attempt
    // documents both error and result as required, yet a pending one carries
    // neither. Constructing them unconditionally would fail on those payloads,
    // so from_dict keeps its None fallback and the field stays Optional.
    const type = mapPropertyToPythonType(property, nestedClassName, isObject)
    const requiredType = mapRequiredPropertyToPythonType(
      property,
      nestedClassName,
    )
    return {
      name: property.name,
      description: property.description,
      isDeprecated: property.isDeprecated,
      deprecationMessage: property.deprecationMessage,
      type,
      // Nested classes are attributes of the class that owns them, so
      // from_dict reaches them through cls rather than a qualified path.
      nestedClassName: nestedClassName ?? '',
      isDictParam: requiredType.startsWith('Dict'),
      isObject,
      isObjectList: nestedClassName != null && property.format === 'list',
    }
  })

  return {
    className,
    description,
    classIndent: ' '.repeat(indentation),
    memberIndent: ' '.repeat(indentation + 4),
    docIndent: indentation + 4,
    nestedClasses,
    properties,
  }
}

export const getResourceLayoutContexts = (
  blueprint: Blueprint,
): ResourceLayoutContext[] => {
  const models = new Map<
    string,
    {
      properties: Property[]
      description: string
      isDeprecated: boolean
      deprecationMessage: string
    }
  >()

  for (const resource of blueprint.resources) {
    models.set(resource.resourceType, resource)
  }

  // The event and action attempt variants merge into a single dataclass with
  // the union of the variant properties, overriding the base resource schema.
  const actionAttemptModel = models.get('action_attempt')
  models.set('action_attempt', {
    properties: mergeResourceProperties(blueprint.actionAttempts),
    description:
      actionAttemptModel?.description ??
      'An attempt to perform an action in the Seam API.',
    isDeprecated: actionAttemptModel?.isDeprecated ?? false,
    deprecationMessage: actionAttemptModel?.deprecationMessage ?? '',
  })
  const eventModel = models.get('event')
  models.set('event', {
    properties: mergeResourceProperties(blueprint.events),
    description: eventModel?.description ?? 'An event emitted by the Seam API.',
    isDeprecated: eventModel?.isDeprecated ?? false,
    deprecationMessage: eventModel?.deprecationMessage ?? '',
  })

  if (blueprint.pagination != null) {
    models.set('pagination', {
      properties: blueprint.pagination.properties,
      description: blueprint.pagination.description,
      isDeprecated: false,
      deprecationMessage: '',
    })
  }

  return [...models.entries()]
    .map(([name, model]) => {
      const { properties, description, isDeprecated, deprecationMessage } =
        model
      const className = pascalCase(convertCustomResourceName(name))
      const rootClass = buildClass(
        className,
        description,
        properties,
        name,
        rootIndentation,
      )

      return {
        ...rootClass,
        isDeprecated,
        deprecationMessage,
        // Derived from the class name rather than the resource type so the
        // module always matches the dataclass it exports (e.g. the "event"
        // resource becomes SeamEvent in seam_event.py).
        moduleName: snakeCase(className),
      }
    })
    .sort((a, b) => (a.moduleName < b.moduleName ? -1 : 1))
}

export const setResourcesIndexLayoutContext = (
  resources: ResourceLayoutContext[],
): ResourcesIndexLayoutContext => ({
  resources: resources.map(({ className, moduleName }) => ({
    className,
    moduleName,
  })),
})
