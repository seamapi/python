// TEMPORARY: Verbatim port of @seamapi/nextlove-sdk-generator
// lib/openapi/map-parent-to-children-resource.ts. This is a frozen
// output-parity workaround: it exists only so the generated output stays
// byte-identical to the previous generator. Do not review, refactor, or
// improve it. Only the first two segments of x-fern-sdk-group-name are
// considered, so deeply nested namespaces (e.g. acs.encoders.simulate) are
// generated as standalone classes but never wired to a parent property.
// TODO: Delete this file and use blueprint.namespaces parent/child
// relationships once generated output is allowed to change, wiring deeply
// nested namespaces to a property on their parent class at the same time.

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
