from common.AAAAAA import *

def MATMUL(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATMUL'

    data_type = ['', 'matmul_m', 'matzmul_m',
                 'matmul_i32', 'matmul_i16', 'matmul_i8',
                 'matmul_ui32', 'matmul_ui16', 'matmul_ui8']
    overflow = ['n', 's', 'e']

    para1 = int(float(parameters[0]))
    para2 = int(float(parameters[1]))
    para3 = int(float(parameters[2]))

    if para2 == 1:
        if para1 == 1 or para1 == 2:
            simulation_func_name = data_type[para1]
        else:
            simulation_func_name = data_type[para1] + overflow[para3]
    elif para2 == 2:
        if para3 == 2:
            if para1 != 2:
                simulation_func_name = 'matmul2_m'
            else:
                simulation_func_name = 'mutmul2_e'
        elif para3 == 1:
            simulation_func_name = 'matmul2_s'
        else:
            simulation_func_name = 'matmul2_m'
    elif para2 == 3:
        if para1 != 2:
            if para3 == 1 or para3 == 2:
                simulation_func_name = 'matbyscal_' + overflow[para3]
            else:
                simulation_func_name = ''
        else:
            simulation_func_name = 'matbyscal'
    else:
        simulation_func_name = ''

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 2, realParts=[0.0, 0.0])
    array = ['1']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, array)
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


def get_from_MATMUL(cell):
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
