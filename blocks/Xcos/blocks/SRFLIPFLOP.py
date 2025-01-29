from blocks.LOGIC import LOGIC
from blocks.DOLLAR_m import DOLLAR_m
from blocks.SPLIT_f import SPLIT_f
from blocks.OUT_f import OUT_f
from blocks.IN_f import IN_f
from common.AAAAAA import *


def SRFLIPFLOP(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'SRFLIPFLOP'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(9, 15, 7)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
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

    LOGIC(root, block_id[2], ordering, geometry, ['[0 1;1 0;1 0;1 0;0 1;0 1;0 0;0 0]', '1'])
    addExplicitInputPort(root, port_id[0], block_id[2], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[1], block_id[2], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[2], block_id[2], "3", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[3], block_id[2], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[4], block_id[2], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    DOLLAR_m(root, block_id[3], ordering, geometry, [parameters[0], '1'])
    addExplicitInputPort(root, port_id[5], block_id[3], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[6], block_id[3], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    SPLIT_f(root, block_id[4], ordering, geometry, ['0'])
    addExplicitInputPort(root, port_id[7], block_id[4], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[8], block_id[4], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[9], block_id[4], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[10], block_id[4], "3", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    array = ['2']
    OUT_f(root, block_id[5], ordering, geometry, array)
    addExplicitInputPort(root, port_id[11], block_id[5], "1", "0.0")

    array = ['1']
    IN_f(root, block_id[6], ordering, geometry, array)
    addExplicitOutputPort(root, port_id[12], block_id[6], "1", "0.0")

    array = ['2']
    IN_f(root, block_id[7], ordering, geometry, array)
    addExplicitOutputPort(root, port_id[13], block_id[7], "1", "0.0")

    array = ['1']
    OUT_f(root, block_id[8], ordering, geometry, array)
    addExplicitInputPort(root, port_id[14], block_id[8], "1", "0.0")

    CCLink = addExplicitLink(root, link_id[0], block_id[1], port_id[9], port_id[14])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[1], block_id[1], port_id[13], port_id[2])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[2], block_id[1], port_id[12], port_id[1])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[3], block_id[1], port_id[4], port_id[11])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[4], block_id[1], port_id[8], port_id[5])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[5], block_id[1], port_id[6], port_id[0])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[6], block_id[1], port_id[3], port_id[7])
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


def get_from_SRFLIPFLOP(cell):
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
