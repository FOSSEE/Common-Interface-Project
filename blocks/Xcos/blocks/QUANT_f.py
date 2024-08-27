from common.AAAAAA import *

def QUANT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'QUANT_f'

    data_type = ['', 'qzrnd', 'qztrn', 'qzflr', 'qzcel']

    simulation_func_name = data_type[int(parameters[1])]

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, simulation_func_name, 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=1, realParts=[
                   format_real_number(parameters[0])])
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, parameters[1])
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


def get_from_QUANT_f(cell):
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
