from blocks.END_c import END_c
from common.AAAAAA import *

# block_id = ['-76454188:14e1ef4db89:-7d58', '-76454188:14e1ef4db8a:-7d58',
#             '-76454188:14e1ef4db88:-7d55']


def ENDBLK(outroot, attribid, ordering, geometry, parameters, parent=1, style=None, superblock=None):
    func_name = 'ENDBLK'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(3, 2, 1)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE)
    # Create the outer Array node for equations
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

    END_c(root, block_id[2], ordering, geometry, parameters)
    addControlPort(root, port_id[0], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[1], block_id[2], "1", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    CCLink = addCommandControlLink(root, link_id[0], block_id[2], port_id[0], port_id[1])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="20.0", y="44.0")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint',
                 x="220.0", y="254.66666000000004")
    addPointNode(ArrayNode, 'mxPoint', x="189.73333000000002",
                 y="254.66666000000004")
    addPointNode(ArrayNode, 'mxPoint', x="189.73333000000002",
                 y="183.53333000000003")
    addPointNode(ArrayNode, 'mxPoint', x="220.0",
                 y="183.53333000000003")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL, a='defaultParent',
                  id=block_id[1],
                  parent=block_id[0])

    return outnode


def get_from_ENDBLK(cell):
    (parameters, display_parameter, eiv, iiv, con, eov, iov, com) = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
