// Holds the class and method data assembled by the routes plugin; all string
// serialization lives in the Handlebars layouts and their context builders.

export interface ClassMethodParameter {
  name: string
  type: string
  position?: number | undefined
  required?: boolean | undefined
}

export interface ClassMethod {
  methodName: string
  path: string
  parameters: ClassMethodParameter[]
  returnPath: string[]
  returnResource: string
}

export interface ChildClassIdentifier {
  className: string
  namespace: string
}

export interface ClassModel {
  name: string
  namespace: string
  methods: ClassMethod[]
  childClassIdentifiers: ChildClassIdentifier[]
}

// Sort tiers: an explicit position first, then required parameters, then
// optional parameters. Array#sort is stable, so ties keep schema order.
const sortTier = ({ position, required }: ClassMethodParameter): number =>
  position ?? ((required ?? false) ? 1000 : 9999)

export const sortClassMethodParameters = (
  parameters: ClassMethodParameter[],
): ClassMethodParameter[] =>
  [...parameters].sort((a, b) => sortTier(a) - sortTier(b))
