from common.AAAAAA import *


def SUMMATION(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'SUMMATION'

    data_type = ['', '', '_z', '_i32', '_i16', '_i8', '_ui32', '_ui16', '_ui8']
    overflow = ['n', 's', 'e']

    para1 = int(float(parameters[0]))
    para3 = int(float(parameters[2]))

    if para1 == 1 or para1 == 2:
        simulation_func_name = 'summation' + data_type[para1]
    else:
        simulation_func_name = 'summation' + data_type[para1] + overflow[para3]

    outnode = addOutNode(outroot, BLOCK_SUMMATION,
                         attribid, ordering, parent,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    if len(parameters) == 1:
        new_parameters = [1, parameters[0], 0]
    else:
        new_parameters = parameters
    addExprsNode(outnode, TYPE_STRING, 3, new_parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 0, [])
    array = ['1', '-1']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 2, array)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_SUMMATION(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''
    inputs = parameters[1].split(';')

    eiv = len(inputs)
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
