from blocks.CONST_m import CONST_m
from blocks.IFTHEL_f import IFTHEL_f
from blocks.LOGICAL_OP import LOGICAL_OP
from blocks.SAMPHOLD_m import SAMPHOLD_m
from blocks.IN_f import IN_f
from blocks.OUT_f import OUT_f
from blocks.ANDBLK import ANDBLK
from blocks.EDGE_TRIGGER import EDGE_TRIGGER
from blocks.Extract_Activation import Extract_Activation
from blocks.SUM_f import SUM_f
from blocks.SPLIT_f import SPLIT_f
from blocks.SELECT_m import SELECT_m
from common.AAAAAA import *


def DFLIPFLOP(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'DFLIPFLOP'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(22, 53, 24)
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

    array = ['1', '1']
    IFTHEL_f(root, block_id[3], ordering, geometry, array)
    addExplicitInputPort(root, port_id[1], block_id[3], "1", "0.0")
    addControlPort(root, port_id[2], block_id[3], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[3], block_id[3], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[4], block_id[3], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    array = ['2', '1', '5', '0']
    LOGICAL_OP(root, block_id[4], ordering, geometry, array)
    addExplicitInputPort(root, port_id[5], block_id[4], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[6], block_id[4], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[7], block_id[4], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    array = ['5']
    SAMPHOLD_m(root, block_id[5], ordering, geometry, array)
    addExplicitInputPort(root, port_id[8], block_id[5], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[9], block_id[5], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addControlPort(root, port_id[10], block_id[5], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    array = ['1', '5', '5', '0']
    LOGICAL_OP(root, block_id[6], ordering, geometry, array)
    addExplicitInputPort(root, port_id[11], block_id[6], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[12], block_id[6], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    array = ['3']
    IN_f(root, block_id[7], ordering, geometry, array)
    addExplicitOutputPort(root, port_id[13], block_id[7], "1", "0.0")

    array = ['1']
    IN_f(root, block_id[8], ordering, geometry, array)
    addExplicitOutputPort(root, port_id[14], block_id[8], "1", "0.0")

    array = ['2']
    OUT_f(root, block_id[9], ordering, geometry, array)
    addExplicitInputPort(root, port_id[15], block_id[9], "1", "0.0")

    array = ['1']
    OUT_f(root, block_id[10], ordering, geometry, array)
    addExplicitInputPort(root, port_id[16], block_id[10], "1", "0.0")

    ANDBLK(root, block_id[11], ordering, geometry, ['0'])
    addControlPort(root, port_id[17], block_id[11], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addControlPort(root, port_id[18], block_id[11], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[19], block_id[11], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    EDGE_TRIGGER(root, block_id[12], ordering, geometry, ['0'])
    addExplicitInputPort(root, port_id[20], block_id[12], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[21], block_id[12], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    IN_f(root, block_id[13], ordering, geometry, ['2'])
    addExplicitOutputPort(root, port_id[22], block_id[13], "1", "0.0")

    Extract_Activation(root, block_id[14], ordering, geometry, ['2'])
    addExplicitInputPort(root, port_id[23], block_id[14], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addCommandPort(root, port_id[24], block_id[14], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    SUM_f(root, block_id[15], ordering, geometry, ['2'])
    addExplicitInputPort(root, port_id[25], block_id[15], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[26], block_id[15], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[27], block_id[15], "3", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[28], block_id[15], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    SPLIT_f(root, block_id[16], ordering, geometry, ['0'])
    addExplicitInputPort(root, port_id[29], block_id[16], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[30], block_id[16], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[31], block_id[16], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[32], block_id[16], "3", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    SPLIT_f(root, block_id[17], ordering, geometry, ['0'])
    addExplicitInputPort(root, port_id[33], block_id[17], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[34], block_id[17], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[35], block_id[17], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[36], block_id[17], "3", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    array = ['5', '2', '1']
    SELECT_m(root, block_id[18], ordering, geometry, array)
    addExplicitInputPort(root, port_id[37], block_id[18], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[38], block_id[18], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[39], block_id[18], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addControlPort(root, port_id[40], block_id[18], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addControlPort(root, port_id[41], block_id[18], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    SPLIT_f(root, block_id[19], ordering, geometry, ['0'])
    addExplicitInputPort(root, port_id[42], block_id[19], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[43], block_id[19], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[44], block_id[19], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[45], block_id[19], "3", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    SPLIT_f(root, block_id[20], ordering, geometry, ['0'])
    addExplicitInputPort(root, port_id[46], block_id[20], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[47], block_id[20], "1", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[48], block_id[20], "2", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[49], block_id[20], "3", "0.0", dataType="INT8_MATRIX", dataColumns="1", dataLines="1")

    SPLIT_f(root, block_id[21], ordering, geometry, ['0'])
    addControlPort(root, port_id[50], block_id[21], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[51], block_id[21], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[52], block_id[21], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    CCLink = addCommandControlLink(root, link_id[0], block_id[1], port_id[4], port_id[40])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[1], block_id[1], port_id[51], port_id[39])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[2], block_id[1], port_id[50], port_id[10])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[3], block_id[1], port_id[47], port_id[37])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[4], block_id[1], port_id[46], port_id[6])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[5], block_id[1], port_id[43], port_id[16])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[6], block_id[1], port_id[42], port_id[11])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[7], block_id[1], port_id[38], port_id[41])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[8], block_id[1], port_id[9], port_id[36])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[9], block_id[1], port_id[28], port_id[23])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[10], block_id[1], port_id[35], port_id[27])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[11], block_id[1], port_id[34], port_id[1])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[12], block_id[1], port_id[31], port_id[25])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[13], block_id[1], port_id[30], port_id[20])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[14], block_id[1], port_id[22], port_id[29])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[15], block_id[1], port_id[24], port_id[2])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[16], block_id[1], port_id[21], port_id[17])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[17], block_id[1], port_id[19], port_id[49])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addCommandControlLink(root, link_id[18], block_id[1], port_id[3], port_id[18])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[19], block_id[1], port_id[12], port_id[15])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[20], block_id[1], port_id[14], port_id[5])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[21], block_id[1], port_id[13], port_id[33])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[22], block_id[1], port_id[0], port_id[45])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addExplicitLink(root, link_id[23], block_id[1], port_id[7], port_id[8])
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


def get_from_DFLIPFLOP(cell):
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
