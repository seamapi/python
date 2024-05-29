import { createFake } from '@seamapi/fake-seam-connect'

async function startFakeSeamServer() {
  try {
    const fake = await createFake()
    await fake.seed()
    await fake.startServer()

    const endpoint = fake.serverUrl
    if (!endpoint) throw new Error('Fake endpoint is null')

    const res = await fetch(`${endpoint}/health`)
    if (!res.ok) throw new Error('Fake Seam Connect unhealthy')

    console.log(endpoint) // Output the server URL
  } catch (err) {
    console.error('Error starting fake-seam-connect server:', err)
    process.exit(1)
  }
}

startFakeSeamServer()
