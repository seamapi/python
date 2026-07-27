// Builds the template context for seam/routes/__init__.py.
// Holds AbstractRoutes alongside the concrete Routes class, mirroring how each
// route module pairs its abstract class with its implementation.
// Mirrors the nextlove routes.py.template.ts.

import { pascalCase } from 'change-case'

export interface RoutesIndexLayoutContext {
  namespaces: Array<{
    namespace: string
    className: string
    abstractClassName: string
  }>
  routesNamespaces: Array<{ namespace: string; abstractClassName: string }>
}

export const setRoutesIndexLayoutContext = (
  topLevelNamespaces: string[],
): RoutesIndexLayoutContext => ({
  namespaces: topLevelNamespaces.map((ns) => ({
    namespace: ns,
    className: pascalCase(ns),
    abstractClassName: `Abstract${pascalCase(ns)}`,
  })),
  routesNamespaces: topLevelNamespaces.map((ns) => ({
    namespace: ns,
    abstractClassName: `Abstract${pascalCase(ns)}`,
  })),
})
