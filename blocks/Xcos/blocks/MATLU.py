from common.AAAAAA import *

def MATLU(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATLU'

    data_type = ['', 'mat_lu', 'matz_lu']

    simulation_func_name = data_type[int(parameters[0])]

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_MATLU(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)