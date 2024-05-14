from common.AAAAAA import *

def OUT_f(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'OUT_f'

    outnode = addOutNode(outroot, BLOCK_EXPLICIT_OUT,
                         attribid, ordering, parent,
                         func_name, 'output', 'DEFAULT',
                         func_name, BLOCKTYPE_C, dependsOnU='0',
                         dependsOnT='0')

    addExprsNode(outnode, TYPE_STRING, 1, parameters[1])
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    array = ['1']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, array)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, arr)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_OUT_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
