from blocks.MFCLCK_f import MFCLCK_f
from blocks.CLKSOM_f import CLKSOM_f
from blocks.CLKOUT_f import CLKOUT_f
from blocks.SplitBlock import SplitBlock
from common.AAAAAA import *


def MCLOCK_f(outroot, attribid, ordering, geometry, parameters, parent=1, style=None, superblock=None):
    func_name = 'MCLOCK_f'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(8, 15, 7)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H, dependsOnU="0", dependsOnT="0")

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    # Create the SuperBlockDiagram element
    SuperBlockDiagram = addSuperNode(outnode, TYPE_SUPER,
                                     a="child",
                                     background="-1",
                                     gridEnabled="1",
                                     title="")

    addSuperBlkNode(SuperBlockDiagram, TYPE_ARRAY,
                    a="context",
                    scilabClass="String[]")

    mxGraphModel = addmxGraphModelNode(SuperBlockDiagram,
                                       TYPE_MODEL, a="model")
    root = addNode(mxGraphModel, TYPE_ROOT)
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[0])
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[1],
                  parent=block_id[0])

    MFCLCK_f(root, block_id[2], ordering, geometry, parameters, parent=block_id[1])
    addControlPort(root, port_id[0], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[1], block_id[2], "1", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[2], block_id[2], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    CLKSOM_f(root, block_id[3], ordering, geometry, parameters, parent=block_id[1])
    addControlPort(root, port_id[3], block_id[3], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addControlPort(root, port_id[4], block_id[3], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addControlPort(root, port_id[5], block_id[3], "3", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[6], block_id[3], "1", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    CLKOUT_f(root, block_id[4], ordering, geometry, ['1'], parent=block_id[1])
    addControlPort(root, port_id[7], block_id[4], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    CLKOUT_f(root, block_id[5], ordering, geometry, [parameters[1]], parent=block_id[1])
    addControlPort(root, port_id[8], block_id[5], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    SplitBlock(root, block_id[6], ordering, geometry, parameters, parent=block_id[1])
    addControlPort(root, port_id[9], block_id[6], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[10], block_id[6], "1", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[11], block_id[6], "2", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    SplitBlock(root, block_id[7], ordering, geometry, parameters, parent=block_id[1])
    addControlPort(root, port_id[12], block_id[7], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[13], block_id[7], "1", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[14], block_id[7], "2", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    CCLink = addCommandControlLink(root, link_id[0], block_id[1], port_id[2], port_id[9])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="360.7", y="193.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="360.7",
                 y="169.3")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="411.9", y="169.3")
    CCLink = addCommandControlLink(root, link_id[1], block_id[1], port_id[1], port_id[3])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="347.3", y="193.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint',
                 x="347.3", y="155.5")
    addPointNode(ArrayNode, 'mxPoint', x="461.8",
                 y="155.5")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="461.8", y="161.0")
    CCLink = addCommandControlLink(root, link_id[2], block_id[1], port_id[6], port_id[12])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="468.9", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="482.5", y="169.3")

    CCLink = addCommandControlLink(root, link_id[3], block_id[1], port_id[10], port_id[4])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="411.9", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="457.0", y="169.3")
    CCLink = addCommandControlLink(root, link_id[4], block_id[1], port_id[11], port_id[7])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="411.9", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="411.9", y="271.0")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="509.0", y="271.0")
    CCLink = addCommandControlLink(root, link_id[5], block_id[1], port_id[13], port_id[0])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="482.5", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="489.6", y="169.3")
    addPointNode(ArrayNode, 'mxPoint', x="489.6", y="338.3")
    addPointNode(ArrayNode, 'mxPoint', x="354.0", y="338.3")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="354.0", y="244.7")
    CCLink = addCommandControlLink(root, link_id[6], block_id[1], port_id[14], port_id[8])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="482.4", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="482.4", y="152.0")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="509.0", y="152.0")

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL, a='defaultParent',
                  id=block_id[1],
                  parent=block_id[0])

    return outnode


def get_from_MCLOCK_f(cell):
    (parameters, display_parameter, eiv, iiv, con, eov, iov, com) = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
