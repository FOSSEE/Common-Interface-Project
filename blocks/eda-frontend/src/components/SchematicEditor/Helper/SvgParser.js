let pinOrientation
let x_pos, y_pos
let width, height

// we need to divide the svg width and height by the same number in order to maintain the aspect ratio.
export const default_scale = 5;

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

  const block_name = component.main_category + '-' + component.blockprefix + '-' + component.name;
  const pins = []
  // make the component images smaller by scaling
  width = component.block_width / default_scale
  height = component.block_height / default_scale

  const v1 = graph.insertVertex(
    parent,
    null,
    null,
    x,
    y,
    width,
    height,
    block_name
  )
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

      x_pos = width / 2 + blockport.port_x / default_scale;
      y_pos = height / 2 - blockport.port_y / default_scale;

      pinOrientation = blockport.port_orientation;
      let portStyle = "defaultPin" + pinOrientation;

      pins[i] = graph.insertVertex(v1, null, blockport.port_number, x_pos, y_pos, 0.5, 0.5, portStyle)
      pins[i].geometry.relative = false;
      pins[i].ParentComponent = v1.id;
  }
}
