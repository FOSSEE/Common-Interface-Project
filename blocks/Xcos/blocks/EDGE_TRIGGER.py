from blocks.CLKOUTV_f import CLKOUTV_f
from blocks.IN_f import IN_f
from blocks.IFTHEL_f import IFTHEL_f
from blocks.EDGETRIGGER import EDGETRIGGER
from common.AAAAAA import *

block_id = ['3dd766ce:16069f39bc0:-7d61', '3dd766ce:16069f39bc1:-7d61',
            '3dd766ce:16069f39bbf:-7d34', '3dd766ce:16069f39bbf:-7d31',
            '3dd766ce:16069f39bbf:-7d2d', '3dd766ce:16069f39bbf:-7d2b']


def EDGE_TRIGGER(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EDGE_TRIGGER'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
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

    # Create the SuperBlockDiagram element
    SuperBlockDiagram = addSuperNode(outnode, TYPE_SUPER,
                                     a="child",
                                     background="-1",
                                     gridEnabled="1",
                                     title="")

    Array = addSuperBlkNode(SuperBlockDiagram, TYPE_ARRAY,
                            a="context",
                            scilabClass="String[]")
    superAddNode(Array, TYPE_ADD, value="")
    mxGraphModel = addmxGraphModelNode(SuperBlockDiagram,
                                       TYPE_MODEL, a="model")
    root = addNode(mxGraphModel, TYPE_ROOT)
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[0])
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[1],
                  parent=block_id[0])

    EDGETRIGGER(root, block_id[2], ordering, geometry, parameters)

    IFTHEL_f(root, block_id[3], ordering, geometry, parameters)

    IN_f(root, block_id[4], ordering, geometry, parameters)

    CLKOUTV_f(root, block_id[5], ordering, geometry, parameters)

    return outnode


def get_from_EDGE_TRIGGER(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
