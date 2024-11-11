/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import 'mxgraph/javascript/src/css/common.css'

import mxGraphFactory from 'mxgraph'
import { portSize, getParameter } from './SvgParser'
import { styleToObject, getPortType, InputPort, OutputPort } from './ComponentDrag'
import store from '../../../redux/store'
import { setModel, setNetlist } from '../../../redux/actions/index'

let graph
let undoManager

const {
  mxPrintPreview,
  mxConstants,
  mxRectangle,
  mxUtils,
  mxUndoManager,
  mxEvent,
  mxCodec,
  mxPoint
} = new mxGraphFactory()

export default function toolbarTools (grid, unredo) {
  graph = grid

  undoManager = new mxUndoManager()
  const listener = function (sender, evt) {
    undoManager.undoableEditHappened(evt.getProperty('edit'))
  }
  graph.getModel().addListener(mxEvent.UNDO, listener)
  graph.getView().addListener(mxEvent.UNDO, listener)
}

// SAVE
export function saveXml (description = '') {
  try {
    xmlWireConnections()
  } catch (e) {
    console.error('error', e)
  }
  const enc = new mxCodec(mxUtils.createXmlDocument())
  const model = graph.getModel()
  const firstCell = model.cells[0]
  firstCell.appname = process.env.REACT_APP_NAME
  firstCell.description = description
  const node = enc.encode(model)
  const pins = node.querySelectorAll("Object[as='errorFields'],Object[as='pins']")
  pins.forEach(pin => { pin.remove() })
  const value = mxUtils.getXml(node)
  return value
}

// UNDO
export function editorUndo () {
  undoManager.undo()
}

// REDO
export function editorRedo () {
  undoManager.redo()
}

// Zoom IN
export function editorZoomIn () {
  graph.zoomIn()
}

// ZOOM OUT
export function editorZoomOut () {
  graph.zoomOut()
}

// ZOOM ACTUAL
export function editorZoomAct () {
  graph.zoomActual()
}

// DELETE COMPONENT
export function deleteComp () {
  graph.removeCells()
}

// CLEAR WHOLE GRID
export function ClearGrid () {
  graph.removeCells(graph.getChildVertices(graph.getDefaultParent()))
}

// ROTATE COMPONENT
export function Rotate () {
  const cell = graph.getSelectionCell()
  if (cell != null && cell.CellType === 'Component') {
    const view = graph.getView()
    const state = view.getState(cell, true)
    const vHandler = graph.createVertexHandler(state)
    vHandler.rotateCell(cell, 90, cell.getParent())
    vHandler.destroy()
  }
}

// PRINT PREVIEW OF SCHEMATIC
export function PrintPreview () {
  // Matches actual printer paper size and avoids blank pages
  const scale = 0.8
  const headerSize = 50
  const footerSize = 50

  // Applies scale to page
  const pageFormat = { x: 0, y: 0, width: 1169, height: 827 }
  const pf = mxRectangle.fromRectangle(pageFormat || mxConstants.PAGE_FORMAT_A4_LANDSCAPE)
  pf.width = Math.round(pf.width * scale * graph.pageScale)
  pf.height = Math.round(pf.height * scale * graph.pageScale)

  // Finds top left corner of top left page
  const bounds = mxRectangle.fromRectangle(graph.getGraphBounds())
  bounds.x -= graph.view.translate.x * graph.view.scale
  bounds.y -= graph.view.translate.y * graph.view.scale

  const x0 = Math.floor(bounds.x / pf.width) * pf.width
  const y0 = Math.floor(bounds.y / pf.height) * pf.height

  const preview = new mxPrintPreview(graph, scale, pf, 0, -x0, -y0)
  preview.marginTop = headerSize * scale * graph.pageScale
  preview.marginBottom = footerSize * scale * graph.pageScale
  preview.autoOrigin = false

  const oldRenderPage = preview.renderPage
  preview.renderPage = function (w, h, x, y, content, pageNumber) {
    const div = oldRenderPage.apply(this, arguments)

    const header = document.createElement('div')
    header.style.position = 'absolute'
    header.style.boxSizing = 'border-box'
    header.style.fontFamily = 'Arial,Helvetica'
    header.style.height = (this.marginTop - 10) + 'px'
    header.style.textAlign = 'center'
    header.style.verticalAlign = 'middle'
    header.style.marginTop = 'auto'
    header.style.fontSize = '12px'
    header.style.width = '100%'
    header.style.fontWeight = '100'

    // Vertical centering for text in header/footer
    header.style.lineHeight = (this.marginTop - 10) + 'px'

    const footer = header.cloneNode(true)
    const title = store.getState().saveSchematicReducer.title
    mxUtils.write(header, title + ' - ' + process.env.REACT_APP_NAME + ' on Cloud')
    header.style.borderBottom = '1px solid blue'
    header.style.top = '0px'

    mxUtils.write(footer, 'Made with ' + process.env.REACT_APP_DIAGRAM_NAME + ' Editor - ' + pageNumber + ' - ' + process.env.REACT_APP_NAME + ' on Cloud')
    footer.style.borderTop = '1px solid blue'
    footer.style.bottom = '0px'

    div.firstChild.appendChild(footer)
    div.firstChild.appendChild(header)

    return div
  }

  preview.open()
}

// ERC CHECK FOR SCHEMATIC
export function ErcCheck () {
  const NoAddition = 'No ' + process.env.REACT_APP_BLOCK_NAME + ' added'
  const list = graph.getModel().cells // mapping the grid
  let vertexCount = 0
  let errorCount = 0
  let PinNC = 0
  const ground = 0
  for (const property in list) {
    const cell = list[property]
    if (cell.CellType === 'Component') {
      for (const child in cell.children) {
        const childVertex = cell.children[child]
        if (childVertex.CellType === 'Pin' && childVertex.edges === null) { // Checking if connections exist from a given pin
          ++PinNC
          ++errorCount
        } else {
          for (const w in childVertex.edges) {
            if (childVertex.edges[w].source === null || childVertex.edges[w].target === null) {
              ++PinNC
            }
          }
        }
      }
      ++vertexCount
    }
  }

  if (vertexCount === 0) {
    alert(NoAddition)
    ++errorCount
  } else if (PinNC !== 0) {
    alert('Pins not connected')
  } else if (ground === 0) {
    alert('Ground not connected')
  } else {
    if (errorCount === 0) {
      alert('ERC Check completed')
    }
  }
}

function ercCheckNets () {
  const NoAddition = 'No ' + process.env.REACT_APP_BLOCK_NAME + ' added'
  const list = graph.getModel().cells // mapping the grid
  let vertexCount = 0
  let errorCount = 0
  let PinNC = 0
  const ground = 0
  for (const property in list) {
    const cell = list[property]
    if (cell.CellType === 'Component') {
      for (const child in cell.children) {
        console.log(cell.children[child])
        const childVertex = cell.children[child]
        if (childVertex.CellType === 'Pin' && childVertex.edges === null) {
          graph.getSelectionCell(childVertex)
          console.log('This pin is not connected')
          console.log(childVertex)
          ++PinNC
          ++errorCount
        }
      }
      ++vertexCount
    }
  }
  if (vertexCount === 0) {
    alert(NoAddition)
    ++errorCount
    return false
  } else if (PinNC !== 0) {
    alert('Pins not connected')
    return false
  } else if (ground === 0) {
    alert('Ground not connected')
    return false
  } else {
    if (errorCount === 0) {
      return true
    }
  }
}

// GENERATE NETLIST
export function generateNetList () {
  let c = 1
  const spiceModels = ''
  const netlist = {
    componentlist: [],
    nodelist: []
  }
  const erc = ercCheckNets()
  let k = ''
  if (erc === false) {
    alert('ERC check failed')
  } else {
    const list = annotate(graph)
    for (const property in list) {
      if (list[property].CellType === 'Component' && list[property].blockprefix !== 'PWR') {
        const compobj = {
          name: '',
          node1: '',
          node2: '',
          magnitude: ''
        }
        const component = list[property]
        k = k + component.blockprefix + c.toString()
        component.value = component.blockprefix + c.toString()
        ++c

        if (component.children !== null) {
          for (const child in component.children) {
            const pin = component.children[child]
            if (pin.vertex === true) {
              if (pin.edges !== null && pin.edges.length !== 0) {
                for (const wire in pin.edges) {
                  if (pin.edges[wire].source !== null && pin.edges[wire].target !== null) {
                    if (pin.edges[wire].source.edge === true) {
                      console.log('wire')
                      console.log(pin.edges[wire].source)
                      console.log(pin.edges[wire].source.node)
                      pin.edges[wire].node = pin.edges[wire].source.node
                      pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                      pin.edges[wire].targetVertex = pin.edges[wire].target.id
                    } else if (pin.edges[wire].target.edge === true) {
                      console.log('wire')
                      console.log(pin.edges[wire].target)
                      console.log(pin.edges[wire].target.node)
                      pin.edges[wire].node = pin.edges[wire].target.node
                      pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                      pin.edges[wire].targetVertex = pin.edges[wire].target.id
                      pin.edges[wire].tarx = pin.edges[wire].geometry.targetPoint.x
                      pin.edges[wire].tary = pin.edges[wire].geometry.targetPoint.y
                    } else {
                      pin.edges[wire].node = '.' + pin.edges[wire].source.value
                      console.log('comp')
                      pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                      pin.edges[wire].targetVertex = pin.edges[wire].target.id

                      pin.edges[wire].value = pin.edges[wire].node
                    }
                    pin.edges[wire].value = pin.edges[wire].node
                  }
                  console.log('Check the wires here', pin.edges[wire].sourceVertex, pin.edges[wire].targetVertex)
                }
                k = k + ' ' + pin.edges[0].node
              }
            }
          }
          compobj.name = component.blockprefix
          compobj.node1 = component.children[0].edges[0].node
          compobj.node2 = component.children[1].edges[0].node
          compobj.magnitude = 10
          netlist.nodelist.push(compobj.node2, compobj.node1)
        }
        console.log('component parameter_values', component.parameter_values)

        k = k + ' \n'
      }
    }
  }
  store.dispatch(setModel(spiceModels))
  store.dispatch(setNetlist(k))
  graph.getModel().beginUpdate()
  try {
    graph.view.refresh()
  } finally {
    graph.getModel().endUpdate()
  }
  const a = new Set(netlist.nodelist)
  console.log(netlist.nodelist)
  console.log(a)
  const netobj = {
    models: spiceModels,
    main: k
  }
  return netobj
}

function annotate (graph) {
  return graph.getModel().cells
}

export function renderXML () {
  graph.view.refresh()
  const xml = 'null'
  const xmlDoc = mxUtils.parseXml(xml)
  parseXmlToGraph(xmlDoc, graph)
}

const PORTDIRECTIONS = {
  UNK: 0,
  LOR: 4,
  L2T: 5,
  L2R: 6,
  L2B: 7,
  TOB: 12,
  T2R: 13,
  T2B: 14,
  T2L: 15
}

export function getRotationParameters (stylename, rotation) {
  const RotateNames = ['ExplicitInputPort', 'ControlPort', 'ExplicitOutputPort', 'CommandPort',
    'ExplicitInputPort', 'ControlPort', 'ExplicitOutputPort', 'CommandPort']

  let rotatename
  if (stylename === 'ImplicitInputPort') {
    rotatename = 'ExplicitInputPort'
  } else if (stylename === 'ImplicitOutputPort') {
    rotatename = 'ExplicitOutputPort'
  } else {
    rotatename = stylename
  }

  let index = RotateNames.indexOf(rotatename)

  let portdirection = PORTDIRECTIONS.UNK
  if (rotatename === 'ExplicitInputPort' || rotatename === 'ExplicitOutputPort') {
    portdirection = PORTDIRECTIONS.LOR
  } else if (rotatename === 'ControlPort' || rotatename === 'CommandPort') {
    portdirection = PORTDIRECTIONS.TOB
  }

  const turns = Math.round(rotation / 90)

  if (turns !== 0) {
    index += turns
    rotatename = RotateNames[index]

    portdirection += turns
  }

  return { rotatename, portdirection }
}

export function getPins (portOrientation, v1) {
  let pins
  switch (portOrientation) {
    case 'ExplicitInputPort':
      v1.explicitInputPorts += 1
      pins = v1.pins?.explicitInputPorts
      break
    case 'ImplicitInputPort':
      v1.implicitInputPorts += 1
      pins = v1.pins?.implicitInputPorts
      break
    case 'ControlPort':
      v1.controlPorts += 1
      pins = v1.pins?.controlPorts
      break
    case 'ExplicitOutputPort':
      v1.explicitOutputPorts += 1
      pins = v1.pins?.explicitOutputPorts
      break
    case 'ImplicitOutputPort':
      v1.implicitOutputPorts += 1
      pins = v1.pins?.implicitOutputPorts
      break
    case 'CommandPort':
      v1.commandPorts += 1
      pins = v1.pins?.commandPorts
      break
    default:
      pins = null
      break
  }
  return pins
}

export function getPointXY (rotationParameters) {
  let pointX
  let pointY
  switch (rotationParameters.rotatename) {
    case 'ExplicitInputPort':
      pointX = -portSize
      pointY = -portSize / 2
      break
    case 'ControlPort':
      pointX = -portSize / 2
      pointY = -portSize
      break
    case 'ExplicitOutputPort':
      pointX = 0
      pointY = -portSize / 2
      break
    case 'CommandPort':
      pointX = -portSize / 2
      pointY = 0
      break
    default:
      pointX = -portSize / 2
      pointY = -portSize / 2
      break
  }
  return { pointX, pointY }
}

export function getXYPos (rotationParameters, xPos, yPos) {
  const xPosOld = xPos
  switch (rotationParameters.portdirection) {
    case PORTDIRECTIONS.L2T:
    case PORTDIRECTIONS.T2L:
      xPos = yPos
      yPos = xPosOld
      break
    case PORTDIRECTIONS.L2R:
      xPos = 1 - xPosOld
      /* same yPos */
      break
    case PORTDIRECTIONS.L2B:
      xPos = yPos
      yPos = 1 - xPosOld
      break
    case PORTDIRECTIONS.T2R:
      xPos = 1 - yPos
      yPos = xPosOld
      break
    case PORTDIRECTIONS.T2B:
      /* same xPos */
      yPos = 1 - yPos
      break
  }
  return { xPos, yPos }
}

function parseXmlToGraph (xmlDoc, graph) {
  const parent = graph.getDefaultParent()
  let v1
  let blockrotation
  graph.getModel().beginUpdate()

  let oldcellslength = 0
  let cells = xmlDoc.documentElement.children[0].children
  let cellslength = cells.length
  let remainingcells = []
  let portCount
  try {
    console.log('cellslength=', cellslength)
    while (cellslength > 0 && cellslength !== oldcellslength) {
      for (let i = 0; i < cellslength; i++) {
        const cell = cells[i]
        const cellAttrs = cell.attributes
        const cellChildren = cell.children
        if (cellAttrs.CellType?.value === 'Component') { // is component
          portCount = {
            ExplicitInputPort: 0,
            ImplicitInputPort: 0,
            ControlPort: 0,
            ExplicitOutputPort: 0,
            ImplicitOutputPort: 0,
            CommandPort: 0
          }
          const style = cellAttrs.style.value
          const styleObject = styleToObject(style)
          if (styleObject.rotation === undefined) {
            blockrotation = 0
          } else {
            blockrotation = parseInt(styleObject.rotation)
          }
          const vertexId = cellAttrs.id.value
          const geom = cellChildren[0].attributes
          const xPos = (geom.x !== undefined) ? Number(geom.x.value) : 0
          const yPos = (geom.y !== undefined) ? Number(geom.y.value) : 0
          const height = Number(geom.height.value)
          const width = Number(geom.width.value)
          v1 = graph.insertVertex(parent, vertexId, null, xPos, yPos, width, height, style)
          v1.connectable = 0
          v1.CellType = 'Component'
          v1.blockprefix = cellAttrs.blockprefix.value
          const blockportSet = []
          const cellChildrenBlockportSet = cellChildren[1].children[0]
          if (cellChildrenBlockportSet !== undefined) {
            for (const b of cellChildrenBlockportSet.children) {
              const bc = {}
              for (let i = 0, n = b.attributes.length; i < n; i++) {
                const key = b.attributes[i].nodeName
                const value = b.attributes[i].nodeValue
                bc[key] = value
              }
              blockportSet.push(bc)
            }
          }
          v1.displayProperties = {
            display_parameter: cellChildren[1].attributes.display_parameter.value
          }
          const parameterValues = {}
          const cellChildrenAttributes = cellChildren[2].attributes
          if (cellChildrenAttributes !== undefined) {
            const pattern = /^p[0-9]{3}_value$/
            const parameterCount = Object.values(cellChildrenAttributes).filter((value) => {
              return pattern.test(value.name)
            }).length
            for (let i = 0; i < parameterCount; i++) {
              const p = getParameter(i) + '_value'
              if (cellChildrenAttributes[p] !== undefined) {
                parameterValues[p] = cellChildrenAttributes[p].value
              }
            }
          }
          v1.parameter_values = parameterValues
          // Todo set v1.errorFields
          v1.explicitInputPorts = 0
          v1.implicitInputPorts = 0
          v1.explicitOutputPorts = 0
          v1.implicitOutputPorts = 0
          v1.controlPorts = 0
          v1.commandPorts = 0
          v1.simulationFunction = cellAttrs.simulationFunction?.value
        } else if (cellAttrs.CellType?.value === 'Pin') {
          const style = cellAttrs.style.value
          const styleObject = styleToObject(style)
          const stylename = styleObject.default
          let portrotation

          if (styleObject.rotation === undefined) {
            portrotation = 0
          } else {
            portrotation = parseInt(styleObject.rotation)
          }
          let rotation = portrotation - blockrotation
          if (stylename === 'ControlPort' || stylename === 'CommandPort') {
            rotation -= 90
          }
          if (rotation < 0) {
            rotation += 360
          }

          const vertexId = cellAttrs.id.value
          const geom = cellChildren[0].attributes
          console.log('CELLATTR:', cellAttrs)
          let xPos = (geom.x !== undefined) ? Number(geom.x.value) : 0
          let yPos = (geom.y !== undefined) ? Number(geom.y.value) : 0

          const rotationParameters = getRotationParameters(stylename, rotation)

          if (rotation !== 0) {
            console.log('Ports:', styleObject)
            console.log('DIFF:', rotation)
            console.log(geom, xPos, yPos, portSize)
            console.log('rotationParameters:', rotationParameters)
          }

          getPins(stylename, v1)

          const pointXY = getPointXY(rotationParameters)
          const pointX = pointXY.pointX
          const pointY = pointXY.pointY

          const xyPos = getXYPos(rotationParameters, xPos, yPos)
          xPos = xyPos.xPos
          yPos = xyPos.yPos

          const point = new mxPoint(pointX, pointY)
          const vp = graph.insertVertex(v1, vertexId, null, xPos, yPos, portSize, portSize, style)

          vp.geometry.relative = true
          vp.geometry.offset = point
          vp.CellType = 'Pin'
          let orderingname
          if (stylename === 'ImplicitInputPort') {
            orderingname = 'ExplicitInputPort'
          } else if (stylename === 'ImplicitOutputPort') {
            orderingname = 'ExplicitOutputPort'
          } else {
            orderingname = stylename
          }
          portCount[orderingname] += 1
          let ordering
          if (cellAttrs.ordering) {
            ordering = cellAttrs.ordering
          } else {
            ordering = portCount[orderingname]
          }

          vp.ordering = ordering
          vp.ParentComponent = v1.id
        } else if (cellAttrs.edge) { // is edge
          const edgeId = cellAttrs.id.value

          let source = cellAttrs.sourceVertex.value
          let target = cellAttrs.targetVertex.value
          let sourceCell = graph.getModel().getCell(source)
          let targetCell = graph.getModel().getCell(target)
          const msgSource = (sourceCell == null) ? ' (not found)' : ''
          const msgTarget = (targetCell == null) ? ' (not found)' : ''
          console.log(`ST ${source}${msgSource} ${target}${msgTarget}`)
          if (sourceCell == null || targetCell == null) {
            remainingcells.push(cell)
            continue
          }
          const firstChild = cellChildren[0].querySelector('Array[as=points]')
          const points = []
          if (firstChild !== null) {
            const plist = firstChild.children
            for (const a of plist) {
              try {
                const point = new mxPoint(Number(a.attributes.x.value), Number(a.attributes.y.value))
                points.push(point)
              } catch (e) { console.error('error', e) }
            }
          }

          const sourceType = getPortType(sourceCell)
          const targetType = getPortType(targetCell)
          if (sourceType.type2 !== OutputPort && targetType.type2 !== InputPort) {
            console.log('switch', source, target)
            const tmp = source
            source = target
            target = tmp
            console.log('sourceCell:', sourceCell)
            const tmpCell = sourceCell
            sourceCell = targetCell
            targetCell = tmpCell
            // const tmpsourcePoint = sourcePoint
            // sourcePoint = targetPoint
            // targetPoint = tmpsourcePoint
            points.reverse()
          }

          try {
            const edge = graph.insertEdge(parent, edgeId, null, sourceCell, targetCell)
            console.log('Points:', points)
            edge.geometry.points = points
            const terminalPoint = new mxPoint(Number(cellAttrs.tarx.value), Number(cellAttrs.tary.value))
            const terminalPoint2 = new mxPoint(Number(cellAttrs.tar2x.value), Number(cellAttrs.tar2y.value))
            if (targetCell?.edge === true) {
              edge.geometry.setTerminalPoint(terminalPoint2, false)
            }
            if (sourceCell?.edge === true) {
              edge.geometry.setTerminalPoint(terminalPoint, true)
            }
            console.log('edge:', edge)
          } catch (e) {
            console.log(sourceCell)
            console.log(targetCell)
            console.error('error', e)
          }
        }
      }

      oldcellslength = cellslength
      cells = remainingcells
      cellslength = remainingcells.length
      remainingcells = []
      console.log('cellslength=', cellslength, ', oldcellslength=', oldcellslength)
    }
    graph.view.refresh()
  } finally {
    graph.getModel().endUpdate()
  }
}

export function renderGalleryXML (xml) {
  graph.removeCells(graph.getChildVertices(graph.getDefaultParent()))
  graph.view.refresh()
  const xmlDoc = mxUtils.parseXml(xml)
  parseXmlToGraph(xmlDoc, graph)
}

function xmlWireConnections () {
  const list = graph.getModel().cells
  for (const component of Object.values(list)) {
    const children = component.children
    if (component.CellType !== 'Component' || component.blockprefix === 'PWR' || children === null) {
      continue
    }

    for (const pin of Object.values(children)) {
      if (pin.vertex !== true || pin.edges === null || pin.edges.length === 0) {
        continue
      }

      for (const edge of Object.values(pin.edges)) {
        if (edge.source === null || edge.target === null) {
          continue
        }
        console.log('edge.source:', edge, edge.source)
        edge.sourceVertex = edge.source.id
        edge.targetVertex = edge.target.id
        console.log('outside if', edge.source.edge, edge.target.edge)
        if (edge.source.edge === true) {

          edge.tarx = edge.geometry.sourcePoint.x
          edge.tary = edge.geometry.sourcePoint.y
          console.log('tarx', edge.tarx, edge.tary)
        }
        if (edge.target.edge === true) {

          edge.tar2x = edge.geometry.targetPoint.x
          edge.tar2y = edge.geometry.targetPoint.y
          console.log('tar2x', edge.tar2x, edge.tar2y)
        }


        console.log('Check the wires here', edge.sourceVertex, edge.targetVertex)
      }
    }
  }
}
