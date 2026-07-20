// Ported from @seamapi/nextlove-sdk-generator lib/openapi/get-filtered-routes.ts.
// TODO: Use route.isUndocumented from @seamapi/blueprint once generated output
// is allowed to change.

import type { OpenapiSchema, Route } from './types.js'

export function getFilteredRoutes(openapi: OpenapiSchema): Route[] {
  return Object.entries(openapi.paths)
    .filter(([, pathSchema]) => {
      const post = pathSchema.post
      if (post == null) return false
      const summary = post.summary ?? ''

      const isDocumented = post['x-undocumented'] == null
      const isSeamInternalRoute = summary.startsWith('/seam/')

      return isDocumented && !isSeamInternalRoute
    })
    .map(([path, route]) => ({ path, ...route }) as Route)
}
