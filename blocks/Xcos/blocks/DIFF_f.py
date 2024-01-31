from common.AAAAAA import *

def DIFF_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DIFF_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'diffblk', 'OLDBLOCKS',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_DIFF_f(cell):
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
