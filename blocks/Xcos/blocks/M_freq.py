from common.AAAAAA import *

def M_freq(outroot, attribid, ordering, geometry, parameters):
    func_name = 'M_freq'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'm_frequ', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_M_freq(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''
    inputs = parameters[0].split(';')

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = (len(inputs)**2)-1

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
