// Builds the template context for the seam/resources modules.
// Each blueprint resource, along with events, action attempts, and pagination,
// becomes a dataclass in its own module, re-exported from seam/resources/__init__.py.

import type { Blueprint, Property } from '@seamapi/blueprint'
import { pascalCase, snakeCase } from 'change-case'

import { convertCustomResourceName } from '../custom-resource-name-conversions.js'
import { mapPropertyToPythonType } from '../python-type.js'

export interface ResourceLayoutContext {
  className: string
  moduleName: string
  description: string
  isDeprecated: boolean
  deprecationMessage: string
  nestedClasses: ResourceClassLayoutContext[]
  properties: ResourcePropertyLayoutContext[]
}

interface ResourceClassLayoutContext {
  className: string
  description: string
  properties: ResourcePropertyLayoutContext[]
}

interface ResourcePropertyLayoutContext {
  name: string
  description: string
  isDeprecated: boolean
  deprecationMessage: string
  type: string
  isDictParam: boolean
  isObject: boolean
  isObjectList: boolean
}

export interface ResourcesIndexLayoutContext {
  resources: Array<{ className: string; moduleName: string }>
}

// The action attempt and event variants each generate a single dataclass with
// the union of the variant properties. The first occurrence of a property
// name wins.
const mergeResourceProperties = (
  resources: Array<{ properties: Property[] }>,
): Property[] => {
  const merged = new Map<string, Property>()
  for (const { properties } of resources) {
    for (const property of properties) {
      if (!merged.has(property.name)) merged.set(property.name, property)
    }
  }
  return [...merged.values()]
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
      const nestedClasses = new Map<string, ResourceClassLayoutContext>()

      const buildProperties = (
        sourceProperties: Property[],
      ): ResourcePropertyLayoutContext[] =>
        sourceProperties.map((property) => {
          let nestedClassName: string | undefined
          let nestedProperties: Property[] | undefined
          if (property.format === 'object') {
            nestedClassName = `${className}${pascalCase(property.name)}`
            nestedProperties = property.properties
          } else if (
            property.format === 'list' &&
            property.itemFormat === 'object'
          ) {
            nestedClassName = `${className}${pascalCase(property.name)}`
            nestedProperties = property.itemProperties
          } else if (
            property.format === 'list' &&
            property.itemFormat === 'discriminated_object'
          ) {
            nestedClassName = `${className}${pascalCase(property.name)}`
            nestedProperties = mergeResourceProperties(property.variants)
          }

          if (
            nestedClassName != null &&
            nestedProperties != null &&
            !nestedClasses.has(nestedClassName)
          ) {
            // Reserve the name before recursing so colliding/recursive shapes
            // cannot register it twice. Reinsert after children for definition
            // order: annotations are evaluated when each class is created.
            nestedClasses.set(nestedClassName, {
              className: nestedClassName,
              description: property.description,
              properties: [],
            })
            const childProperties = buildProperties(nestedProperties)
            nestedClasses.delete(nestedClassName)
            nestedClasses.set(nestedClassName, {
              className: nestedClassName,
              description: property.description,
              properties: childProperties,
            })
          }

          const type = mapPropertyToPythonType(property, nestedClassName)
          return {
            name: property.name,
            description: property.description,
            isDeprecated: property.isDeprecated,
            deprecationMessage: property.deprecationMessage,
            type,
            isDictParam: type.startsWith('Dict'),
            isObject: nestedClassName != null && property.format === 'object',
            isObjectList: nestedClassName != null && property.format === 'list',
          }
        })

      const resourceProperties = buildProperties(properties)
      return {
        className,
        description,
        isDeprecated,
        deprecationMessage,
        // Derived from the class name rather than the resource type so the
        // module always matches the dataclass it exports (e.g. the "event"
        // resource becomes SeamEvent in seam_event.py).
        moduleName: snakeCase(className),
        nestedClasses: [...nestedClasses.values()],
        properties: resourceProperties,
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
