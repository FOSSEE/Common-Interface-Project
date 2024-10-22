from common.AAAAAA import *


def CMATVIEW(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'CMATVIEW'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'cmatview', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=77, realParts=[
                   "0.24", "1.0", "0.0", "0.0", "0.0", "0.0", "0.0",
                   "0.0", "0.0", "0.0", "0.0", "0.020000000000000018",
                   "0.18000000000000016", "0.3400000000000001", "0.5",
                   "0.6600000000000001", "0.8200000000000003", "0.98",
                   "1.0", "1.0", "1.0", "1.0", "1.0", "1.0",
                   "0.8999999999999999", "0.7399999999999998",
                   "0.5800000000000001", "0.0", "0.0", "0.0",
                   "0.05999999999999994", "0.21999999999999997",
                   "0.38", "0.54", "0.7000000000000002",
                   "0.8600000000000001", "1.0", "1.0", "1.0",
                   "1.0", "1.0", "1.0", "1.0", "0.8599999999999999",
                   "0.6999999999999997", "0.54", "0.3799999999999999",
                   "0.21999999999999975", "0.06000000000000005", "0.0",
                   "0.0", "0.0", "0.58", "0.74", "0.9", "1.0", "1.0",
                   "1.0", "1.0", "1.0", "1.0", "0.98",
                   "0.8199999999999998", "0.6599999999999999", "0.5",
                   "0.33999999999999986", "0.17999999999999972",
                   "0.020000000000000018", "0.0", "0.0", "0.0", "0.0",
                   "0.0", "0.0", "0.0", "0.0", "0.0"
                   ])
    para = ["0", "100", "25"]
    addPrecNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 3, para)
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


def get_from_CMATVIEW(cell):
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
