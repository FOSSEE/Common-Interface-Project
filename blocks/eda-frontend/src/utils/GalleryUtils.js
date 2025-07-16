import { saveAs } from 'file-saver'

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

const getGeometryXsltProcessor = async () => {
  const xcos2xml = '/geometry.xsl'
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

const splitBlockXPathCount = 'count(/XcosDiagram/mxGraphModel/root/SplitBlock)'

const countNodesByXPath = (xpath, contextNode) => {
  const result = contextNode.evaluate(xpath, contextNode, null, XPathResult.NUMBER_TYPE, null)

  return result.numberValue
}

export const transformXcos = async (xmlDoc) => {
  // saveXmlToFile('xcos.xml', xmlDoc)
  const splitProcessor = await getSplitXsltProcessor()
  xmlDoc = removeSplits1(xmlDoc, splitProcessor)
  // saveXmlToFile('xcos-split.xml', xmlDoc)
  const processor = await getXsltProcessor()
  xmlDoc = processor.transformToDocument(xmlDoc)
  // saveXmlToFile('xcos-xcos2xml.xml', xmlDoc)
  const geometryprocessor = await getGeometryXsltProcessor()
  xmlDoc = geometryprocessor.transformToDocument(xmlDoc)
  // saveXmlToFile('xcos-geometry.xml', xmlDoc)
  return xmlDoc
}

const removeOneSplit = (xmlDoc, count, splitProcessor) => {
  if (count === 0) {
    return { xmlDoc, count }
  }

  xmlDoc = splitProcessor.transformToDocument(xmlDoc)
  const newCount = countNodesByXPath(splitBlockXPathCount, xmlDoc)
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
    if (count === 0) {
      return xmlDoc
    }

    return removeNextSplit(xmlDoc, count, splitProcessor)
  }

  const count = countNodesByXPath(splitBlockXPathCount, xmlDoc)
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

  const count = countNodesByXPath(splitBlockXPathCount, xmlDoc)
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
  const geometryprocessor = await getGeometryXsltProcessor()
  xmlDoc = geometryprocessor.transformToDocument(xmlDoc)
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

export const styleToObject = (style) => {
  // To add semicolon at the end if it isn't already present.
  if (style[style.length - 1] !== ';') {
    style = style + ';'
  }
  const styleObject = {
  }

  let remainingStyle = style
  while (remainingStyle.length > 0) {
    const indexOfKeyValue = remainingStyle.indexOf(';')

    const indexOfKey = remainingStyle.indexOf('=')
    if (indexOfKey > 0 && indexOfKey < indexOfKeyValue) {
      const key = remainingStyle.substring(0, indexOfKey)
      const value = remainingStyle.substring(indexOfKey + 1, indexOfKeyValue)
      styleObject[key] = value
    } else {
      const key = 'default'
      const value = remainingStyle.substring(0, indexOfKeyValue)
      if (value !== '' && !(key in styleObject)) {
        styleObject[key] = value
      }
    }

    remainingStyle = remainingStyle.substring(indexOfKeyValue + 1)
  }

  return styleObject
}

export const objectToStyle = (styleObject) => {
  let style = ''

  for (const key in styleObject) {
    if (Object.hasOwnProperty.call(styleObject, key)) {
      const value = styleObject[key]
      if (value !== undefined && value !== null && value !== '') {
        if (key === 'default') {
          style += `${value};`
        } else {
          style += `${key}=${value};`
        }
      }
    }
  }

  return style
}

export const saveToFile = (filename, filetype, data) => {
  const blob = new Blob([data], { type: filetype + ';charset=utf-8' })
  saveAs(blob, filename)
}

export const saveXmlToFile = (filename, xmlDoc) => {
  const serializer = new XMLSerializer()
  const data = serializer.serializeToString(xmlDoc)
  saveToFile(filename, 'application/xml', data)
}

export const getUppercaseInitial = (str) => {
  const match = str.match(/[a-zA-Z]/)
  const char = match ? match[0] : str.charAt(0)
  return char.toUpperCase()
}

export const removeBySaveIdInPlace = (schematics, saveId) => {
  const index = schematics.findIndex(item => item.save_id === saveId)
  if (index !== -1) {
    schematics.splice(index, 1)
  }
}

export const sanitizeTitle = (title, replacement = '_') => {
  return title.replace(/[<>:"/\\|?* ]/g, replacement).trim()
}

export const generate_ids = (() => {
  let prefixCounter = 0

  const generate = (count) => {
    const prefix = prefixCounter.toString().padStart(9, '0')
    const ids = Array.from({ length: count }, (_, i) => {
      const hex = i.toString(16).padStart(4, '0')
      return `${prefix}:${hex}`
    })
    prefixCounter++
    return ids
  }

  generate.reset = () => {
    prefixCounter = 0
  }

  return generate
})()

export const updateMxGraphXML = (xmlString) => {
  const xmlDoc = new DOMParser().parseFromString(xmlString, 'application/xml')

  const idMap = new Map()

  // Step 1: Generate new IDs for all mxCell elements
  const cells = xmlDoc.querySelectorAll('mxCell[id]')
  const ids = generate_ids(cells.length)
  let count = 0
  cells.forEach(cell => {
    const oldId = cell.getAttribute('id')
    const newId = ids[count++]
    idMap.set(oldId, newId)
    cell.setAttribute('id', newId)
  })

  // Step 2: update ParentComponent and other references as needed
  cells.forEach(cell => {
    ['ParentComponent', 'sourceVertex', 'targetVertex'].forEach(attr => {
      const val = cell.getAttribute(attr)
      if (val && idMap.has(val)) {
        cell.setAttribute(attr, idMap.get(val))
      }
    })
  })

  // Step 3: Serialize back to XML
  return new XMLSerializer().serializeToString(xmlDoc)
}
