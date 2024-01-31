from common.AAAAAA import *

def SWITCH_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SWITCH_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'switchn', 'TYPE_2',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1',
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_SWITCH_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[1]

    eiv = int(float(parameters[0]))
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
