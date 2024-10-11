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

// handle display format of last saved status
export const getDateTime = (jsonDateTime) => {
  const date = new Date(jsonDateTime)
  const dateTimeFormat = new Intl.DateTimeFormat('en', { month: 'short', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' })
  const [{ value: month }, , { value: day }, , { value: hour }, , { value: minute }, , { value: second }] = dateTimeFormat.formatToParts(date)
  return `${day} ${month} ${hour}:${minute}:${second}`
}

// Display diagram created date (e.g : Created On 29 Jun 2020)
export const getDate = (jsonDate) => {
  const date = new Date(jsonDate)
  const dateTimeFormat = new Intl.DateTimeFormat('en', { year: 'numeric', month: 'short', day: '2-digit' })
  const [{ value: month }, , { value: day }, , { value: year }] = dateTimeFormat.formatToParts(date)
  return `${day}-${month}-${year}`
}
