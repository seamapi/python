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
  properties: Array<{
    name: string
    safeName: string
    type: string
    isDictParam: boolean
  }>
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
  const models = new Map<string, Property[]>()

  for (const resource of blueprint.resources) {
    models.set(resource.resourceType, resource.properties)
  }

  // The event and action attempt variants merge into a single dataclass with
  // the union of the variant properties, overriding the base resource schema.
  models.set(
    'action_attempt',
    mergeResourceProperties(blueprint.actionAttempts),
  )
  models.set('event', mergeResourceProperties(blueprint.events))

  if (blueprint.pagination != null) {
    models.set('pagination', blueprint.pagination.properties)
  }

  return [...models.entries()]
    .map(([name, properties]) => {
      const className = pascalCase(convertCustomResourceName(name))
      return {
        className,
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
