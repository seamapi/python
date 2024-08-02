import fs from 'fs/promises'

async function generateTableOfContents(content) {
  const lines = content.split('\n')
  const headings = []
  let contentsHeadingIndex = -1
  let parsingHeadings = false

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim()
    const nextLine = lines[i + 1]?.trim() || ''

    if (line === 'Contents' && nextLine.startsWith('--------')) {
      contentsHeadingIndex = i
      parsingHeadings = true // Start parsing headings after the "Contents" section
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

  // Generate table of contents
  const toc = [''] // Start with an empty line after the "Contents" section
  headings.forEach((heading) => {
    const indent = '  '.repeat(heading.level - 1)
    toc.push(`${indent}* \`${heading.text} <${heading.text}_>\`_`)
    toc.push('') // Add a newline after each item
  })

  return { toc, contentsHeadingIndex }
}

async function updateReadme() {
  try {
    const content = await fs.readFile('README.rst', 'utf8')
    const { toc, contentsHeadingIndex } = await generateTableOfContents(content)

    if (contentsHeadingIndex === -1) {
      console.error('Contents heading not found in the README.')
      process.exit(1)
    }

    const lines = content.split('\n')
    const tocTableEndIndex = lines.findIndex(
      (line, index) =>
        index > contentsHeadingIndex + 2 &&
        !line.trim().startsWith('*') &&
        line.trim() !== '',
    )

    const newContent = [
      ...lines.slice(0, contentsHeadingIndex + 2), // Include readme content before "Contents" heading, the heading itself and its underline
      ...toc,
      ...lines.slice(tocTableEndIndex), // Include all content after the previous TOC
    ].join('\n')

    await fs.writeFile('README.rst', newContent)
    console.log('Table of Contents has been updated in README.rst')
  } catch (error) {
    console.error('Error processing file:', error)
    process.exit(1)
  }
}

updateReadme()
