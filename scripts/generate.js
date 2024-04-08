import { generatePythonSDK, writeFs } from '@seamapi/nextlove-sdk-generator'
import { openapi } from '@seamapi/types/connect'
import path from 'path'
import { fileURLToPath } from 'url'

const SEAM_DIRECTORY_PREFIX = 'seam/'
const OUTPUT_DIRECTORY = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  '../',
)

const main = async () => {
  try {
    const pythonSdkFileSystem = await generatePythonSDK({
      openApiSpecObject: openapi,
    })

    const seamFiles = Object.entries(pythonSdkFileSystem).filter(([fileName]) =>
      fileName.startsWith(SEAM_DIRECTORY_PREFIX),
    )

    writeFs(OUTPUT_DIRECTORY, Object.fromEntries(seamFiles))

    console.log('Python SDK generated successfully!')
  } catch (error) {
    console.error('Failed to generate SDK:', error)
  }
}

await main()
