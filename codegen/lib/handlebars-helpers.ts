const PYTHON_KEYWORDS = new Set([
  'False',
  'None',
  'True',
  'and',
  'as',
  'assert',
  'async',
  'await',
  'break',
  'class',
  'continue',
  'def',
  'del',
  'elif',
  'else',
  'except',
  'finally',
  'for',
  'from',
  'global',
  'if',
  'import',
  'in',
  'is',
  'lambda',
  'nonlocal',
  'not',
  'or',
  'pass',
  'raise',
  'return',
  'try',
  'while',
  'with',
  'yield',
])

export const identity = (x: unknown): unknown => x

// Blueprint descriptions use Markdown, while Python docstrings use
// Sphinx/reStructuredText fields.
export const pythonDoc = (value: string): string =>
  value
    .trim()
    .replaceAll('"""', '\\"\\"\\"')
    .replaceAll(/(?<!`)`([^`\n]+)`(?!`)/g, '``$1``')
    .replaceAll(/\[([^\]]+)]\(([^)]+)\)/g, '`$1 <$2>`_')

export const indent = (value: string, spaces: number): string =>
  value.replaceAll('\n', `\n${' '.repeat(spaces)}`)

export const pythonIdentifier = (name: string): string =>
  PYTHON_KEYWORDS.has(name) ? `${name}_` : name

export const isListType = (type: string): boolean => type.startsWith('List[')

export const listItemType = (type: string): string => type.slice(5, -1)
