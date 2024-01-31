from common.AAAAAA import *

def CURV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CURV_f'
    para = parameters[0].split(' ')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'intplt', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    node = addNode(outnode, TYPE_STRING, height=1, width=len(para))

    for i in range(len(para)):

        addData(node, i, 0, para[i])

    return outnode


def get_from_CURV_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
