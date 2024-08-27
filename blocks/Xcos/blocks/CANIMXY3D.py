from common.AAAAAA import *

def CANIMXY3D(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CANIMXY3D'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'canimxy3d', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 11, parameters)
    para = []
    for item in parameters:
        if item and item != '[]':
            para.extend(item.split())
        else:
            para.append(item)

    addScilabDNode(outnode, AS_REAL_PARAM, width=8, realParts=[
                   format_real_number(para[20]),
                   format_real_number(para[21]),
                   format_real_number(para[22]),
                   format_real_number(para[23]),
                   format_real_number(para[24]),
                   format_real_number(para[25]),
                   format_real_number(para[26]),
                   format_real_number(para[27])
                   ])
    param = ["-1", "8", "2", "1", "2", "3", "4", "5", "6", "7",
             "13", "1", "1", "1", "1", "1", "1", "1", "1", "8",
             "-1", "-1", "-1", "-1", "1"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 25, param)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CANIMXY3D(cell):
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
