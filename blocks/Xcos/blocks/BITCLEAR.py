from common.AAAAAA import *

def BITCLEAR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BITCLEAR'

    datatype = ['', '', '', '32', '16', '8', '32', '16', '8']
    para1 = int(float(parameters[0]))

    simulation_func_name = 'bit_clear_' + datatype[para1]

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_BITCLEAR(cell):
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
