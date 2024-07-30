from common.AAAAAA import *

def c_block(outroot, attribid, ordering, geometry, parameters):
    func_name = 'c_block'

    code = parameters[4]
    codeLines = code.split('\n')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, parameters[3], 'DYNAMIC_C_1',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsArrayNode(outnode, TYPE_STRING, 4, parameters, codeLines)
    addScilabDNode(outnode, AS_REAL_PARAM, width=1, realParts=[
                   format_real_number(parameters[3])
                   ])
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 7, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['1']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addScilabDNode(outnode, AS_STATE, width=2, realParts=[
                   format_real_number(parameters[1]),
                   format_real_number(parameters[2])])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_c_block(cell):
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
