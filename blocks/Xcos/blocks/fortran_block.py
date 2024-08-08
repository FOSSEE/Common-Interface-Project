from common.AAAAAA import *

def fortran_block(outroot, attribid, ordering, geometry, parameters):
    func_name = 'fortran_block'

    code = parameters[3]
    codeLines = code.split('\n')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, parameters[3], 'DYNAMIC_FORTRAN_1',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsArrayNode(outnode, TYPE_STRING, 4, parameters, codeLines, TYPE_ARRAY, func_name)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    param = ['0']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, param)
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


def get_from_fortran_block(cell):
    parameters = getParametersFromExprsNode(cell)

    display_parameter = parameters[3]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
