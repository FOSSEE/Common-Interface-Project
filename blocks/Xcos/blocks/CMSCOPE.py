from common.AAAAAA import *

def CMSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CMSCOPE'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'cmscope', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1',
                         value=parameters[10])

    addExprsNode(outnode, TYPE_STRING, 11, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 7, realParts=[0.0, 10.0, 10.0, 0.0, 2.0, 0.0, 2.0])
    array = ['-1', '2', '20', '-1', '-1', '-1', '-1', '1', '1', '1', '3', '0']
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
