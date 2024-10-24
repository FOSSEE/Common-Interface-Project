from common.AAAAAA import *


def CMSCOPE(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'CMSCOPE'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'cmscope', 'C_OR_FORTRAN',
                         style, BLOCKTYPE_C,
                         dependsOnU='1', dependsOnT='0'
                         )

    addExprsNode(outnode, TYPE_STRING, 11, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 7, realParts=[0.0, 0.25, 0.25, -15.0, 15.0, -15.0, 15.0])
    array = ['-1', '2', '2', '-1', '-1', '-1', '-1', '1', '1', '1', '3', '0']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 12, array)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CMSCOPE(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''
    input = parameters[0].split(' ')

    eiv = len(input)
    iiv = ''
    con = 1 if int(float(parameters[9])) == 0 else 0
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
