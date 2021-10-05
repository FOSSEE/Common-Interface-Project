import 'mxgraph/javascript/src/css/common.css'

import mxGraphFactory from 'mxgraph'
import { portSize } from './SvgParser'
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

export default function ToolbarTools (grid, unredo) {
  graph = grid

  undoManager = new mxUndoManager()
  const listener = function (sender, evt) {
    undoManager.undoableEditHappened(evt.getProperty('edit'))
  }
  graph.getModel().addListener(mxEvent.UNDO, listener)
  graph.getView().addListener(mxEvent.UNDO, listener)
}

// SAVE
export function Save (description = '') {
  XMLWireConnections()
  const enc = new mxCodec(mxUtils.createXmlDocument())
  const model = graph.getModel()
  const firstCell = model.cells[0]
  firstCell.appname = process.env.REACT_APP_NAME
  firstCell.description = description
  const node = enc.encode(model)
  const value = mxUtils.getXml(node)
  return value
}

// UNDO
export function Undo () {
  undoManager.undo()
}

// REDO
export function Redo () {
  undoManager.redo()
}

// Zoom IN
export function ZoomIn () {
  graph.zoomIn()
}

// ZOOM OUT
export function ZoomOut () {
  graph.zoomOut()
}

// ZOOM ACTUAL
export function ZoomAct () {
  graph.zoomActual()
}

// DELETE COMPONENT
export function DeleteComp () {
  graph.removeCells()
}

// CLEAR WHOLE GRID
export function ClearGrid () {
  graph.removeCells(graph.getChildVertices(graph.getDefaultParent()))
}

// ROTATE COMPONENT
export function Rotate () {
  const view = graph.getView()
  const cell = graph.getSelectionCell()
  const state = view.getState(cell, true)
  const vHandler = graph.createVertexHandler(state)
  if (cell != null) {
    vHandler.rotateCell(cell, 90, cell.getParent())
  }
  vHandler.destroy()
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
  let ground = 0
  for (const property in list) {
    const cell = list[property]
    if (cell.CellType.value === 'Component') {
      for (const child in cell.children) {
        const childVertex = cell.children[child]
        if (childVertex.CellType.value === 'Pin' && childVertex.edges === null) { // Checking if connections exist from a given pin
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
    if (cell.blockprefix === 'PWR') { // Checking for ground
      console.log('Ground is present')
      console.log(cell)
      ++ground
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
function ErcCheckNets () {
  const NoAddition = 'No ' + process.env.REACT_APP_BLOCK_NAME + ' added'
  const list = graph.getModel().cells // mapping the grid
  let vertexCount = 0
  let errorCount = 0
  let PinNC = 0
  let ground = 0
  for (const property in list) {
    const cell = list[property]
    if (cell.CellType.value === 'Component') {
      for (const child in cell.children) {
        console.log(cell.children[child])
        const childVertex = cell.children[child]
        if (childVertex.CellType.value === 'Pin' && childVertex.edges === null) {
          graph.getSelectionCell(childVertex)
          console.log('This pin is not connected')
          console.log(childVertex)
          ++PinNC
          ++errorCount
        }
      }
      ++vertexCount
    }
    if (cell.blockprefix === 'PWR') {
      console.log('Ground is present')
      console.log(cell)
      ++ground
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
export function GenerateNetList () {
  let r = 1
  let v = 1
  let c = 1
  let spiceModels = ''
  const netlist = {
    componentlist: [],
    nodelist: []
  }
  const erc = ErcCheckNets()
  let k = ''
  if (erc === false) {
    alert('ERC check failed')
  } else {
    const list = annotate(graph)
    for (const property in list) {
      if (list[property].CellType.value === 'Component' && list[property].blockprefix !== 'PWR') {
        const compobj = {
          name: '',
          node1: '',
          node2: '',
          magnitude: ''
        }
        const component = list[property]
        if (component.blockprefix === 'R') {
          k = k + component.blockprefix + r.toString()
          component.value = component.blockprefix + r.toString()
          component.properties.PREFIX = component.value
          ++r
        } else if (component.blockprefix === 'V') {
          console.log(component)
          k = k + component.blockprefix + v.toString()
          component.value = component.blockprefix + v.toString()
          component.properties.PREFIX = component.value
          ++v
        } else {
          k = k + component.blockprefix + c.toString()
          component.value = component.blockprefix + c.toString()
          component.properties.PREFIX = component.value
          ++c
        } 

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
                    } else if (pin.edges[wire].source.ParentComponent.blockprefix === 'PWR' || pin.edges[wire].target.ParentComponent.blockprefix === 'PWR') {
                      pin.edges[wire].node = 0
                      // pin.edges[wire].node = '0'
                      pin.edges[wire].value = 0
                      // k = k + ' ' + pin.edges[wire].node
                      pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                      pin.edges[wire].targetVertex = pin.edges[wire].target.id
                    } else {
                      pin.edges[wire].node = pin.edges[wire].source.ParentComponent.properties.PREFIX + '.' + pin.edges[wire].source.value
                      console.log('comp')
                      pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                      pin.edges[wire].targetVertex = pin.edges[wire].target.id

                      pin.edges[wire].value = pin.edges[wire].node
                    }
                    pin.edges[wire].value = pin.edges[wire].node
                  }
                  console.log('Check the wires here ')
                  console.log(pin.edges[wire].sourceVertex)
                  console.log(pin.edges[wire].targetVertex)
                }
                k = k + ' ' + pin.edges[0].node
              }
            }
          }
          compobj.name = component.blockprefix
          compobj.node1 = component.children[0].edges[0].node
          compobj.node2 = component.children[1].edges[0].node
          compobj.magnitude = 10
          netlist.componentlist.push(component.properties.PREFIX)
          netlist.nodelist.push(compobj.node2, compobj.node1)

        }
        console.log('component properties', component.properties)

        if (component.properties.PREFIX.charAt(0) === 'V' || component.properties.PREFIX.charAt(0) === 'v' || component.properties.PREFIX.charAt(0) === 'I' || component.properties.PREFIX.charAt(0) === 'i') {
          const comp = component.properties
          if (comp.NAME === 'SINE') {
            k = k + ` SIN(${comp.OFFSET} ${comp.AMPLITUDE} ${comp.FREQUENCY} ${comp.DELAY} ${comp.DAMPING_FACTOR} ${comp.PHASE} )`
          } else if (comp.NAME === 'EXP') {
            k = k + ` EXP(${comp.INITIAL_VALUE} ${comp.PULSED_VALUE} ${comp.FREQUENCY} ${comp.RISE_DELAY_TIME} ${comp.RISE_TIME_CONSTANT} ${comp.FALL_DELAY_TIME} ${comp.FALL_TIME_CONSTANT} )`
          } else if (comp.NAME === 'DC') {
            if (component.properties.VALUE !== undefined) {
              k = k + ' DC ' + component.properties.VALUE
              component.value = component.value + '\n' + component.properties.VALUE
            }
          } else if (comp.NAME === 'PULSE') {
            k = k + ` PULSE(${comp.INITIAL_VALUE} ${comp.PULSED_VALUE} ${comp.DELAY_TIME} ${comp.RISE_TIME} ${comp.FALL_TIME} ${comp.PULSE_WIDTH} ${comp.PERIOD} ${comp.PHASE} )`
          } else {
            if (component.properties.VALUE !== undefined) {
              k = k + ' ' + component.properties.VALUE
              component.value = component.value + '\n' + component.properties.VALUE
            }
          }
        } else {
          if (component.properties.VALUE !== undefined) {
            k = k + ' ' + component.properties.VALUE
            component.value = component.value + '\n' + component.properties.VALUE
          }
        }

        if (component.properties.EXTRA_EXPRESSION.length > 0) {
          k = k + ' ' + component.properties.EXTRA_EXPRESSION
          component.value = component.value + ' ' + component.properties.EXTRA_EXPRESSION
        }
        if (component.properties.MODEL.length > 0) {
          k = k + ' ' + component.properties.MODEL.split(' ')[1]
        }
        if (component.properties.MODEL.length > 0) {
          spiceModels += component.properties.MODEL + '\n'
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

export function GenerateCompList () {
  const list = annotate(graph)
  const netlist = []

  for (const property in list) {
    if (list[property].CellType.value === 'Component' && list[property].blockprefix !== 'PWR') {
      const compobj = {
        name: '',
        node1: '',
        node2: '',
        magnitude: ''
      }
      const component = list[property]
      compobj.name = component.blockprefix
      compobj.node1 = component.children[0].edges[0].node
      compobj.node2 = component.children[1].edges[0].node
      netlist.push(component.properties.PREFIX)
    }
  }

  return netlist
  
}

export function renderXML () {
  graph.view.refresh()
  const xml = 'null'
  const xmlDoc = mxUtils.parseXml(xml)
  parseXmlToGraph(xmlDoc, graph)
}
function parseXmlToGraph (xmlDoc, graph) {
  const cells = xmlDoc.documentElement.children[0].children
  const parent = graph.getDefaultParent()
  let v1

  graph.getModel().beginUpdate()
  try {
    for (let i = 0; i < cells.length; i++) {
      const cell = cells[i]
      const cellAttrs = cell.attributes
      const cellChildren = cell.children
      if (cellAttrs.CellType.value === 'Component') { // is component
        const style = cellAttrs.style.value
        const vertexId = Number(cellAttrs.id.value)
        const geom = cellChildren[0].attributes
        const xPos = (geom.x !== undefined) ? Number(geom.x.value) : 0
        const yPos = (geom.y !== undefined) ? Number(geom.y.value) : 0
        const height = Number(geom.height.value)
        const width = Number(geom.width.value)
        v1 = graph.insertVertex(parent, vertexId, null, xPos, yPos, width, height, style)
        v1.connectable = 0
        v1.CellType = 'Component'
        v1.block_id = Number(cellAttrs.block_id.value)
        v1.blockprefix = cellAttrs.blockprefix.value
        const blockport_set = []
        const cellChildrenBlockport_set = cellChildren[1].children[0]
        if (cellChildrenBlockport_set !== undefined) {
          for (const b of cellChildrenBlockport_set.children) {
            const bc = {}
            for (let i = 0, n = b.attributes.length; i < n; i++) {
              const key = b.attributes[i].nodeName
              const value = b.attributes[i].nodeValue
              bc[key] = value
            }
            blockport_set.push(bc)
          }
        }
        v1.displayProperties = {
          blockport_set: blockport_set,
          display_parameter: cellChildren[1].attributes.display_parameter.value
        }
        let parameter_values = {}
        const cellChildrenParameter_values = cellChildren[2].attributes.parameter_values
        if (cellChildrenParameter_values !== undefined) {
          parameter_values = cellChildrenParameter_values.value
        }
        v1.parameter_values = parameter_values
      } else if (cellAttrs.CellType.value === 'Pin') {
        const style = cellAttrs.style.value
        const vertexId = Number(cellAttrs.id.value)
        const geom = cellChildren[0].attributes
        const xPos = (geom.x !== undefined) ? Number(geom.x.value) : 0
        const yPos = (geom.y !== undefined) ? Number(geom.y.value) : 0
        let point = null
        switch (style) {
          case 'ExplicitInputPort': case 'ImplicitInputPort': point = new mxPoint(-portSize, -portSize / 2); break
          case 'ControlPort': point = new mxPoint(-portSize / 2, -portSize); break
          case 'ExplicitOutputPort': case 'ImplicitOutputPort': point = new mxPoint(0, -portSize / 2); break
          case 'CommandPort': point = new mxPoint(-portSize / 2, 0); break
          default: point = new mxPoint(-portSize / 2, -portSize / 2); break
        }
        const vp = graph.insertVertex(v1, vertexId, null, xPos, yPos, portSize, portSize, style)
        vp.geometry.relative = true
        vp.geometry.offset = point
        vp.CellType = 'Pin'
        vp.ParentComponent = v1
      } else if (cellAttrs.edge) { // is edge
        const edgeId = Number(cellAttrs.id.value)
        const source = Number(cellAttrs.sourceVertex.value)
        const target = Number(cellAttrs.targetVertex.value)
        const sourceCell = graph.getModel().getCell(source)
        const targetCell = graph.getModel().getCell(target)
        try {
          const edge = graph.insertEdge(parent, edgeId, null, sourceCell, targetCell)
          const firstChild = cellChildren[0].children[0]
          if (firstChild !== undefined) {
            edge.geometry.points = []
            const plist = firstChild.children
            for (const a of plist) {
              try {
                const xPos = Number(a.attributes.x.value)
                const yPos = Number(a.attributes.y.value)
                edge.geometry.points.push(new mxPoint(xPos, yPos))
              } catch (e) { console.log('error', e) }
            }
          }
          if (targetCell.edge === true) {
            edge.geometry.setTerminalPoint(new mxPoint(Number(cellAttrs.tarx.value), Number(cellAttrs.tary.value)), false)
          }
        } catch (e) {
          console.log(sourceCell)
          console.log(targetCell)
          console.log('error', e)
        }
      }
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

function XMLWireConnections () {
  const erc = true
  if (erc === false) {
    alert('ERC check failed')
  } else {
    const list = graph.getModel().cells
    for (const property in list) {
      if (list[property].CellType.value === 'Component' && list[property].blockprefix !== 'PWR') {
        const component = list[property]

        if (component.children !== null) {
          for (const child in component.children) {
            const pin = component.children[child]
            if (pin.vertex === true) {
              try {
                if (pin.edges !== null && pin.edges.length !== 0) {
                  for (const wire in pin.edges) {
                    if (pin.edges[wire].source !== null && pin.edges[wire].target !== null) {
                      if (pin.edges[wire].source.edge === true) {
                        pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                        pin.edges[wire].targetVertex = pin.edges[wire].target.id
                      } else if (pin.edges[wire].target.edge === true) {
                        pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                        pin.edges[wire].targetVertex = pin.edges[wire].target.id
                        pin.edges[wire].tarx = pin.edges[wire].geometry.targetPoint.x
                        pin.edges[wire].tary = pin.edges[wire].geometry.targetPoint.y
                      } else if (pin.edges[wire].source.ParentComponent.blockprefix === 'PWR' || pin.edges[wire].target.ParentComponent.blockprefix === 'PWR') {
                        pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                        pin.edges[wire].targetVertex = pin.edges[wire].target.id
                      } else {
                        pin.edges[wire].node = pin.edges[wire].source.ParentComponent.properties.PREFIX + '.' + pin.edges[wire].source.value
                        pin.edges[wire].sourceVertex = pin.edges[wire].source.id
                        pin.edges[wire].targetVertex = pin.edges[wire].target.id
                      }
                    }
                    console.log('Check the wires here ')
                    console.log(pin.edges[wire].sourceVertex)
                    console.log(pin.edges[wire].targetVertex)
                  }
                }
              } catch (e) { console.log('error', e) }
            }
          }
        }
      }
    }
  }
}
