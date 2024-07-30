from common.AAAAAA import *

def CBLOCK4(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CBLOCK4'

    if parameters[1] == 'y':
        type = 'IMPLICIT'
    else:
        type = 'EXPLICIT'

    simulation_func_type = 'DYNAMIC_' + type + '_4'

    if parameters[17] == 'y':
        depends_u = '1'
    else:
        depends_u = '0'

    if parameters[18] == 'y':
        depends_t = '1'
    else:
        depends_t = '0'

    code = parameters[19]
    codeLines = code.split('\n')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, parameters[0], simulation_func_type,
                         func_name, BLOCKTYPE_C,
                         dependsOnU=depends_u,
                         dependsOnT=depends_t)

    addExprsArrayNode(outnode, TYPE_STRING, 19, parameters, codeLines)
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


def get_from_CBLOCK4(cell):
    parameters = getParametersFromExprsNode(cell)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = 1 if parameters[6] != '[]' and int(float(parameters[6])) == 1 else 0
    eov = ''
    iov = ''
    com = 1 if parameters[7] != '[]' and int(float(parameters[7])) == 1 else 0

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
