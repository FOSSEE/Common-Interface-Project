from common.AAAAAA import *

# block_id = ['-64ce6d85:145ef6f2b50:-7ee7', '-64ce6d85:145ef6f2b51:-7ee7',
#             '-64ce6d85:145ef6f2b4f:-7f54']


def CLKOUTV_f(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'CLKOUTV_f'
    block_id, port_id, link_id = generate_id(3, 0, 0)
    outnode = addOutNode(outroot, BLOCK_EVENT_OUT,
                         attribid, ordering, parent,
                         func_name, 'output', 'DEFAULT',
                         func_name, BLOCKTYPE_D, dependsOnU="0", dependsOnT="0")

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, array)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_CLKOUTV_f(cell):
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
