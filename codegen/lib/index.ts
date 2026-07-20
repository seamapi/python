import { handlebarsHelpers } from '@seamapi/smith'

import * as customHelpers from './handlebars-helpers.js'

export const helpers = { ...handlebarsHelpers, ...customHelpers }

export * from './routes.js'
