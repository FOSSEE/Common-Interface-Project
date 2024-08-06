from common.AAAAAA import *

def INTRPLBLK_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INTRPLBLK_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'intrpl', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    def extract_values(item):
        stripped_item = item[1:-1]
        split_item = stripped_item.split(';')
        return split_item

    flattened_and_split = [value for item in parameters for value in extract_values(item)]
    param = flattened_and_split

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=4, realParts=[
                   format_real_number(param[0]),
                   format_real_number(param[1]),
                   format_real_number(param[2]),
                   format_real_number(param[3])
                   ])
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


def get_from_INTRPLBLK_f(cell):
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
