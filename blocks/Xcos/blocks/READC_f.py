from common.AAAAAA import *

def READC_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'READC_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'readc', 'TYPE_2',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 8, parameters)

    return outnode


def get_from_READC_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    temp = parameters[0]
    temp = temp.replace('[', '')
    temp = temp.replace(']', '')

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = 1 if len(temp) > 0 else 0

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
