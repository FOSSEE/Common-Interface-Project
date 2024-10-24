from common.AAAAAA import *


def CONVERT(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'CONVERT'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'convert', 'C_OR_FORTRAN',
                         style, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    array = ['4']
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


def get_from_CONVERT(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    types = ['decim.', 'decim.', 'int32', 'int16',
             'int8', 'uint32', 'uint16', 'uint8']
    input_t = int(float(parameters[0]))
    output_t = int(float(parameters[1]))

    input_type = types[input_t - 1]
    output_type = types[output_t - 1]

    display_parameter = input_type + ',' + output_type

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
