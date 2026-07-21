// TEMPORARY: Minimal OpenAPI types ported from @seamapi/nextlove-sdk-generator.
// These only support the frozen output-parity workarounds in this directory.
// Do not review, refactor, or improve them.
// TODO: Delete this file and use @seamapi/blueprint types once generated
// output is allowed to change.

export interface PrimitiveSchema {
  type: 'string' | 'integer' | 'boolean' | 'number'
  enum?: string[]
  format?: string
}

export interface ArraySchema {
  type: 'array'
  items: PropertySchema
}

export interface ObjSchema {
  type: 'object'
  properties: Record<string, PropertySchema>
  required: string[]
}

export interface OneOfSchema {
  oneOf: PropertySchema[]
}

export interface AllOfSchema {
  allOf: PropertySchema[]
}

export interface RefSchema {
  $ref: string
}

export type PropertySchema =
  | PrimitiveSchema
  | ArraySchema
  | ObjSchema
  | OneOfSchema
  | AllOfSchema
  | RefSchema

export interface RoutePost {
  summary?: string
  requestBody?: {
    content?: Record<string, { schema: any }>
  }
  responses: Record<string, { content?: Record<string, { schema: any }> }>
  'x-fern-sdk-group-name'?: string[]
  'x-fern-sdk-method-name'?: string
  'x-fern-sdk-return-value'?: string
  'x-response-key'?: string | null
  'x-undocumented'?: string
  [key: string]: any
}

export interface Route {
  path: string
  post: RoutePost
  [key: string]: any
}

export interface OpenapiSchema {
  info: { title: string }
  paths: Record<string, { post?: RoutePost }>
  components: { schemas: Record<string, PropertySchema> }
}
