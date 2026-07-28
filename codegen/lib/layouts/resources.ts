// Builds the template context for the seam/resources modules.
// Each blueprint resource, along with events, action attempts, and pagination,
// becomes a dataclass in its own module, re-exported from seam/resources/__init__.py.

import type { Blueprint, Property, Resource } from '@seamapi/blueprint'
import { pascalCase, snakeCase } from 'change-case'

import { convertCustomResourceName } from '../custom-resource-name-conversions.js'
import { mapPropertyToPythonType } from '../python-type.js'

// Python hard keywords cannot be used as identifiers. When a property name
// collides with one (e.g. "from"), the dataclass field and keyword argument
// are suffixed with an underscore while the original name is preserved as the
// dict key.
const PYTHON_KEYWORDS = new Set([
  'False',
  'None',
  'True',
  'and',
  'as',
  'assert',
  'async',
  'await',
  'break',
  'class',
  'continue',
  'def',
  'del',
  'elif',
  'else',
  'except',
  'finally',
  'for',
  'from',
  'global',
  'if',
  'import',
  'in',
  'is',
  'lambda',
  'nonlocal',
  'not',
  'or',
  'pass',
  'raise',
  'return',
  'try',
  'while',
  'with',
  'yield',
])

const toSafeIdentifier = (name: string): string =>
  PYTHON_KEYWORDS.has(name) ? `${name}_` : name

export interface ResourceLayoutContext {
  className: string
  moduleName: string
  docstring: string
  properties: Array<{
    name: string
    safeName: string
    type: string
    isDictParam: boolean
  }>
}

const cleanDoc = (value: string): string =>
  value.trim().replaceAll('"""', '\\"\\"\\"')

const createResourceDocstring = (
  description: string,
  isDeprecated: boolean,
  deprecationMessage: string,
  properties: Property[],
): string => {
  const lines = [cleanDoc(description)]
  for (const property of properties) {
    const deprecated = property.isDeprecated
      ? `Deprecated${property.deprecationMessage === '' ? '.' : `: ${cleanDoc(property.deprecationMessage)}`}`
      : ''
    lines.push(
      '',
      `:ivar ${toSafeIdentifier(property.name)}: ${[
        deprecated,
        cleanDoc(property.description),
      ]
        .filter(Boolean)
        .join(' ')}`,
      `:vartype ${toSafeIdentifier(property.name)}: ${mapPropertyToPythonType(property)}`,
    )
  }
  if (isDeprecated) {
    lines.push(
      '',
      '.. deprecated::',
      `   ${cleanDoc(deprecationMessage) || 'This resource is deprecated.'}`,
    )
  }
  return lines
    .filter((line, index) => line !== '' || index !== 0)
    .join('\n')
    .replaceAll('\n', '\n    ')
}

export interface ResourcesIndexLayoutContext {
  resources: Array<{ className: string; moduleName: string }>
}

// The action attempt and event variants each generate a single dataclass with
// the union of the variant properties. The first occurrence of a property
// name wins.
const mergeResourceProperties = (resources: Resource[]): Property[] => {
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
      return {
        className,
        docstring: createResourceDocstring(
          description,
          isDeprecated,
          deprecationMessage,
          properties,
        ),
        // Derived from the class name rather than the resource type so the
        // module always matches the dataclass it exports (e.g. the "event"
        // resource becomes SeamEvent in seam_event.py).
        moduleName: snakeCase(className),
        properties: properties.map((property) => {
          const type = mapPropertyToPythonType(property)
          return {
            name: property.name,
            safeName: toSafeIdentifier(property.name),
            type,
            isDictParam:
              type.startsWith('Dict') || property.name === 'properties',
          }
        }),
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
