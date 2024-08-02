import fs from 'fs/promises'

async function generateTOC(content) {
  const lines = content.split('\n')
  const headings = []
  let contentsIndex = -1
  let parsingHeadings = false

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim()
    const nextLine = lines[i + 1]?.trim() || ''

    if (line === 'Contents' && nextLine.startsWith('--------')) {
      contentsIndex = i
      parsingHeadings = true
      i++ // Skip the underline
      continue
    }

    if (parsingHeadings && nextLine && nextLine.match(/^[-~^]+$/)) {
      const level =
        nextLine[0] === '-'
          ? 1
          : nextLine[0] === '~'
            ? 2
            : nextLine[0] === '^'
              ? 3
              : 0
      if (level > 0 && line) {
        headings.push({ text: line, level })
      }
      i++ // Skip the underline
    }
  }

  const toc = [''] // Start with an empty line after the "Contents" section
  headings.forEach((heading) => {
    const indent = '  '.repeat(heading.level - 1)
    toc.push(`${indent}* \`${heading.text} <${heading.text}_>\`_`)
    toc.push('') // Add a newline after each item, including the last one
  })

  return { toc, contentsIndex }
}

async function updateReadme() {
  try {
    const content = await fs.readFile('README.rst', 'utf8')
    const { toc, contentsIndex } = await generateTOC(content)

    if (contentsIndex === -1) {
      console.error('Contents heading not found in the file.')
      process.exit(1)
    }

    const lines = content.split('\n')
    const contentStartIndex = lines.findIndex(
      (line, index) =>
        index > contentsIndex + 2 &&
        !line.trim().startsWith('*') &&
        line.trim() !== '',
    )

    const newContent = [
      ...lines.slice(0, contentsIndex + 2), // Include "Contents" and its underline
      ...toc,
      ...lines.slice(contentStartIndex),
    ].join('\n')

    await fs.writeFile('README.rst', newContent)
    console.log('Table of Contents has been updated in README.rst')
  } catch (error) {
    console.error('Error processing file:', error)
    process.exit(1)
  }
}

updateReadme()
