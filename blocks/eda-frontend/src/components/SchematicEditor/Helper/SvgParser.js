import 'mxgraph/javascript/src/css/common.css';

import mxGraphFactory from 'mxgraph';

const {
    mxPoint
} = new mxGraphFactory();

// we need to divide the svg width and height by the same number in order to maintain the aspect ratio.
export const default_scale = parseFloat(process.env.REACT_APP_BLOCK_SCALE);
export const port_size = parseFloat(process.env.REACT_APP_PORT_SIZE);

function getParameter(i) {
    if (i < 10)
        return 'p00' + i.toString();
    else if (i < 100)
        return 'p0' + i.toString();
    else
        return 'p' + i.toString();
}

export function getSvgMetadata (graph, parent, evt, target, x, y, component) {
  // calls extractData and other MXGRAPH functions
  // initialize information from the svg meta
  // plots pinnumbers and component labels.

  const allowed_part = [0, 1];
  const allowed_dmg = [0, 1];

  const block_name = component.block_name;
  const pins = []
  // make the component images smaller by scaling
  let width = component.block_width / default_scale
  let height = component.block_height / default_scale

  const v1 = graph.insertVertex(parent, null, null, x, y, width, height, block_name)
  v1.Component = true
  v1.CellType = 'Component'
  v1.block_id = component.id
  v1.displayProperties = {
    blockport_set: component.blockport_set,
    display_parameter: component.initial_display_parameter,
  }
  let parameter_values = {};
  for (let i = 0; i < 40; i++) {
      let p = getParameter(i) + '_value';
      let pinitial = p + '_initial';
      parameter_values[p] = component[pinitial];
  }
  v1.parameter_values = parameter_values;

  v1.setConnectable(false)

  let blockports = component.blockport_set;
  let ports = blockports.length;
  for (let i = 0; i < ports; i++) {
      let blockport = blockports[i];
      if (!allowed_part.includes(blockport.port_part))
          continue;
      if (!allowed_dmg.includes(blockport.port_dmg))
          continue;
      if (blockport.port_name === 'NC')
          continue;

      let x_pos = 1 / 2 + blockport.port_x / default_scale / width;
      let y_pos = 1 / 2 - blockport.port_y / default_scale / height;

      let port_orientation = blockport.port_orientation;
      let point = null;
      switch (port_orientation) {
          case 'ExplicitInputPort': case 'ImplicitInputPort': point = new mxPoint(-port_size, -port_size / 2); break;
          case 'ControlPort': point = new mxPoint(-port_size / 2, -port_size); break;
          case 'ExplicitOutputPort': case 'ImplicitOutputPort': point = new mxPoint(0, -port_size / 2); break;
          case 'CommandPort': point = new mxPoint(-port_size / 2, 0); break;
          default: point = new mxPoint(-port_size / 2, -port_size / 2); break;
      }

      var vp = graph.insertVertex(v1, null, null, x_pos, y_pos, port_size, port_size, port_orientation)
      vp.geometry.relative = true;
      vp.geometry.offset = point;
      vp.ParentComponent = v1.id;
      pins[i] = vp;
  }
}
