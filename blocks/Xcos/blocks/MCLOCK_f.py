from blocks.MFCLCK_f import MFCLCK_f
from blocks.CLKSOM_f import CLKSOM_f
from blocks.CLKOUT_f import CLKOUT_f
from blocks.SplitBlock import SplitBlock
from common.AAAAAA import *

# block_id = ['-6bea78c7:19120fe12cb:-7f64', '-6bea78c7:19120fe12cc:-7f64',
#             '-6bea78c7:19120fe12ca:-7f61', '-6bea78c7:19120fe12ca:-7f5d',
#             '-6bea78c7:19120fe12ca:-7f58', '-6bea78c7:19120fe12ca:-7f56',
#             '-6bea78c7:19120fe12ca:-7f54', '-6bea78c7:19120fe12ca:-7f50']
# link_id = ['-6bea78c7:19120fe12ca:-7f4c', '-6bea78c7:19120fe12ca:-7f4b',
#            '-6bea78c7:19120fe12ca:-7f4a', '-6bea78c7:19120fe12ca:-7f49',
#            '-6bea78c7:19120fe12ca:-7f48', '-6bea78c7:19120fe12ca:-7f47',
#            '-6bea78c7:19120fe12ca:-7f46'
#            ]
# port_id = ['-6bea78c7:19120fe12ca:-7f60', '-6bea78c7:19120fe12ca:-7f5f',
#            '-6bea78c7:19120fe12ca:-7f5e', '-6bea78c7:19120fe12ca:-7f5c',
#            '-6bea78c7:19120fe12ca:-7f5b', '-6bea78c7:19120fe12ca:-7f5a',
#            '-6bea78c7:19120fe12ca:-7f59', '-6bea78c7:19120fe12ca:-7f57',
#            '-6bea78c7:19120fe12ca:-7f55', '-6bea78c7:19120fe12ca:-7f53',
#            '-6bea78c7:19120fe12ca:-7f52', '-6bea78c7:19120fe12ca:-7f51',
#            '-6bea78c7:19120fe12ca:-7f4f', '-6bea78c7:19120fe12ca:-7f4e',
#            '-6bea78c7:19120fe12ca:-7f4d'
#            ]


def MCLOCK_f(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
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

    addPort(root, TYPE_CNTRL, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[1],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[2],
            parent=block_id[2], ordering="2",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")

    CLKSOM_f(root, block_id[3], ordering, geometry, parameters, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[3],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CNTRL, id=port_id[4],
            parent=block_id[3], ordering="2",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CNTRL, id=port_id[5],
            parent=block_id[3], ordering="3",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[6],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")

    CLKOUT_f(root, block_id[4], ordering, geometry, parameters, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[7],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")

    CLKOUT_f(root, block_id[5], ordering, geometry, parameters, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[8],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")

    SplitBlock(root, block_id[6], ordering, geometry, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[9],
            parent=block_id[6], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[10],
            parent=block_id[6], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[11],
            parent=block_id[6], ordering="2",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")

    SplitBlock(root, block_id[7], ordering, geometry, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[12],
            parent=block_id[7], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[13],
            parent=block_id[7], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[14],
            parent=block_id[7], ordering="2",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")

    CCLink = addLink(root, TYPE_LINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[2],
                     target=port_id[9],
                     style="", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="360.7", y="193.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="360.7",
                 y="169.3")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="411.9", y="169.3")
    CCLink = addLink(root, TYPE_LINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[1],
                     target=port_id[3],
                     style="", value="")
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
    CCLink = addLink(root, TYPE_LINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[6],
                     target=port_id[12],
                     style="", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="468.9", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="482.5", y="169.3")

    CCLink = addLink(root, TYPE_LINK, id=link_id[3],
                     parent=block_id[1],
                     source=port_id[10],
                     target=port_id[4],
                     style="", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="411.9", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="457.0", y="169.3")
    CCLink = addLink(root, TYPE_LINK, id=link_id[4],
                     parent=block_id[1],
                     source=port_id[11],
                     target=port_id[7],
                     style="", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="411.9", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="411.9", y="271.0")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="509.0", y="271.0")
    CCLink = addLink(root, TYPE_LINK, id=link_id[5],
                     parent=block_id[1],
                     source=port_id[13],
                     target=port_id[0],
                     style="", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="482.5", y="169.3")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="489.6", y="169.3")
    addPointNode(ArrayNode, 'mxPoint', x="489.6", y="338.3")
    addPointNode(ArrayNode, 'mxPoint', x="354.0", y="338.3")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="354.0", y="244.7")
    CCLink = addLink(root, TYPE_LINK, id=link_id[6],
                     parent=block_id[1],
                     source=port_id[14],
                     target=port_id[8],
                     style="", value="")
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
