from blocks.FROMWS_c import FROMWS_c
from blocks.OUT_f import OUT_f
from common.AAAAAA import *

# block_id = ['51059305:16030bc407e:-7d4e', '51059305:16030bc407f:-7d4e',
#             '51059305:16030bc407d:-7d36', '51059305:16030bc407d:-7d32']

# port_id = ['5631d1e9:18ea7a6d774:-7ff3', '5631d1e9:18ea7a6d774:-7ff2',
#            '5631d1e9:18ea7a6d774:-7ff1', '5631d1e9:18ea7a6d774:-7fee']

# link_id = ['5631d1e9:18ea7a6d774:-7fed', '5631d1e9:18ea7a6d774:-7fec']


def FROMWSB(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'FROMWSB'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(4, 4, 2)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H)

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
    addObjNode(outnode, TYPE_ARRAY,
               CLASS_LIST, AS_EQUATIONS, parameters)
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

    FROMWS_c(root, block_id[2], ordering, geometry, parameters)
    addExplicitOutputPort(root, port_id[0], block_id[2], "1", "0.0")
    addControlPort(root, port_id[1], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[2], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    array = ['1']
    OUT_f(root, block_id[3], ordering, geometry, array)
    addExplicitInputPort(root, port_id[3], block_id[3], "1", "0.0")

    CCLink = addExplicitLink(root, link_id[0], block_id[1], port_id[0], port_id[3])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[1], block_id[1], port_id[2], port_id[1])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL,
                  id=block_id[1], a="defaultParent",
                  parent=block_id[0])

    return outnode


def get_from_FROMWSB(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
