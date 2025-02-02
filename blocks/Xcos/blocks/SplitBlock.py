from common.AAAAAA import *


def SplitBlock(outroot, attribid, ordering, geometry, parameters, parent=1, style=None, func_name='CLKSPLIT_f'):
    if style is None:
        style = func_name

    if func_name == 'CLKSPLIT_f':
        simulationFunctionName = 'split'
        blockType = BLOCKTYPE_D
    else:
        simulationFunctionName = ''
        blockType = BLOCKTYPE_C

    outnode = addOutNode(outroot, BLOCK_SPLIT,
                         attribid, ordering, parent,
                         func_name, simulationFunctionName, 'DEFAULT',
                         style, blockType, dependsOnU='0',
                         dependsOnT='0')
    addExprsNode(outnode, TYPE_DOUBLE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS, [])
    addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
            x=geometry['x'], y=geometry['y'],
            width=geometry['width'], height=geometry['height']
            )

    return outnode


def get_from_SplitBlock(cell):
    (parameters, display_parameter, eiv, iiv, con, eov, iov, com) = getParametersFromExprsNode(None)

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
