// Blueprint descriptions use Markdown, while the generated Python docstrings
// use Sphinx/reStructuredText fields. Normalize the Markdown constructs that
// would otherwise be displayed literally (or interpreted as invalid roles).
export const formatPythonDoc = (value: string): string =>
  value
    .trim()
    .replaceAll('"""', '\\"\\"\\"')
    .replaceAll(/(?<!`)`([^`\n]+)`(?!`)/g, '``$1``')
    .replaceAll(/\[([^\]]+)]\(([^)]+)\)/g, '`$1 <$2>`_')
