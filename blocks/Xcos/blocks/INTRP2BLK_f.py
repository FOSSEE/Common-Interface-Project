from common.AAAAAA import *

def INTRP2BLK_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'INTRP2BLK_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'intrp2', 'TYPE_1',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    def extract_elements(item):
        stripped_item = item[1:-1]
        split_item = stripped_item.split(';')
        return split_item[:2]

    result = [extract_elements(item) for item in parameters]

    def split_values(values):
        split_result = []
        for value in values:
            split_result.extend(value.split(','))
        return split_result

    flattened_and_split = [split_value for sublist in result for split_value in split_values(sublist)]
    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    param = flattened_and_split
    addScilabDNode(outnode, AS_REAL_PARAM, width=8, realParts=[
                   format_real_number(param[0]),
                   format_real_number(param[1]),
                   format_real_number(param[2]),
                   format_real_number(param[3]),
                   format_real_number(param[4]),
                   format_real_number(param[5]),
                   format_real_number(param[6]),
                   format_real_number(param[7])
                   ])
    array = ['2', '2']
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 2, array)
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


def get_from_INTRP2BLK_f(cell):
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
