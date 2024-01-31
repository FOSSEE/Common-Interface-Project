from common.AAAAAA import *

def ESELECT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ESELECT_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'eselect', 'ESELECT',
                         func_name, BLOCKTYPE_L,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_ESELECT_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = 0 if float(parameters[1]) == 0.0 else 1
    eov = ''
    iov = ''
    com = int(float(parameters[0]))

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
