from common.AAAAAA import *

def Modulo_Count(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Modulo_Count'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'modulo_count', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_Modulo_Count(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[1]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
