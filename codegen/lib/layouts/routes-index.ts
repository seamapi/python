// Builds the template context for seam/routes/__init__.py.
// Holds AbstractRoutes alongside the concrete Routes class, mirroring how each
// route module pairs its abstract class with its implementation.
// Mirrors the nextlove routes.py.template.ts.

import { pascalCase } from 'change-case'

interface AbstractRoutesLayoutContext {
  className: string
  namespaces: Array<{ namespace: string; abstractClassName: string }>
}

export interface RoutesIndexLayoutContext {
  namespaces: Array<{
    namespace: string
    className: string
    abstractClassName: string
    asyncClassName: string
    asyncAbstractClassName: string
  }>
  abstractRoutes: AbstractRoutesLayoutContext
  asyncAbstractRoutes: AbstractRoutesLayoutContext
}

export const setRoutesIndexLayoutContext = (
  topLevelNamespaces: string[],
): RoutesIndexLayoutContext => ({
  namespaces: topLevelNamespaces.map((ns) => ({
    namespace: ns,
    className: pascalCase(ns),
    abstractClassName: `Abstract${pascalCase(ns)}`,
    asyncClassName: `Async${pascalCase(ns)}`,
    asyncAbstractClassName: `AbstractAsync${pascalCase(ns)}`,
  })),
  abstractRoutes: {
    className: 'AbstractRoutes',
    namespaces: topLevelNamespaces.map((ns) => ({
      namespace: ns,
      abstractClassName: `Abstract${pascalCase(ns)}`,
    })),
  },
  asyncAbstractRoutes: {
    className: 'AbstractAsyncRoutes',
    namespaces: topLevelNamespaces.map((ns) => ({
      namespace: ns,
      abstractClassName: `AbstractAsync${pascalCase(ns)}`,
    })),
  },
})
