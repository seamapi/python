// Builds the template context for seam/routes/models.py.
// Dataclasses come from the blueprint resources, events, action attempts, and
// pagination; the abstract route classes mirror the generated route classes.

import type { Blueprint, Property, Resource } from '@seamapi/blueprint'
import { pascalCase } from 'change-case'

import type { ClassModel } from '../class-model.js'
import { convertCustomResourceName } from '../custom-resource-name-conversions.js'
import { mapPropertyToPythonType } from '../python-type.js'
import { getMethodLayoutContext } from './route.js'

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

export interface ModelsLayoutContext {
  resources: Array<{
    className: string
    properties: Array<{
      name: string
      safeName: string
      type: string
      isDictParam: boolean
    }>
  }>
  abstractClasses: Array<{
    className: string
    showPass: boolean
    childProperties: Array<{ namespace: string; abstractClassName: string }>
    methods: Array<{
      name: string
      hasParams: boolean
      signatureParams: string
      returnType: string
    }>
  }>
  routesNamespaces: Array<{ namespace: string; abstractClassName: string }>
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

export const setModelsLayoutContext = (
  blueprint: Blueprint,
  classMap: Map<string, ClassModel>,
  topLevelNamespaces: string[],
): ModelsLayoutContext => {
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

  const resources = [...models.entries()]
    .sort(([a], [b]) => (a < b ? -1 : 1))
    .map(([name, properties]) => ({
      className: pascalCase(convertCustomResourceName(name)),
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
    }))

  const abstractClasses = [...classMap.values()]
    // Define classes without children first for parent-child referencing.
    // Array#sort is stable, so ties keep class-map insertion order.
    .sort(
      (a, b) => a.childClassIdentifiers.length - b.childClassIdentifiers.length,
    )
    .map((cls) => ({
      className: `Abstract${cls.name}`,
      showPass:
        cls.methods.length === 0 && cls.childClassIdentifiers.length === 0,
      childProperties: cls.childClassIdentifiers.map((i) => ({
        namespace: i.namespace,
        abstractClassName: `Abstract${i.className}`,
      })),
      methods: cls.methods.map((method) => {
        const { name, hasParams, signatureParams, returnType } =
          getMethodLayoutContext(method)
        return { name, hasParams, signatureParams, returnType }
      }),
    }))

  return {
    resources,
    abstractClasses,
    routesNamespaces: topLevelNamespaces.map((ns) => ({
      namespace: ns,
      abstractClassName: `Abstract${pascalCase(ns)}`,
    })),
  }
}
