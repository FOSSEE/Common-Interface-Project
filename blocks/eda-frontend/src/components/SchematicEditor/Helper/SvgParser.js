import mxGraphFactory from 'mxgraph'

const {
  mxPoint
} = new mxGraphFactory();

let pinOrientation
let x_pos, y_pos
let width, height

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

  const block_name = component.name;
  const pins = []
  width = component.block_width
  height = component.block_height

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
    explicit_input_ports: component.initial_explicit_input_ports,
    implicit_input_ports: component.initial_implicit_input_ports,
    control_ports: component.initial_control_ports,
    explicit_output_ports: component.initial_explicit_output_ports,
    implicit_output_ports: component.initial_implicit_output_ports,
    command_ports: component.initial_command_ports,
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

  let ports = component.initial_explicit_input_ports + component.initial_implicit_input_ports;
  for (let i = 0; i < ports; i++) {
      if (i < component.initial_explicit_input_ports)
        pinOrientation = 'ExplicitInputPort';
    else
        pinOrientation = 'ImplicitInputPort';

    x_pos = 0;
    y_pos = (i + 1) / (ports + 1);

    pins[i] = graph.insertVertex(v1, null, null, x_pos, y_pos, 8, 8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].geometry.offset = new mxPoint(-8, -4);
    pins[i].ParentComponent = v1.id
  }

  ports = component.initial_explicit_output_ports + component.initial_implicit_output_ports;
  for (let i = 0; i < ports; i++) {
      if (i < component.initial_explicit_output_ports)
        pinOrientation = 'ExplicitOutputPort';
    else
        pinOrientation = 'ImplicitOutputPort';

    x_pos = 1;
    y_pos = (i + 1) / (ports + 1);

    pins[i] = graph.insertVertex(v1, null, null, x_pos, y_pos, 8, 8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].geometry.offset = new mxPoint(0, -4);
    pins[i].ParentComponent = v1.id
  }

  ports = component.initial_control_ports;
  for (let i = 0; i < ports; i++) {
    pinOrientation = 'ControlPort';

    x_pos = (i + 1) / (ports + 1);
    y_pos = 0;

    pins[i] = graph.insertVertex(v1, null, null, x_pos, y_pos, 8, 8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].geometry.offset = new mxPoint(-4, -8);
    pins[i].ParentComponent = v1.id
  }

  ports = component.initial_command_ports;
  for (let i = 0; i < ports; i++) {
    pinOrientation = 'CommandPort';

    x_pos = (i + 1) / (ports + 1);
    y_pos = 1;

    pins[i] = graph.insertVertex(v1, null, null, x_pos, y_pos, 8, 8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].geometry.offset = new mxPoint(-4, 0);
    pins[i].ParentComponent = v1.id
  }
}
