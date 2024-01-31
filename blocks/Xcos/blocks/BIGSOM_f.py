from common.AAAAAA import *

def BIGSOM_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BIGSOM_f'

    outnode = addOutNode(outroot, BLOCK_BIGSOM,
                         attribid, ordering, 1,
                         func_name, 'sum', 'TYPE_2',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1',
                         value='+')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_BIGSOM_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''
    inputs = parameters[0].split(';')

    eiv = len(inputs)
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
