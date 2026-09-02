// Builds the template context for the seam/resources modules.
// Each blueprint resource, along with events, action attempts, and pagination,
// becomes a dataclass in its own module, re-exported from seam/resources/__init__.py.

import type {
  ActionAttemptStatus,
  Blueprint,
  EnumProperty,
  Property,
} from '@seamapi/blueprint'
import { pascalCase, snakeCase } from 'change-case'

import { convertCustomResourceName } from '../custom-resource-name-conversions.js'
import {
  mapPropertyToPythonType,
  mapRequiredPropertyToPythonType,
} from '../python-type.js'

export interface ResourceLayoutContext {
  className: string
  hasRawJson?: boolean
  moduleName: string
  isDeprecated: boolean
  deprecationMessage: string
  classes: ResourceClassLayoutContext[]
  union?: DiscriminatedUnionLayoutContext
  hasDiscriminatedLists: boolean
  exports: string[]
}

interface ResourceClassLayoutContext {
  className: string
  description: string
  isDeprecated?: boolean
  deprecationMessage?: string
  classIndent: string
  memberIndent: string
  docIndent: number
  nestedClasses: ResourceClassLayoutContext[]
  nestedUnions: DiscriminatedUnionLayoutContext[]
  properties: ResourcePropertyLayoutContext[]
}

interface DiscriminatedUnionLayoutContext {
  className: string
  discriminator: string
  secondaryDiscriminator?: string
  fromDictName: string
  variantsName: string
  variants: Array<{
    className: string
    values: string[]
    secondaryValue?: string
  }>
  aliases?: Array<{ className: string; variantClassNames: string[] }>
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
  isRequiredObject: boolean
  isObjectList: boolean
  isDiscriminatedObjectList: boolean
  discriminator: string
}

export interface ResourcesIndexLayoutContext {
  resources: Array<{ exports: string[]; moduleName: string }>
}

// Kept public because Ruby and PHP share these exact merge semantics. Union
// generation bypasses merging rather than changing it.
export const mergeResourceProperties = (
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
  'Literal',
  'Optional',
  'ResourceMapping',
  'Union',
  'dataclass',
])

type StatusAnnotatedProperty = Property & {
  renderAsNone?: boolean
  presentForStatus?: boolean
}

const isRenderedAsNone = (property: Property): boolean =>
  (property as StatusAnnotatedProperty).renderAsNone === true

const isPresentForStatus = (property: Property): boolean =>
  (property as StatusAnnotatedProperty).presentForStatus === true

const getNestedProperties = (property: Property): Property[] | undefined => {
  if (property.format === 'object') return property.properties
  if (property.format === 'list' && property.itemFormat === 'object') {
    return property.itemProperties
  }
  return undefined
}

const getDiscriminatorValues = (
  properties: Property[],
  discriminator: string,
  path: string,
): string[] => {
  const property = properties.find(({ name }) => name === discriminator)
  if (property?.format !== 'enum' || property.values.length === 0) {
    throw new Error(
      `${path} must have an enum property named ${discriminator} to generate a discriminated union.`,
    )
  }
  return property.values.map(({ name }) => name)
}

const singular = (name: string): string =>
  name.endsWith('s') ? name.slice(0, -1) : name

const pythonClassName = (value: string): string => {
  const name = pascalCase(value).replaceAll('_', '')
  return /^[A-Z]/.test(name) ? name : `Variant${name}`
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
  const nestedUnions: DiscriminatedUnionLayoutContext[] = []
  const takenClassNames = new Set<string>()

  const properties = classProperties.map((property) => {
    if (isRenderedAsNone(property)) {
      return {
        name: property.name,
        description: property.description,
        isDeprecated: property.isDeprecated,
        deprecationMessage: property.deprecationMessage,
        type: 'None',
        nestedClassName: '',
        isDictParam: false,
        isObject: false,
        isRequiredObject: false,
        isObjectList: false,
        isDiscriminatedObjectList: false,
        discriminator: '',
      }
    }

    const nestedProperties = getNestedProperties(property)
    const nestedPath = `${path}.${property.name}`
    const isDiscriminatedObjectList =
      property.format === 'list' &&
      property.itemFormat === 'discriminated_object'
    let nestedClassName: string | undefined

    if (isDiscriminatedObjectList) {
      nestedClassName = pascalCase(property.name)
      if (
        reservedClassNames.has(nestedClassName) ||
        takenClassNames.has(nestedClassName)
      ) {
        throw new Error(
          `${nestedPath} would generate a duplicate or reserved union named ${nestedClassName}.`,
        )
      }
      takenClassNames.add(nestedClassName)
      const suffix = pascalCase(singular(property.name))
      const variants = property.variants.map((variant) => {
        const values = getDiscriminatorValues(
          variant.properties,
          property.discriminator,
          nestedPath,
        )
        const variantClassName = `${pythonClassName(values[0] ?? '')}${suffix}`
        if (
          reservedClassNames.has(variantClassName) ||
          takenClassNames.has(variantClassName)
        ) {
          throw new Error(
            `${nestedPath} would generate a duplicate or reserved nested class named ${variantClassName}.`,
          )
        }
        takenClassNames.add(variantClassName)
        nestedClasses.push(
          buildClass(
            variantClassName,
            variant.description,
            variant.properties,
            `${nestedPath}.${values[0]}`,
            indentation + 4,
          ),
        )
        return { className: variantClassName, values }
      })
      nestedUnions.push({
        className: nestedClassName,
        discriminator: property.discriminator,
        fromDictName: '',
        variantsName: '',
        variants,
      })
    } else if (nestedProperties != null) {
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
    const isRequiredObject =
      isObject &&
      isPresentForStatus(property) &&
      !property.isOptional &&
      !property.isNullable
    const type = mapPropertyToPythonType(
      property,
      nestedClassName,
      isObject && !isRequiredObject,
    )
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
      isRequiredObject,
      isObjectList:
        !isDiscriminatedObjectList &&
        nestedClassName != null &&
        property.format === 'list',
      isDiscriminatedObjectList,
      discriminator: isDiscriminatedObjectList ? property.discriminator : '',
    }
  })

  return {
    className,
    description,
    classIndent: ' '.repeat(indentation),
    memberIndent: ' '.repeat(indentation + 4),
    docIndent: indentation + 4,
    nestedClasses,
    nestedUnions,
    properties,
  }
}

const hasDiscriminatedLists = (
  resourceClass: ResourceClassLayoutContext,
): boolean =>
  resourceClass.nestedUnions.length > 0 ||
  resourceClass.nestedClasses.some(hasDiscriminatedLists)

interface UnionVariant {
  value: string
  secondaryValue?: string
  description: string
  properties: Property[]
  isDeprecated: boolean
  deprecationMessage: string
}

const buildUnionAliases = (
  variants: Array<{ className: string; groupValue: string | undefined }>,
  suffix: string,
): Array<{ className: string; variantClassNames: string[] }> => {
  const groups = new Map<string, string[]>()
  for (const { className, groupValue } of variants) {
    if (groupValue == null) continue
    const group = groups.get(groupValue)
    if (group == null) {
      groups.set(groupValue, [className])
    } else {
      group.push(className)
    }
  }
  return [...groups.entries()].map(([value, variantClassNames]) => ({
    className: `${pythonClassName(value)}${suffix}`,
    variantClassNames,
  }))
}

const buildUnionResource = (
  className: string,
  discriminator: string,
  fromDictName: string,
  variants: UnionVariant[],
  isDeprecated: boolean,
  deprecationMessage: string,
  secondaryDiscriminator?: string,
): ResourceLayoutContext => {
  const suffix = className === 'SeamEvent' ? 'Event' : 'ActionAttempt'
  const classes = variants.map((variant) => {
    const secondaryName =
      variant.secondaryValue == null
        ? ''
        : pythonClassName(variant.secondaryValue)
    const secondaryPath =
      variant.secondaryValue == null ? '' : `.${variant.secondaryValue}`
    return {
      ...buildClass(
        `${pythonClassName(variant.value)}${secondaryName}${suffix}`,
        variant.description,
        variant.properties,
        `${snakeCase(className)}.${variant.value}${secondaryPath}`,
        rootIndentation,
      ),
      isDeprecated: variant.isDeprecated,
      deprecationMessage: variant.deprecationMessage,
    }
  })

  const aliases =
    secondaryDiscriminator == null
      ? []
      : [
          ...buildUnionAliases(
            classes.map(({ className: name }, index) => ({
              className: name,
              groupValue: variants[index]?.value,
            })),
            suffix,
          ),
          ...buildUnionAliases(
            classes.map(({ className: name }, index) => ({
              className: name,
              groupValue: variants[index]?.secondaryValue,
            })),
            suffix,
          ),
        ]
  const classNames = new Set(classes.map(({ className: name }) => name))
  for (const alias of aliases) {
    if (classNames.has(alias.className) || alias.className === className) {
      throw new Error(
        `The union alias ${alias.className} collides with a generated class name.`,
      )
    }
  }

  const union = {
    className,
    discriminator,
    ...(secondaryDiscriminator == null ? {} : { secondaryDiscriminator }),
    fromDictName,
    variantsName: `_${snakeCase(className).toUpperCase()}_VARIANTS`,
    variants: classes.map((variantClass, index) => {
      const secondaryValue = variants[index]?.secondaryValue
      return {
        className: variantClass.className,
        values: [variants[index]?.value ?? ''],
        ...(secondaryValue == null ? {} : { secondaryValue }),
      }
    }),
    aliases,
  }

  return {
    className,
    moduleName: snakeCase(className),
    isDeprecated,
    deprecationMessage,
    classes,
    union,
    hasDiscriminatedLists: classes.some(hasDiscriminatedLists),
    exports: [
      ...classes.map(({ className: name }) => name),
      ...aliases.map(({ className: name }) => name),
      className,
      fromDictName,
    ],
  }
}

const expandActionAttemptByStatus = (
  attempt: Blueprint['actionAttempts'][number],
): UnionVariant[] => {
  const statusProperty = attempt.properties.find(
    (property): property is EnumProperty =>
      property.name === 'status' && property.format === 'enum',
  )
  if (statusProperty == null || statusProperty.values.length === 0) {
    throw new Error(
      `The ${attempt.actionAttemptType} action attempt must have a status enum property to expand into per-status variants.`,
    )
  }

  return statusProperty.values.map(({ name: status }) => ({
    value: attempt.actionAttemptType,
    secondaryValue: status,
    description: attempt.description,
    isDeprecated: attempt.isDeprecated,
    deprecationMessage: attempt.deprecationMessage,
    properties: attempt.properties.map((property): Property => {
      if (property === statusProperty) {
        return {
          ...statusProperty,
          values: statusProperty.values.filter(
            (value) => value.name === status,
          ),
        }
      }
      const { actionAttemptStatuses } = property
      if (actionAttemptStatuses == null) return property
      if (actionAttemptStatuses.includes(status as ActionAttemptStatus)) {
        const presentProperty: StatusAnnotatedProperty = {
          ...property,
          presentForStatus: true,
        }
        return presentProperty
      }
      const noneProperty: StatusAnnotatedProperty = {
        ...property,
        isNullable: false,
        renderAsNone: true,
      }
      return noneProperty
    }),
  }))
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
  >(blueprint.resources.map((resource) => [resource.resourceType, resource]))

  const discriminatedResourceTypes = new Set(
    [...blueprint.events, ...blueprint.actionAttempts].map(
      ({ resourceType }) => resourceType,
    ),
  )
  for (const resourceType of discriminatedResourceTypes) {
    models.delete(resourceType)
  }

  if (blueprint.pagination != null) {
    models.set('pagination', {
      properties: blueprint.pagination.properties,
      description: blueprint.pagination.description,
      isDeprecated: false,
      deprecationMessage: '',
    })
  }

  const resources: ResourceLayoutContext[] = [...models.entries()].map(
    ([name, model]) => {
      const { properties, description, isDeprecated, deprecationMessage } =
        model
      const className = pascalCase(convertCustomResourceName(name))
      const rootClass = {
        ...buildClass(
          className,
          description,
          properties,
          name,
          rootIndentation,
        ),
        isDeprecated,
        deprecationMessage,
      }

      return {
        className,
        moduleName: snakeCase(className),
        isDeprecated,
        deprecationMessage,
        classes: [rootClass],
        hasDiscriminatedLists: hasDiscriminatedLists(rootClass),
        exports: [className],
      }
    },
  )

  const eventModel = blueprint.resources.find(
    ({ resourceType }) => resourceType === 'event',
  )
  resources.push({
    // raw_json exists for the webhook verify return, so the events carry it and
    // nothing else does.
    ...buildUnionResource(
      'SeamEvent',
      'event_type',
      'seam_event_from_dict',
      blueprint.events.map((event) => ({
        value: event.eventType,
        description: event.description,
        properties: event.properties,
        isDeprecated: event.isDeprecated,
        deprecationMessage: event.deprecationMessage,
      })),
      eventModel?.isDeprecated ?? false,
      eventModel?.deprecationMessage ?? '',
    ),
    hasRawJson: true,
  })

  const actionAttemptModel = blueprint.resources.find(
    ({ resourceType }) => resourceType === 'action_attempt',
  )
  resources.push(
    buildUnionResource(
      'ActionAttempt',
      'action_type',
      'action_attempt_from_dict',
      blueprint.actionAttempts.flatMap(expandActionAttemptByStatus),
      actionAttemptModel?.isDeprecated ?? false,
      actionAttemptModel?.deprecationMessage ?? '',
      'status',
    ),
  )

  return resources.sort((a, b) => (a.moduleName < b.moduleName ? -1 : 1))
}

export const setResourcesIndexLayoutContext = (
  resources: ResourceLayoutContext[],
): ResourcesIndexLayoutContext => ({
  resources: resources.map(({ exports, moduleName }) => ({
    exports,
    moduleName,
  })),
})
