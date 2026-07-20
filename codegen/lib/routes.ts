// The Metalsmith plugin that generates the Python SDK route files.
// Ported from @seamapi/nextlove-sdk-generator lib/generate-python-sdk/generate-python-sdk.ts,
// restructured to mirror the javascript-http codegen plugin (lib/connect.ts).
//
// The blueprint from @seamapi/blueprint drives the iteration order and the
// route, endpoint, and namespace structure. The raw OpenAPI spec is still
// consulted wherever the previous nextlove generator derived output from data
// the blueprint normalizes differently; each of those spots is marked with a
// TODO so they can migrate to the blueprint once output is allowed to change.

import type { Blueprint } from '@seamapi/blueprint'
import * as types from '@seamapi/types/connect'
import { pascalCase } from 'change-case'
import type Metalsmith from 'metalsmith'

import type { ClassModel } from './class-model.js'
import { convertCustomResourceName } from './custom-resource-name-conversions.js'
import {
  endpointsReturningDeprecatedActionAttempt,
  ignoredEndpointPaths,
} from './endpoint-rules.js'
import { setModelsLayoutContext } from './layouts/models.js'
import { setRouteLayoutContext } from './layouts/route.js'
import { setRoutesIndexLayoutContext } from './layouts/routes-index.js'
import { mapPythonType } from './map-python-type.js'
import { deepFlattenOneOfAndAllOfSchema } from './openapi/deep-flatten-one-of-and-all-of-schema.js'
import { getFilteredRoutes } from './openapi/get-filtered-routes.js'
import { getParameterAndResponseSchema } from './openapi/get-parameter-and-response-schema.js'
import { mapParentToChildResources } from './openapi/map-parent-to-children-resource.js'
import type { OpenapiSchema, PropertySchema } from './openapi/types.js'

interface Metadata {
  blueprint: Blueprint
}

const rootPath = 'seam/routes'

const openapi = types.openapi as unknown as OpenapiSchema

export const routes = (
  files: Metalsmith.Files,
  metalsmith: Metalsmith,
): void => {
  const metadata = metalsmith.metadata() as Metadata
  const { blueprint } = metadata

  // TODO: Derive the parent to child resource map from blueprint.namespaces
  // once generated output is allowed to change.
  const rawRoutes = getFilteredRoutes(openapi)
  const parentToChildResourcesMap = mapParentToChildResources(rawRoutes)

  const classMap = new Map<string, ClassModel>()
  const namespaces: string[][] = []

  const processClass = (resourceName: string): void => {
    const childClassIdentifiers = (
      parentToChildResourcesMap[resourceName] ?? []
    ).map((childResource) => ({
      className: pascalCase(`${resourceName} ${childResource}`),
      namespace: childResource,
    }))
    const className = pascalCase(resourceName)

    classMap.set(className, {
      name: className,
      namespace: resourceName,
      methods: [],
      childClassIdentifiers,
    })
  }

  for (const route of blueprint.routes) {
    for (const endpoint of route.endpoints) {
      const post = openapi.paths[endpoint.path]?.post
      if (post == null) continue

      // TODO: Filter on endpoint.isUndocumented and route.isUndocumented from
      // the blueprint once generated output is allowed to change. The raw
      // OpenAPI extensions are used here to exclude exactly the same endpoint
      // set as the previous nextlove generator.
      if (post['x-undocumented'] != null) continue
      if ((post.summary ?? '').startsWith('/seam/')) continue
      if (post['x-fern-sdk-group-name'] == null) continue
      if (ignoredEndpointPaths.includes(endpoint.path)) continue

      const groupNames = [...post['x-fern-sdk-group-name']]
      const [baseResource] = groupNames
      const namespace = groupNames.join('_')
      const className = pascalCase(namespace)

      if (!classMap.has(className)) {
        namespaces.push(post['x-fern-sdk-group-name'])

        processClass(namespace)
      }

      /*
        Special case when we don't have routes for a base resource
        and thus a respective x-fern-sdk-group-name for ex. /noise_sensors
      */
      if (baseResource != null && !classMap.has(pascalCase(baseResource))) {
        namespaces.push([baseResource])

        processClass(baseResource)
      }

      const cls = classMap.get(className)

      if (cls == null) {
        // eslint-disable-next-line no-console
        console.warn(`No class for "${endpoint.path}", skipping`)
        continue
      }

      const { parameterSchema, responseObjType, responseArrType } =
        getParameterAndResponseSchema({ path: endpoint.path, post })

      if (parameterSchema == null) {
        // eslint-disable-next-line no-console
        console.warn(`No parameter schema for "${endpoint.path}", skipping`)
        continue
      }

      cls.methods.push({
        methodName: endpoint.name,
        path: endpoint.path,
        // TODO: Use endpoint.request.parameters from the blueprint once
        // generated output is allowed to change. The blueprint collapses
        // integer to number and flattens unions differently, so parameters
        // are derived from the raw OpenAPI schema for identical output.
        parameters: Object.entries(parameterSchema.properties)
          .filter(
            ([, paramVal]) =>
              'type' in paramVal ||
              ('oneOf' in paramVal && 'type' in (paramVal.oneOf[0] ?? {})),
          )
          .map(([paramName, paramVal]) => ({
            name: paramName,
            type: mapPythonType(
              'type' in paramVal
                ? (paramVal as PropertySchema)
                : deepFlattenOneOfAndAllOfSchema(paramVal as PropertySchema),
            ),
            position:
              endpoint.name === 'get' &&
              paramName === `${post['x-fern-sdk-return-value']}_id`
                ? 0
                : undefined,
            required: parameterSchema.required?.includes(paramName),
          })),
        // TODO: Use endpoint.response.responseKey from the blueprint once
        // generated output is allowed to change.
        returnPath: [post['x-fern-sdk-return-value']],
        returnResource: determineReturnResource({
          routePath: endpoint.path,
          responseObjType,
          responseArrType,
        }),
      })
    }
  }

  const topLevelNamespaces = namespaces
    .map((ns) => (ns.length === 1 ? ns[0] : null))
    .filter((ns): ns is string => ns != null)

  for (const cls of classMap.values()) {
    const k = `${rootPath}/${cls.namespace}.py`
    files[k] = {
      contents: Buffer.from('\n'),
      layout: 'route.hbs',
      ...setRouteLayoutContext(cls),
    }
  }

  files[`${rootPath}/models.py`] = {
    contents: Buffer.from('\n'),
    layout: 'models.hbs',
    ...setModelsLayoutContext(openapi, classMap, topLevelNamespaces),
  }

  files[`${rootPath}/__init__.py`] = {
    contents: Buffer.from('\n'),
    layout: 'routes-index.hbs',
    ...setRoutesIndexLayoutContext(topLevelNamespaces),
  }
}

const determineReturnResource = ({
  routePath,
  responseObjType,
  responseArrType,
}: {
  routePath: string
  responseObjType?: string | undefined
  responseArrType?: string | undefined
}): string => {
  if (endpointsReturningDeprecatedActionAttempt.includes(routePath)) {
    return 'None'
  }

  const responseType = responseObjType ?? responseArrType

  if (responseType != null) {
    const convertedResponseType = convertCustomResourceName(responseType)
    const formattedResponseType = pascalCase(convertedResponseType)

    return responseObjType != null
      ? formattedResponseType
      : `List[${formattedResponseType}]`
  }

  return 'None'
}
