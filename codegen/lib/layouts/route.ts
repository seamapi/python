// Builds the template context for route class files (seam/routes/{namespace}.py).
// The context contains semantic route data; Handlebars templates own all Python
// and docstring serialization.

import {
  type ClassMethod,
  type ClassModel,
  sortClassMethodParameters,
} from '../class-model.js'

export interface MethodLayoutContext {
  name: string
  path: string
  description: string
  responseDescription: string
  isDeprecated: boolean
  deprecationMessage: string
  params: Array<{
    name: string
    type: string
    description: string
    isDeprecated: boolean
    deprecationMessage: string
    required: boolean
  }>
  returnPath: string[]
  returnType: string
}

export interface AbstractClassLayoutContext {
  className: string
  isDeprecated: boolean
  showPass: boolean
  childProperties: Array<{ namespace: string; abstractClassName: string }>
  methods: MethodLayoutContext[]
}

export interface RouteLayoutContext {
  className: string
  abstractClassName: string
  isDeprecated: boolean
  abstractClass: AbstractClassLayoutContext
  resourceClasses: string[]
  childClasses: Array<{
    namespace: string
    className: string
    abstractClassName: string
    module: string
  }>
  importResolveActionAttempt: boolean
  methods: MethodLayoutContext[]
}

export const getMethodLayoutContext = (
  method: ClassMethod,
): MethodLayoutContext => ({
  name: method.methodName,
  path: method.path,
  description: method.description,
  responseDescription: method.responseDescription,
  isDeprecated: method.isDeprecated,
  deprecationMessage: method.deprecationMessage,
  params: sortClassMethodParameters(method.parameters).map((parameter) => ({
    name: parameter.name,
    type: parameter.type,
    description: parameter.description,
    isDeprecated: parameter.isDeprecated,
    deprecationMessage: parameter.deprecationMessage,
    required: parameter.required ?? false,
  })),
  returnPath: method.returnPath,
  returnType: method.returnResource,
})

export const setRouteLayoutContext = (cls: ClassModel): RouteLayoutContext => {
  const resourceClasses = Array.from(
    new Set(
      cls.methods.map((method) =>
        method.returnResource.replace(/^List\[/, '').replace(/\]$/, ''),
      ),
    ),
  ).filter((className) => className !== '' && className !== 'None')

  const importResolveActionAttempt = cls.methods.some(
    ({ returnResource }) => returnResource === 'ActionAttempt',
  )

  const abstractClassName = `Abstract${cls.name}`
  const methods = cls.methods.map(getMethodLayoutContext)

  return {
    className: cls.name,
    abstractClassName,
    isDeprecated: cls.isDeprecated,
    abstractClass: {
      className: abstractClassName,
      isDeprecated: cls.isDeprecated,
      showPass:
        cls.methods.length === 0 && cls.childClassIdentifiers.length === 0,
      childProperties: cls.childClassIdentifiers.map((identifier) => ({
        namespace: identifier.namespace,
        abstractClassName: `Abstract${identifier.className}`,
      })),
      methods,
    },
    resourceClasses,
    childClasses: cls.childClassIdentifiers.map((identifier) => ({
      namespace: identifier.namespace,
      className: identifier.className,
      abstractClassName: `Abstract${identifier.className}`,
      module: `${cls.namespace}_${identifier.namespace}`,
    })),
    importResolveActionAttempt,
    methods,
  }
}
