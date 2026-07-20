// Ported from @seamapi/nextlove-sdk-generator lib/openapi/map-parent-to-children-resource.ts.
// Only the first two segments of x-fern-sdk-group-name are considered, so
// deeply nested namespaces (e.g. acs.encoders.simulate) are generated as
// standalone classes but never wired to a parent property. Do not "fix" this:
// the generated output must stay identical.
// TODO: Use blueprint.namespaces parent/child relationships once generated
// output is allowed to change.

import { ignoredEndpointPaths } from '../endpoint-rules.js'
import type { Route } from './types.js'

export const mapParentToChildResources = (
  routes: Route[],
): Record<string, string[]> =>
  routes.reduce((acc: Record<string, string[]>, route) => {
    if (route.post?.['x-fern-sdk-group-name'] == null) return acc
    if (ignoredEndpointPaths.includes(route.path)) return acc

    const [parentResourceName, childResourceName] =
      route.post['x-fern-sdk-group-name']

    if (parentResourceName == null) return acc

    if (acc[parentResourceName] == null) {
      acc[parentResourceName] = []
    }

    if (
      childResourceName != null &&
      !(acc[parentResourceName]?.includes(childResourceName) ?? false)
    ) {
      acc[parentResourceName]?.push(childResourceName)
    }

    return acc
  }, {})
