export const getXsltProcessor = async () => {
  const xcos2xml = '/xcos2xml.xsl'
  const response = await fetch(xcos2xml)
  const text = await response.text()
  const parser = new DOMParser()
  const xsl = parser.parseFromString(text, 'application/xml')
  const processor = new XSLTProcessor()
  processor.importStylesheet(xsl)
  return processor
}

export const getSplitXsltProcessor = async () => {
  const xcos2xml = '/splitblock.xsl'
  const response = await fetch(xcos2xml)
  const text = await response.text()
  const parser = new DOMParser()
  const xsl = parser.parseFromString(text, 'application/xml')
  const processor = new XSLTProcessor()
  processor.importStylesheet(xsl)
  return processor
}
