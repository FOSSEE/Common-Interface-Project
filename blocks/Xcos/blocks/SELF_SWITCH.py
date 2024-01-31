from common.AAAAAA import *

def SELF_SWITCH(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SELF_SWITCH'
    if parameters[0] == 'on':
        style = func_name + '_ON'
    else:
        style = func_name + '_OFF'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_SELF_SWITCH(cell):
    style = cell.attrib['style']
    if style == 'SELF_SWITCH_ON':
        value = 'on'
    else:
        value = 'off'

    parameters = [value]

    style = cell.attrib.get('style')
    display_parameter = 'on' if style == 'SELF_SWITCH_ON' else 'off'

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
