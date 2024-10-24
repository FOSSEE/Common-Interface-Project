from common.AAAAAA import *


def CBLOCK(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'CBLOCK'
    if style is None:
        style = func_name

    if parameters[1] == 'y':
        type = 'IMPLICIT'
    else:
        type = 'EXPLICIT'

    simulation_func_type = 'DYNAMIC_' + type + '_4'

    if parameters[11] == 'y':
        depends_u = '1'
    else:
        depends_u = '0'

    if parameters[12] == 'y':
        depends_t = '1'
    else:
        depends_t = '0'

    code = parameters[13]
    codeLines = code.split('\n')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, parameters[0], simulation_func_type,
                         style, BLOCKTYPE_C,
                         dependsOnU=depends_u,
                         dependsOnT=depends_t)

    addExprsArrayNode(outnode, TYPE_STRING, 14, parameters, codeLines, TYPE_DOUBLE, func_name)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
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


def get_from_CBLOCK(cell):
    parameters = getParametersFromExprsNode(cell)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = 1 if parameters[4] != '[]' and int(float(parameters[4])) == 1 else 0
    eov = ''
    iov = ''
    com = 1 if parameters[5] != '[]' and int(float(parameters[5])) == 1 else 0

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
