from common.AAAAAA import *


def LOGICAL_OP(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'LOGICAL_OP'

    d_type = ['', '', '', 'i32', 'i16', 'i8', 'ui32', 'ui16', 'ui8']

    para3 = int(float(parameters[2]))

    if para3 != 1:
        datatype = '_' + d_type[para3]
    else:
        datatype = ''

    simulation_func_name = 'logicalop' + datatype

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, simulation_func_name, 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 4, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    array = ['4']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, array)
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


def get_from_LOGICAL_OP(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    logical_operators = ['AND', 'OR', 'NAND', 'NOR', 'XOR', 'NOT']
    display_parameter = logical_operators[int(float(parameters[1]))]

    eiv = int(float(parameters[0]))
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
