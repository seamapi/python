import { dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

import layouts from '@metalsmith/layouts'
import { createBlueprint, type TypesModuleInput } from '@seamapi/blueprint'
import { getHandlebarsPartials } from '@seamapi/smith'
import * as types from '@seamapi/types/connect'
import { deleteAsync } from 'del'
import Metalsmith from 'metalsmith'

import { helpers, routes } from './lib/index.js'

const rootDir = dirname(fileURLToPath(import.meta.url))

await Promise.all([deleteAsync('./seam/routes')])

const partials = await getHandlebarsPartials(`${rootDir}/layouts/partials`)

// Build the Blueprint with omitUndocumented so undocumented routes,
// namespaces, endpoints, parameters, resources, events, action attempts, and
// properties are stripped out before codegen runs.
const setBlueprint = async (
  _files: Metalsmith.Files,
  metalsmith: Metalsmith,
): Promise<void> => {
  const blueprint = await createBlueprint(types as TypesModuleInput, {
    omitUndocumented: true,
  })
  Object.assign(metalsmith.metadata(), { blueprint })
}

Metalsmith(rootDir)
  .source('./content')
  .destination('../')
  .clean(false)
  .use(setBlueprint)
  .use(routes)
  .use(
    layouts({
      default: 'default.hbs',
      engineOptions: {
        noEscape: true,
        helpers,
        partials,
      },
    }),
  )
  .build((err) => {
    if (err != null) throw err
  })
