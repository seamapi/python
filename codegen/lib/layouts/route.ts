// Builds the template context for route class files (seam/routes/{namespace}.py).
// The context mirrors the output of the nextlove ClassFile#serializeToClass.

import {
  type ClassMethod,
  type ClassModel,
  sortClassMethodParameters,
} from '../class-model.js'

export interface MethodLayoutContext {
  name: string
  path: string
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

export interface RouteLayoutContext {
  className: string
  abstractClassName: string
  modelImportList: string
  childClasses: Array<{ namespace: string; className: string; module: string }>
  importResolveActionAttempt: boolean
  methods: MethodLayoutContext[]
}

const waitForActionAttemptParameter =
  'wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None'

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
    hasParams,
    signatureParams,
    params: sortedParameters.map(({ name }) => ({ name })),
    returnType: returnResource,
    returnsNone,
    pollsActionAttempt,
    isList,
    itemType: returnResourceItem,
    resAccessor: `res["${returnPath.join('"]["')}"]`,
  }
}

export const setRouteLayoutContext = (cls: ClassModel): RouteLayoutContext => {
  const validClasses = [
    `Abstract${cls.name}`,
    ...Array.from(
      new Set(
        cls.methods.map((m) =>
          m.returnResource.replace(/^List\[/, '').replace(/\]$/, ''),
        ),
      ),
    ),
  ].filter((classInstance) => classInstance !== '')

  const importResolveActionAttempt = cls.methods.some(
    ({ returnResource }) => returnResource === 'ActionAttempt',
  )

  return {
    className: cls.name,
    abstractClassName: `Abstract${cls.name}`,
    modelImportList: validClasses.filter((c) => c !== 'None').join(','),
    childClasses: cls.childClassIdentifiers.map((i) => ({
      namespace: i.namespace,
      className: i.className,
      module: `${cls.namespace}_${i.namespace}`,
    })),
    importResolveActionAttempt,
    methods: cls.methods.map(getMethodLayoutContext),
  }
}
