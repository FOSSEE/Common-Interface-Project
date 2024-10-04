const getXsltProcessor = async () => {
  const xcos2xml = '/xcos2xml.xsl'
  const response = await fetch(xcos2xml)
  const text = await response.text()
  const parser = new DOMParser()
  const xsl = parser.parseFromString(text, 'application/xml')
  const processor = new XSLTProcessor()
  processor.importStylesheet(xsl)
  return processor
}

const getSplitXsltProcessor = async () => {
  const xcos2xml = '/splitblock.xsl'
  const response = await fetch(xcos2xml)
  const text = await response.text()
  const parser = new DOMParser()
  const xsl = parser.parseFromString(text, 'application/xml')
  const processor = new XSLTProcessor()
  processor.importStylesheet(xsl)
  return processor
}

export const transformXcos = async (xmlDoc) => {
  const splitBlock = /<SplitBlock /g
  const splitProcessor = await getSplitXsltProcessor()
  let dataDump = new XMLSerializer().serializeToString(xmlDoc)
  let count = dataDump.match(splitBlock).length
  console.log('count=', count)
  while (count > 0) {
    xmlDoc = splitProcessor.transformToDocument(xmlDoc)
    dataDump = new XMLSerializer().serializeToString(xmlDoc)
    const matches = dataDump.match(splitBlock)
    const newCount = matches ? matches.length : 0
    if (newCount !== count - 1) {
      console.error('newCount=', newCount, ', count=', count)
    }
    count = newCount
    console.log('count=', count)
  }
  const processor = await getXsltProcessor()
  xmlDoc = processor.transformToDocument(xmlDoc)
  return xmlDoc
}
