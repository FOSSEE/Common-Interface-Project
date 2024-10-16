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

const splitBlock = /<SplitBlock /g

export const transformXcos = async (xmlDoc) => {
  const splitProcessor = await getSplitXsltProcessor()
  xmlDoc = removeSplits1(xmlDoc, splitProcessor)
  const processor = await getXsltProcessor()
  xmlDoc = processor.transformToDocument(xmlDoc)
  return xmlDoc
}

const removeOneSplit = (xmlDoc, count, splitProcessor) => {
  if (count === 0) {
    return { xmlDoc, count }
  }

  xmlDoc = splitProcessor.transformToDocument(xmlDoc)
  const dataDump = new XMLSerializer().serializeToString(xmlDoc)
  const matches = dataDump.match(splitBlock)
  const newCount = matches ? matches.length : 0
  if (newCount !== count - 1) {
    console.error('newCount=', newCount, ', count=', count)
    throw new Error('count mismatch')
  }
  return { xmlDoc, count: newCount }
}

const removeSplits1 = (xmlDoc, splitProcessor) => {
  const removeNextSplit = (xmlDoc, count, splitProcessor) => {
    const rv = removeOneSplit(xmlDoc, count, splitProcessor)
    xmlDoc = rv.xmlDoc
    count = rv.count
    console.log('count=', count)
    if (count === 0) {
      return xmlDoc
    }

    return removeNextSplit(xmlDoc, count, splitProcessor)
  }

  const dataDump = new XMLSerializer().serializeToString(xmlDoc)
  const count = dataDump.match(splitBlock).length
  console.log('count=', count)
  if (count === 0) {
    return xmlDoc
  }

  return removeNextSplit(xmlDoc, count, splitProcessor)
}

const removeSplits = async (xmlDoc, splitProcessor, delay) => {
  const removeNextSplit = async (xmlDoc, count, splitProcessor) => {
    const rv = removeOneSplit(xmlDoc, count, splitProcessor)
    xmlDoc = rv.xmlDoc
    count = rv.count
    console.log('count=', count)
    if (count === 0) {
      return xmlDoc
    }

    return new Promise((resolve) => {
      setTimeout(() => {
        const result = removeNextSplit(xmlDoc, count, splitProcessor)
        resolve(result)
      }, delay)
    })
  }

  const dataDump = new XMLSerializer().serializeToString(xmlDoc)
  const count = dataDump.match(splitBlock).length
  console.log('count=', count)
  if (count === 0) {
    return xmlDoc
  }

  return new Promise((resolve) => {
    setTimeout(() => {
      const result = removeNextSplit(xmlDoc, count, splitProcessor)
      resolve(result)
    }, delay)
  })
}

export const transformXcos2 = async (xmlDoc) => {
  const splitProcessor = await getSplitXsltProcessor()
  xmlDoc = await removeSplits(xmlDoc, splitProcessor, 1)
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
