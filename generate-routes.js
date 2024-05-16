import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

import {
  generatePythonSDK as generateSdk,
  writeFs,
} from '@seamapi/nextlove-sdk-generator'
import { openapi } from '@seamapi/types/connect'
import { deleteAsync } from 'del'

const libName = 'seam'

const rootPath = dirname(fileURLToPath(import.meta.url))
const outputPath = resolve(rootPath, libName, 'routes')

await deleteAsync(outputPath)

const fileSystem = await generateSdk({
  openApiSpecObject: openapi,
})

const files = Object.entries(fileSystem).filter(([fileName]) =>
  fileName.startsWith(`${libRoutesPath}/`),
)

writeFs(rootPath, Object.fromEntries(files))
