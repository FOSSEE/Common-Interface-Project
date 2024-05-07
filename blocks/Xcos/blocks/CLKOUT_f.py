from common.AAAAAA import *

def CLKOUT_f(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'CLKOUT_f'

    outnode = addOutNode(outroot, BLOCK_EVENT_OUT,
                         attribid, ordering, parent,
                         func_name, 'output', 'DEFAULT',
                         func_name, BLOCKTYPE_D, dependsOnU='0',
                         dependsOnT='0')

    input_list = parameters
    output_list = [str(int(float(num)) + 1) for num in input_list]

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    array = ['1']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, array)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    arr = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, arr)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, arr)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CLKOUT_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
