import 'mxgraph/javascript/src/css/common.css'

import mxGraphFactory from 'mxgraph'

const {
  mxPoint
} = new mxGraphFactory()

// we need to divide the svg width and height by the same number in order to maintain the aspect ratio.
export const defaultScale = parseFloat(process.env.REACT_APP_BLOCK_SCALE)
export const portSize = parseFloat(process.env.REACT_APP_PORT_SIZE)

function getParameter (i) {
  if (i < 10) { return 'p00' + i.toString() } else if (i < 100) { return 'p0' + i.toString() } else { return 'p' + i.toString() }
}

export function getSvgMetadata (graph, parent, evt, target, x, y, component) {
  // calls extractData and other MXGRAPH functions
  // initialize information from the svg meta
  // plots pinnumbers and component labels.

  const allowedPart = [0, 1]
  const allowedDmg = [0, 1]

  const block_name = component.block_name
  const pins = []
  // make the component images smaller by scaling
  const width = component.block_width / defaultScale
  const height = component.block_height / defaultScale

  const v1 = graph.insertVertex(parent, null, null, x, y, width, height, block_name)
  v1.CellType = 'Component'
  v1.block_id = component.id
  v1.blockprefix = component.blockprefix.name
  v1.displayProperties = {
    blockport_set: component.blockport_set,
    display_parameter: component.initial_display_parameter
  }
  const parameter_values = {}
  for (let i = 0; i < 40; i++) {
    const p = getParameter(i) + '_value'
    const pinitial = p + '_initial'
    parameter_values[p] = component[pinitial]
  }
  v1.parameter_values = parameter_values

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

    const port_orientation = blockport.port_orientation
    let point = null
    switch (port_orientation) {
      case 'ExplicitInputPort': case 'ImplicitInputPort': point = new mxPoint(-portSize, -portSize / 2); break
      case 'ControlPort': point = new mxPoint(-portSize / 2, -portSize); break
      case 'ExplicitOutputPort': case 'ImplicitOutputPort': point = new mxPoint(0, -portSize / 2); break
      case 'CommandPort': point = new mxPoint(-portSize / 2, 0); break
      default: point = new mxPoint(-portSize / 2, -portSize / 2); break
    }

    const vp = graph.insertVertex(v1, null, null, xPos, yPos, portSize, portSize, port_orientation)
    vp.geometry.relative = true
    vp.geometry.offset = point
    vp.CellType = 'Pin'
    pins[i] = vp
  }
}
