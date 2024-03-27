from common.AAAAAA import *

def TEXT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TEXT_f'

    outnode = addOutNode(outroot, BLOCK_TEXT,
                         attribid, ordering, 1,
                         func_name, None, None,
                         func_name, None,
                         value=parameters[0])

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_TEXT_f(cell):
    parameters = [cell.attrib['value']]

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
