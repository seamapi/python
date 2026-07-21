// Ported from @seamapi/nextlove-sdk-generator lib/generate-python-sdk/class-file.ts.
// Holds the data previously carried by the nextlove ClassFile; all string
// serialization moved to the Handlebars layouts and their context builders.

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
  returnPath: Array<string | undefined>
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

// Verbatim port of the nextlove parameter comparator. The original
// expression `(a.position ?? a.required ? 1000 : 9999)` parses as
// `(a.position ?? a.required) ? 1000 : 9999`, so a parameter with
// position 0 is falsy and lands in the 9999 tier together with the
// optional parameters. Combined with a stable sort this yields: required
// parameters first (in schema order), then everything else (in schema
// order).
// TODO: Fix the operator precedence so position sorts a parameter first
// as originally intended, once generated output is allowed to change.
// Until then, do not "fix" it: the generated output must stay identical.
export const sortClassMethodParameters = (
  parameters: ClassMethodParameter[],
): ClassMethodParameter[] =>
  [...parameters].sort(
    (a, b) =>
      ((a.position ?? a.required) ? 1000 : 9999) -
      ((b.position ?? b.required) ? 1000 : 9999),
  )
