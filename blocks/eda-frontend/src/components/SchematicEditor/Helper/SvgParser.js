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
    block_name,
    x,
    y,
    width,
    height,
    block_name
  )
  v1.Component = true
  v1.CellType = 'Component'
  v1.block_id = component.id
  v1.explicit_input_ports = component.initial_explicit_input_ports
  v1.implicit_input_ports = component.initial_implicit_input_ports
  v1.control_ports = component.initial_control_ports
  v1.explicit_output_ports = component.initial_explicit_output_ports
  v1.implicit_output_ports = component.initial_implicit_output_ports
  v1.command_ports = component.initial_command_ports
  v1.display_parameter = component.initial_display_parameter
  for (let i = 0; i < 40; i++) {
      let p = getParameter(i) + '_value';
      let pinitial = p + '_initial';
      v1[p] = component[pinitial];
  }

  var props = {}
  props.NAME = component.name
  v1.properties = props

  v1.setConnectable(false)

  let ports = component.initial_explicit_input_ports + component.initial_implicit_input_ports;
  for (let i = 0; i < ports; i++) {
      if (i < component.initial_explicit_input_ports)
        pinOrientation = 'ExplicitInputPort';
    else
        pinOrientation = 'ImplicitInputPort';

    x_pos = 0;
    y_pos = (i + 1) / (ports + 1);

    pins[i] = graph.insertVertex(v1, null, i, x_pos, y_pos, 0.8, 0.8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].pinType = 'Input'
    pins[i].ParentComponent = v1
    pins[i].PinNumber = i
  }

  ports = component.initial_explicit_output_ports + component.initial_implicit_output_ports;
  for (let i = 0; i < ports; i++) {
      if (i < component.initial_explicit_output_ports)
        pinOrientation = 'ExplicitOutputPort';
    else
        pinOrientation = 'ImplicitOutputPort';

    x_pos = 1;
    y_pos = (i + 1) / (ports + 1);

    pins[i] = graph.insertVertex(v1, null, i, x_pos, y_pos, 0.8, 0.8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].pinType = 'Output'
    pins[i].ParentComponent = v1
    pins[i].PinNumber = i
  }

  ports = component.initial_control_ports;
  for (let i = 0; i < ports; i++) {
    pinOrientation = 'ControlPort';

    x_pos = (i + 1) / (ports + 1);
    y_pos = 0;

    pins[i] = graph.insertVertex(v1, null, i, x_pos, y_pos, 0.8, 0.8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].pinType = 'Input'
    pins[i].ParentComponent = v1
    pins[i].PinNumber = i
  }

  ports = component.initial_command_ports;
  for (let i = 0; i < ports; i++) {
    pinOrientation = 'CommandPort';

    x_pos = (i + 1) / (ports + 1);
    y_pos = 1;

    pins[i] = graph.insertVertex(v1, null, i, x_pos, y_pos, 0.8, 0.8, pinOrientation)
    pins[i].geometry.relative = true;
    pins[i].pinType = 'Output'
    pins[i].ParentComponent = v1
    pins[i].PinNumber = i
  }
}
