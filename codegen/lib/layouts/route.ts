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
  httpVerb: string
  payloadVar: string
  payloadArg: string
  hasRequiredParameters: boolean
  hasPagination: boolean
  description: string
  responseDescription: string
  isDeprecated: boolean
  deprecationMessage: string
  params: Array<{
    name: string
    type: string
    isNullable: boolean
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
  isAsync: boolean
  isDeprecated: boolean
  showPass: boolean
  childProperties: Array<{ namespace: string; abstractClassName: string }>
  methods: MethodLayoutContext[]
}

export interface RouteLayoutContext {
  className: string
  abstractClassName: string
  asyncClassName: string
  asyncAbstractClassName: string
  isDeprecated: boolean
  abstractClass: AbstractClassLayoutContext
  asyncAbstractClass: AbstractClassLayoutContext
  resourceClasses: string[]
  childClasses: Array<{
    namespace: string
    className: string
    abstractClassName: string
    asyncClassName: string
    asyncAbstractClassName: string
    module: string
  }>
  importResolveActionAttempt: boolean
  importNull: boolean
  methods: MethodLayoutContext[]
}

const getRequestLayoutContext = (
  preferredMethod: string,
): Pick<MethodLayoutContext, 'httpVerb' | 'payloadVar' | 'payloadArg'> => {
  const httpVerb = preferredMethod.toLowerCase()

  if (preferredMethod === 'GET' || preferredMethod === 'DELETE') {
    return { httpVerb, payloadVar: 'params', payloadArg: 'params' }
  }

  return { httpVerb, payloadVar: 'json_payload', payloadArg: 'json' }
}

export const getMethodLayoutContext = (
  method: ClassMethod,
): MethodLayoutContext => ({
  name: method.methodName,
  path: method.path,
  ...getRequestLayoutContext(method.preferredMethod),
  hasRequiredParameters: method.hasRequiredParameters,
  hasPagination: method.hasPagination,
  description: method.description,
  responseDescription: method.responseDescription,
  isDeprecated: method.isDeprecated,
  deprecationMessage: method.deprecationMessage,
  params: sortClassMethodParameters(method.parameters).map((parameter) => ({
    name: parameter.name,
    type: parameter.type,
    isNullable: parameter.isNullable,
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

  if (resourceClasses.includes('ActionAttempt')) {
    resourceClasses.push('action_attempt_from_dict')
  }
  if (resourceClasses.includes('SeamEvent')) {
    resourceClasses.push('seam_event_from_dict')
  }

  const abstractClassName = `Abstract${cls.name}`
  const asyncClassName = `Async${cls.name}`
  const asyncAbstractClassName = `AbstractAsync${cls.name}`
  const methods = cls.methods.map(getMethodLayoutContext)

  const importNull = methods.some(({ params }) =>
    params.some(({ isNullable }) => isNullable),
  )

  const showPass =
    cls.methods.length === 0 && cls.childClassIdentifiers.length === 0

  return {
    className: cls.name,
    abstractClassName,
    asyncClassName,
    asyncAbstractClassName,
    isDeprecated: cls.isDeprecated,
    abstractClass: {
      className: abstractClassName,
      isAsync: false,
      isDeprecated: cls.isDeprecated,
      showPass,
      childProperties: cls.childClassIdentifiers.map((identifier) => ({
        namespace: identifier.namespace,
        abstractClassName: `Abstract${identifier.className}`,
      })),
      methods,
    },
    asyncAbstractClass: {
      className: asyncAbstractClassName,
      isAsync: true,
      isDeprecated: cls.isDeprecated,
      showPass,
      childProperties: cls.childClassIdentifiers.map((identifier) => ({
        namespace: identifier.namespace,
        abstractClassName: `AbstractAsync${identifier.className}`,
      })),
      methods,
    },
    resourceClasses,
    childClasses: cls.childClassIdentifiers.map((identifier) => ({
      namespace: identifier.namespace,
      className: identifier.className,
      abstractClassName: `Abstract${identifier.className}`,
      asyncClassName: `Async${identifier.className}`,
      asyncAbstractClassName: `AbstractAsync${identifier.className}`,
      module: `${cls.namespace}_${identifier.namespace}`,
    })),
    importResolveActionAttempt,
    importNull,
    methods,
  }
}
