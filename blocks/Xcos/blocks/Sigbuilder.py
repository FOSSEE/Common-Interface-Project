from blocks.CURVE_c import CURVE_c
from blocks.SplitBlock import SplitBlock
from blocks.OUT_f import OUT_f
from blocks.CLKOUTV_f import CLKOUTV_f
from common.AAAAAA import *


def Sigbuilder(outroot, attribid, ordering, geometry, parameters, parent=1, style=None, superblock=None):
    func_name = 'Sigbuilder'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(6, 8, 4)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H, dependsOnU="0", dependsOnT="0")

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
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

    CURVE_c(root, block_id[2], ordering, geometry, parameters, parent=block_id[1])
    addExplicitOutputPort(root, port_id[0], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addControlPort(root, port_id[1], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[2], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    SplitBlock(root, block_id[3], ordering, geometry, parameters, parent=block_id[1])
    addControlPort(root, port_id[3], block_id[3], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[4], block_id[3], "1", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[5], block_id[3], "2", "-1.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    param = ['1']
    OUT_f(root, block_id[4], ordering, geometry, param, parent=block_id[1])
    addExplicitInputPort(root, port_id[6], block_id[4], "1", "0.0")

    p = ['1']
    CLKOUTV_f(root, block_id[5], ordering, geometry, p, parent=block_id[1])
    addControlPort(root, port_id[7], block_id[5], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    CCLink = addCommandControlLink(root, link_id[0], block_id[1], port_id[2], port_id[3], value="drawlink")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="349.63473", y="600.47089")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="349.49528", y="565.10704")
    CCLink = addCommandControlLink(root, link_id[1], block_id[1], port_id[5], port_id[1], value="drawlink")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="349.49528", y="565.10704")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint',
                 x="266.69602", y="565.10704")
    addPointNode(ArrayNode, 'mxPoint', x="266.69602",
                 y="680.99483")
    addPointNode(ArrayNode, 'mxPoint',
                 x="270.35525", y="680.99483")
    addPointNode(ArrayNode, 'mxPoint', x="342.80795",
                 y="680.99483")
    addPointNode(ArrayNode, 'mxPoint',
                 x="342.80795", y="651.89946")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="349.63473", y="651.89946")

    CCLink = addExplicitLink(root, link_id[2], block_id[1], port_id[0], port_id[6], value="drawlink")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="378.20616", y="626.18517")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="398.20616", y="626.18517")

    CCLink = addCommandControlLink(root, link_id[3], block_id[1], port_id[4], port_id[7], value="drawlink")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="349.49528", y="565.10704")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="349.49528", y="535.10704")

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL, a='defaultParent',
                  id=block_id[1],
                  parent=block_id[0])

    return outnode


def get_from_Sigbuilder(cell):
    (parameters, display_parameter, eiv, iiv, con, eov, iov, com) = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
