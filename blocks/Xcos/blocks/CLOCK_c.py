from blocks.CLKOUT_f import CLKOUT_f
from blocks.EVTDLY_c import EVTDLY_c
from blocks.SplitBlock import SplitBlock
from common.AAAAAA import *


def CLOCK_c(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'CLOCK_c'
    block_id, port_id, link_id = generate_id(9, 12, 7)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H, dependsOnU='0',
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

    # Create the EventOutBlock node inside the root tag
    CLKOUT_f(root, block_id[2], ordering, geometry, parameters, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    EVTDLY_c(root, block_id[3], ordering, geometry, parameters, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[1],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")
    addPort(root, TYPE_CMD, id=port_id[2],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.1",
            style="CommandPort", value="")

    SplitBlock(root, block_id[4], ordering, geometry, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[3],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")
    addPort(root, TYPE_CMD, id=port_id[4],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="-1.0",
            style="CommandPort", value="")
    addPort(root, TYPE_CMD, id=port_id[5],
            parent=block_id[4], ordering="2",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="-1.0",
            style="CommandPort", value="")

    CCLink = addLink(root, TYPE_LINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[5],
                     target=port_id[1],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint',
                 x="100.70999999999998", y="40.0")
    addPointNode(ArrayNode, 'mxPoint', x="60.0",
                 y="40.0")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")
    CCLink = addLink(root, TYPE_LINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[4],
                     target=port_id[0],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="0.0", y="11.0")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="10.0", y="-4.0")
    CCLink = addLink(root, TYPE_LINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[2],
                     target=port_id[3],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="20.0", y="44.0")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="60.0", y="170.0")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="0.0", y="-4.0")

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL, a='defaultParent',
                  id=block_id[1],
                  parent=block_id[0])

    return outnode


def get_from_CLOCK_c(cell):
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
