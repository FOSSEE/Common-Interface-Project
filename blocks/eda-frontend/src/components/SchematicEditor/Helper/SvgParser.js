/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import 'mxgraph/javascript/src/css/common.css'

import mxGraphFactory from 'mxgraph'

const {
  mxPoint
} = new mxGraphFactory()

// we need to divide the svg width and height by the same number in order to maintain the aspect ratio.
export const defaultScale = parseFloat(process.env.REACT_APP_BLOCK_SCALE)
export const portSize = parseFloat(process.env.REACT_APP_PORT_SIZE)
export const parameterCount = 40

export function getParameter (i) {
  if (i < 10) { return 'p00' + i.toString() } else if (i < 100) { return 'p0' + i.toString() } else { return 'p' + i.toString() }
}

export function getSvgMetadata (graph, parent, evt, target, x, y, component) {
  // calls extractData and other MXGRAPH functions
  // initialize information from the svg meta
  // plots pinnumbers and component labels.

  const allowedPart = [0, 1]
  const allowedDmg = [0, 1]

  const blockName = component.block_name
  const pins = []
  // make the component images smaller by scaling
  const width = component.block_width / defaultScale
  const height = component.block_height / defaultScale

  const v1 = graph.insertVertex(parent, null, null, x, y, width, height, blockName)
  v1.CellType = 'Component'
  v1.blockprefix = component.blockprefix.name
  v1.displayProperties = {
    blockport_set: component.blockport_set,
    display_parameter: component.initial_display_parameter
  }
  const parameterValues = {}
  for (let i = 0; i < parameterCount; i++) {
    const p = getParameter(i) + '_value'
    const pinitial = p + '_initial'
    parameterValues[p] = component[pinitial]
  }
  v1.parameter_values = parameterValues

  v1.setConnectable(false)

  const blockports = component.blockport_set
  const ports = blockports.length
  for (let i = 0; i < ports; i++) {
    const blockport = blockports[i]
    if (!allowedPart.includes(blockport.port_part)) { continue }
    if (!allowedDmg.includes(blockport.port_dmg)) { continue }
    if (blockport.port_name === 'NC') { continue }

    const xPos = 1 / 2 + blockport.port_x / defaultScale / width
    const yPos = 1 / 2 - blockport.port_y / defaultScale / height

    const portOrientation = blockport.port_orientation
    let pointX
    let pointY
    switch (portOrientation) {
      case 'ExplicitInputPort':
      case 'ImplicitInputPort':
        pointX = -portSize
        pointY = -portSize / 2
        break
      case 'ControlPort':
        pointX = -portSize / 2
        pointY = -portSize
        break
      case 'ExplicitOutputPort':
      case 'ImplicitOutputPort':
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
    const point = new mxPoint(pointX, pointY)

    const vp = graph.insertVertex(v1, null, null, xPos, yPos, portSize, portSize, portOrientation)
    vp.geometry.relative = true
    vp.geometry.offset = point
    vp.CellType = 'Pin'
    vp.ParentComponent = v1.id
    pins[i] = vp
  }
}
