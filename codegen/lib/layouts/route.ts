// Builds the template context for route class files (seam/routes/{namespace}.py).
// Each module holds the abstract route class alongside its concrete
// implementation. The context mirrors the output of the nextlove
// ClassFile#serializeToClass.

import {
  type ClassMethod,
  type ClassModel,
  sortClassMethodParameters,
} from '../class-model.js'

export interface MethodLayoutContext {
  name: string
  path: string
  docstring: string
  hasParams: boolean
  signatureParams: string
  params: Array<{ name: string }>
  returnType: string
  returnsNone: boolean
  pollsActionAttempt: boolean
  isList: boolean
  itemType: string
  resAccessor: string
}

export interface AbstractClassLayoutContext {
  className: string
  docstring: string
  showPass: boolean
  childProperties: Array<{ namespace: string; abstractClassName: string }>
  methods: Array<{
    name: string
    hasParams: boolean
    signatureParams: string
    returnType: string
    docstring: string
  }>
}

export interface RouteLayoutContext {
  className: string
  abstractClassName: string
  docstring: string
  abstractClass: AbstractClassLayoutContext
  resourceImportList: string
  childClasses: Array<{
    namespace: string
    className: string
    abstractClassName: string
    module: string
  }>
  importResolveActionAttempt: boolean
  methods: MethodLayoutContext[]
}

const waitForActionAttemptParameter =
  'wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None'

const cleanDoc = (value: string): string =>
  value.trim().replaceAll('"""', '\\"\\"\\"')

const indentDoc = (value: string, spaces: number): string =>
  value.replaceAll('\n', `\n${' '.repeat(spaces)}`)

const methodDocstring = (
  method: ClassMethod,
  sortedParameters: ClassMethod['parameters'],
): string => {
  const lines = [cleanDoc(method.description)]

  for (const parameter of sortedParameters) {
    const deprecated = parameter.isDeprecated
      ? `Deprecated${parameter.deprecationMessage === '' ? '.' : `: ${cleanDoc(parameter.deprecationMessage)}`}`
      : ''
    const description = cleanDoc(parameter.description)
    lines.push(
      '',
      `:param ${parameter.name}: ${[deprecated, description].filter(Boolean).join(' ')}`,
      `:type ${parameter.name}: ${parameter.type}`,
    )
  }

  if (method.returnResource === 'ActionAttempt') {
    lines.push(
      '',
      ':param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.',
      ':type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]',
    )
  }

  if (method.returnResource !== 'None') {
    lines.push(
      '',
      `:returns: ${cleanDoc(method.responseDescription)}`,
      `:rtype: ${method.returnResource}`,
    )
  }

  if (method.isDeprecated) {
    lines.push(
      '',
      '.. deprecated::',
      `   ${cleanDoc(method.deprecationMessage) || 'This method is deprecated.'}`,
    )
  }

  return lines.filter((line, index) => line !== '' || index !== 0).join('\n')
}

export const getMethodLayoutContext = (
  method: ClassMethod,
): MethodLayoutContext => {
  const { methodName, path, parameters, returnPath, returnResource } = method

  let returnResourceItem = returnResource
  const isList = returnResourceItem.startsWith('List[')

  if (isList) {
    returnResourceItem = returnResource.slice(5, -1)
  }

  const pollsActionAttempt = returnResource === 'ActionAttempt'
  const returnsNone = returnResourceItem === 'None'
  const hasParams = parameters.length > 0

  const sortedParameters = sortClassMethodParameters(parameters)

  const signatureParams = sortedParameters
    .map(({ name, type, required }) =>
      (required ?? false)
        ? `${name}: ${type}`
        : `${name}: Optional[${type}] = None`,
    )
    .concat(pollsActionAttempt ? [waitForActionAttemptParameter] : [])
    .join(', ')

  return {
    name: methodName,
    path,
    docstring: indentDoc(methodDocstring(method, sortedParameters), 8),
    hasParams,
    signatureParams,
    params: sortedParameters.map(({ name }) => ({ name })),
    returnType: returnResource,
    returnsNone,
    pollsActionAttempt,
    isList,
    itemType: returnResourceItem,
    resAccessor:
      returnPath.length > 0 ? `res["${returnPath.join('"]["')}"]` : '',
  }
}

export const setRouteLayoutContext = (cls: ClassModel): RouteLayoutContext => {
  const resourceClasses = Array.from(
    new Set(
      cls.methods.map((m) =>
        m.returnResource.replace(/^List\[/, '').replace(/\]$/, ''),
      ),
    ),
  ).filter((className) => className !== '' && className !== 'None')

  const importResolveActionAttempt = cls.methods.some(
    ({ returnResource }) => returnResource === 'ActionAttempt',
  )

  const abstractClassName = `Abstract${cls.name}`
  const classDocstring = cls.isDeprecated
    ? indentDoc('.. deprecated::\n   This route is deprecated.', 4)
    : ''

  return {
    className: cls.name,
    abstractClassName,
    docstring: classDocstring,
    abstractClass: {
      className: abstractClassName,
      docstring: classDocstring,
      showPass:
        cls.methods.length === 0 && cls.childClassIdentifiers.length === 0,
      childProperties: cls.childClassIdentifiers.map((i) => ({
        namespace: i.namespace,
        abstractClassName: `Abstract${i.className}`,
      })),
      methods: cls.methods.map((method) => {
        const { name, hasParams, signatureParams, returnType, docstring } =
          getMethodLayoutContext(method)
        return { name, hasParams, signatureParams, returnType, docstring }
      }),
    },
    resourceImportList: resourceClasses.join(','),
    childClasses: cls.childClassIdentifiers.map((i) => ({
      namespace: i.namespace,
      className: i.className,
      abstractClassName: `Abstract${i.className}`,
      module: `${cls.namespace}_${i.namespace}`,
    })),
    importResolveActionAttempt,
    methods: cls.methods.map(getMethodLayoutContext),
  }
}
