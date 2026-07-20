// Builds the template context for seam/routes/__init__.py.
// Mirrors the nextlove routes.py.template.ts.

import { pascalCase } from 'change-case'

export interface RoutesIndexLayoutContext {
  namespaces: Array<{ namespace: string; className: string }>
}

export const setRoutesIndexLayoutContext = (
  topLevelNamespaces: string[],
): RoutesIndexLayoutContext => ({
  namespaces: topLevelNamespaces.map((ns) => ({
    namespace: ns,
    className: pascalCase(ns),
  })),
})
