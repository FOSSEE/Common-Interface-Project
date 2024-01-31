from common.AAAAAA import *

def RFILE_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RFILE_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'readf', 'DEFAULT',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 5, parameters)

    return outnode


def get_from_RFILE_f(cell):
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
