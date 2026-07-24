// The Metalsmith plugin that generates the Python SDK route files.
//
// The generator is driven entirely by the Blueprint that the @seamapi/smith
// blueprint plugin places in the Metalsmith metadata; no OpenAPI parsing
// happens here. Documented blueprint routes and namespaces map to route
// classes, endpoints to methods, and the blueprint resources, events, action
// attempts, and pagination to the dataclasses in the models module.

import type { Blueprint, Response } from '@seamapi/blueprint'
import { pascalCase } from 'change-case'
import type Metalsmith from 'metalsmith'

import type { ClassModel } from './class-model.js'
import { convertCustomResourceName } from './custom-resource-name-conversions.js'
import { setModelsLayoutContext } from './layouts/models.js'
import { setRouteLayoutContext } from './layouts/route.js'
import { setRoutesIndexLayoutContext } from './layouts/routes-index.js'
import { mapParameterToPythonType } from './python-type.js'

interface Metadata {
  blueprint: Blueprint
}

const rootPath = 'seam/routes'

const toNamespace = (path: string): string => path.slice(1).replaceAll('/', '_')

export const routes = (
  files: Metalsmith.Files,
  metalsmith: Metalsmith,
): void => {
  const metadata = metalsmith.metadata() as Metadata
  const { blueprint } = metadata

  // The blueprint is built with omitUndocumented, so undocumented routes,
  // namespaces, endpoints, and parameters are already stripped out.

  // Namespaces group routes without endpoints of their own (e.g. /acs) but
  // still produce a route class so their child classes are reachable.
  const classEntries = [...blueprint.namespaces, ...blueprint.routes]
    .map(({ path, parentPath }) => ({ path, parentPath }))
    .sort((a, b) => (a.path < b.path ? -1 : 1))

  const classMap = new Map<string, ClassModel>()

  for (const entry of classEntries) {
    const namespace = toNamespace(entry.path)
    const className = pascalCase(namespace)
    if (classMap.has(className)) continue

    classMap.set(className, {
      name: className,
      namespace,
      methods: [],
      childClassIdentifiers: classEntries
        .filter((child) => child.parentPath === entry.path)
        .map((child) => ({
          className: pascalCase(toNamespace(child.path)),
          // The property name on the parent class. The route layout derives
          // the child module name as `${parent.namespace}_${namespace}`, so
          // this must be the child path relative to the parent path.
          namespace: child.path
            .slice(entry.path.length + 1)
            .replaceAll('/', '_'),
        })),
    })
  }

  for (const route of blueprint.routes) {
    const cls = classMap.get(pascalCase(toNamespace(route.path)))
    if (cls == null) continue

    for (const endpoint of route.endpoints) {
      const { response } = endpoint
      const idParameterName =
        endpoint.name === 'get' && response.responseType !== 'void'
          ? `${response.responseKey}_id`
          : null

      cls.methods.push({
        methodName: endpoint.name,
        path: endpoint.path,
        parameters: endpoint.request.parameters.map((parameter) => ({
          name: parameter.name,
          type: mapParameterToPythonType(parameter),
          position: parameter.name === idParameterName ? 0 : undefined,
          required: parameter.isRequired,
        })),
        ...resolveResponse(response),
      })
    }
  }

  const topLevelNamespaces = classEntries
    .filter((entry) => entry.parentPath == null)
    .map((entry) => toNamespace(entry.path))

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
    ...setModelsLayoutContext(blueprint, classMap, topLevelNamespaces),
  }

  files[`${rootPath}/__init__.py`] = {
    contents: Buffer.from('\n'),
    layout: 'routes-index.hbs',
    ...setRoutesIndexLayoutContext(topLevelNamespaces),
  }
}

const resolveResponse = (
  response: Response,
): { returnPath: string[]; returnResource: string } => {
  if (response.responseType === 'void') {
    return { returnPath: [], returnResource: 'None' }
  }

  const returnPath = [response.responseKey]

  if (response.responseType === 'resource') {
    if (response.resourceType === 'action_attempt') {
      return { returnPath, returnResource: 'ActionAttempt' }
    }

    // Batch responses report resourceType as 'unknown'; the batch resource
    // itself is named by the response key.
    if (response.batchResourceTypes != null) {
      return { returnPath, returnResource: pascalCase(response.responseKey) }
    }
  }

  // Some endpoints respond with a resource the blueprint has no schema for
  // (e.g. unmanaged variants); there is no model class to deserialize into.
  if (response.resourceType === 'unknown') {
    return { returnPath: [], returnResource: 'None' }
  }

  const returnResource = pascalCase(
    convertCustomResourceName(response.resourceType),
  )

  return {
    returnPath,
    returnResource:
      response.responseType === 'resource_list'
        ? `List[${returnResource}]`
        : returnResource,
  }
}
