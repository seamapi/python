import fs from 'fs/promises'

const README_FILE = 'README.rst'
const CONTENTS_HEADING = 'Contents'
const CONTENTS_UNDERLINE = '--------'
const TOC_INDENT_LEVELS = {
  '-': 1,
  '~': 2,
  '^': 3,
}
const HEADING_UNDERLINE_REGEX = /^[-~^]+$/

async function generateTableOfContents(content) {
  const lines = content.split('\n')
  const headings = []
  let contentsHeadingIndex = -1
  let parsingHeadings = false

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim()
    const nextLine = lines[i + 1]?.trim() || ''

    if (line === CONTENTS_HEADING && nextLine.startsWith(CONTENTS_UNDERLINE)) {
      contentsHeadingIndex = i
      parsingHeadings = true // Start parsing headings after the "Contents" section
      i++ // Skip the underline
      continue
    }

    if (
      parsingHeadings &&
      nextLine &&
      nextLine.match(HEADING_UNDERLINE_REGEX)
    ) {
      const level = TOC_INDENT_LEVELS[nextLine[0]] || 0

      if (level > 0 && line) {
        headings.push({ text: line, level })
      }

      i++
    }
  }

  // Generate table of contents
  const toc = ['']
  headings.forEach((heading) => {
    const indent = '  '.repeat(heading.level - 1)

    toc.push(`${indent}* \`${heading.text} <${heading.text}_>\`_`)
    toc.push('')
  })

  return { toc, contentsHeadingIndex }
}

function findTocEndIndex(lines, startIndex) {
  return lines.findIndex(
    (line, index) =>
      index > startIndex + 2 &&
      !line.trim().startsWith('*') &&
      line.trim() !== '',
  )
}

async function updateReadme() {
  try {
    const content = await fs.readFile(README_FILE, 'utf8')
    const { toc, contentsHeadingIndex } = await generateTableOfContents(content)

    if (contentsHeadingIndex === -1) {
      throw new Error('Contents heading not found in the README.')
    }

    const lines = content.split('\n')
    const tocEndIndex = findTocEndIndex(lines, contentsHeadingIndex)

    const newContent = [
      ...lines.slice(0, contentsHeadingIndex + 2), // Include content before "Contents" heading, the heading itself and its underline
      ...toc,
      ...lines.slice(tocEndIndex),
    ].join('\n')

    await fs.writeFile(README_FILE, newContent)
    console.log(`Table of Contents has been updated in ${README_FILE}`)
  } catch (error) {
    console.error('Error updating README:', error.message)
    process.exit(1)
  }
}

updateReadme()
