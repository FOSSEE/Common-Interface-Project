from common.AAAAAA import *


def TEXT_f(outroot, attribid, ordering, geometry, parameters, parent=1, style=None, superblock=None):
    func_name = 'TEXT_f'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_TEXT,
                         attribid, ordering, parent,
                         func_name, None, None,
                         style, None,
                         value=parameters[0])

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_TEXT_f(cell):
    parameters = cell.get('parameters', [])
    display_parameter = parameters[0] if parameters else ""

    # Assuming TEXT_f has no input/output ports
    eiv, iiv, con, eov, iov, com = 0, "", 0, "", "", ""

    ports = [eiv, iiv, con, eov, iov, com]

    return parameters, display_parameter, ports
