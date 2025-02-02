from blocks.CONST_m import CONST_m
from blocks.IFTHEL_f import IFTHEL_f
from blocks.LOGICAL_OP import LOGICAL_OP
from blocks.SAMPHOLD_m import SAMPHOLD_m
from blocks.SPLIT_f import SPLIT_f
from blocks.IN_f import IN_f
from blocks.OUT_f import OUT_f
from common.AAAAAA import *


def DLATCH(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'DLATCH'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(12, 20, 9)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H,
                         dependsOnU='1')

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

    array = ['int8(0)']
    CONST_m(root, block_id[2], ordering, geometry, array)
    addExplicitOutputPort(root, port_id[0], block_id[2], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    array = ['0', '1']
    IFTHEL_f(root, block_id[3], ordering, geometry, array)
    addExplicitInputPort(root, port_id[1], block_id[3], "1", "0.0")
    addCommandPort(root, port_id[2], block_id[3], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[3], block_id[3], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    array = ['2', '1', '5', '0']
    LOGICAL_OP(root, block_id[4], ordering, geometry, array)
    addExplicitInputPort(root, port_id[4], block_id[4], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[5], block_id[4], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[6], block_id[4], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    array = ['5']
    SAMPHOLD_m(root, block_id[5], ordering, geometry, array)
    addExplicitInputPort(root, port_id[7], block_id[5], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[8], block_id[5], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addControlPort(root, port_id[9], block_id[5], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    array = ['1', '5', '5', '0']
    LOGICAL_OP(root, block_id[6], ordering, geometry, array)
    addExplicitInputPort(root, port_id[10], block_id[6], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[11], block_id[6], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    SPLIT_f(root, block_id[7], ordering, geometry, ['0'])
    addExplicitInputPort(root, port_id[12], block_id[7], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[13], block_id[7], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[14], block_id[7], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[15], block_id[7], "3", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    IN_f(root, block_id[8], ordering, geometry, ['2'])
    addExplicitOutputPort(root, port_id[16], block_id[8], "1", "0.0")

    IN_f(root, block_id[9], ordering, geometry, ['2'])
    addExplicitOutputPort(root, port_id[17], block_id[9], "1", "0.0")

    array = ['2']
    OUT_f(root, block_id[10], ordering, geometry, array)
    addExplicitInputPort(root, port_id[18], block_id[10], "1", "0.0")

    array = ['1']
    OUT_f(root, block_id[11], ordering, geometry, array)
    addExplicitInputPort(root, port_id[19], block_id[11], "1", "0.0")

    CCLink = addExplicitLink(root, link_id[0], block_id[1], port_id[14], port_id[19])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[1], block_id[1], port_id[11], port_id[18])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[2], block_id[1], port_id[17], port_id[4])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[3], block_id[1], port_id[16], port_id[1])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[4], block_id[1], port_id[13], port_id[10])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[5], block_id[1], port_id[8], port_id[12])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[6], block_id[1], port_id[0], port_id[5])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[7], block_id[1], port_id[2], port_id[9])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[8], block_id[1], port_id[6], port_id[7])
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


def get_from_DLATCH(cell):
    (parameters, display_parameter, eiv, iiv, con, eov, iov, com) = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
