// Builds the template context for seam/routes/models.py.
// Mirrors the models.py assembly in the nextlove generate-python-sdk.ts plus
// ClassFile#serializeToAbstractClassWithoutImports.

import { pascalCase } from 'change-case'

import type { ClassModel } from 'lib/class-model.js'
import { convertCustomResourceName } from 'lib/custom-resource-name-conversions.js'
import { mapPythonType } from 'lib/map-python-type.js'
import { flattenObjSchema } from 'lib/openapi/flatten-obj-schema.js'
import type { ObjSchema, OpenapiSchema } from 'lib/openapi/types.js'

import { getMethodLayoutContext } from './route.js'

export interface ModelsLayoutContext {
  resources: Array<{
    className: string
    properties: Array<{ name: string; type: string; isDictParam: boolean }>
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

export const setModelsLayoutContext = (
  openapi: OpenapiSchema,
  classMap: Map<string, ClassModel>,
  topLevelNamespaces: string[],
): ModelsLayoutContext => {
  // TODO: Use blueprint.resources, blueprint.events, and
  // blueprint.actionAttempts once generated output is allowed to change.
  // Blueprint currently omits some schemas (e.g. pagination and
  // phone_registration), reorders others, and collapses integer to number,
  // so the raw OpenAPI schemas are used to keep the output identical.
  const resources = Object.entries(openapi.components.schemas)
    .map(
      ([schemaName, schema]) =>
        [schemaName, flattenObjSchema(schema as ObjSchema)] as [
          string,
          ObjSchema,
        ],
    )
    .map(([schemaName, schema]) => ({
      className: pascalCase(convertCustomResourceName(schemaName)),
      properties: Object.entries(schema.properties).map(
        ([name, propertySchema]) => {
          const type = mapPythonType(propertySchema)
          return {
            name,
            type,
            isDictParam: type.startsWith('Dict') || name === 'properties',
          }
        },
      ),
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
