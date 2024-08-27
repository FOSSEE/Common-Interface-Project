from blocks.CURVE_c import CURVE_c
from blocks.SplitBlock import SplitBlock
from blocks.OUT_f import OUT_f
from blocks.CLKOUTV_f import CLKOUTV_f
from common.AAAAAA import *

block_id = ['7b47c302:1912616652e:-7fdb', '7b47c302:1912616652f:-7fdb',
            '7b47c302:1912616652d:-7fd8', '7b47c302:1912616652d:-7fd4',
            '7b47c302:1912616652d:-7fd0', '7b47c302:1912616652d:-7fce']
link_id = ['7b47c302:1912616652d:-7fcc', '7b47c302:1912616652d:-7fcb',
           '7b47c302:1912616652d:-7fca', '7b47c302:1912616652d:-7fc9'
           ]
port_id = ['7b47c302:1912616652d:-7fd7', '7b47c302:1912616652d:-7fd6',
           '7b47c302:1912616652d:-7fd5', '7b47c302:1912616652d:-7fd3',
           '7b47c302:1912616652d:-7fd2', '7b47c302:1912616652d:-7fd1',
           '7b47c302:1912616652d:-7fcf', '7b47c302:1912616652d:-7fcd'
           ]


def Sigbuilder(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Sigbuilder'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H, dependsOnU="0", dependsOnT="0")

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

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="",
            value="")

    addPort(root, TYPE_CNTRL, id=port_id[1],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[2],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")

    SplitBlock(root, block_id[3], ordering, geometry, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[3],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[4],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")
    addPort(root, TYPE_CMD, id=port_id[5],
            parent=block_id[3], ordering="2",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="-1.0",
            style="", value="")

    param = ['0', '1', '2']
    OUT_f(root, block_id[4], ordering, geometry, param, parent=block_id[1])

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[6],
           parent=block_id[4], ordering="1",
           initialState="0.0",
           style="",
           value="")

    p = ['1']
    CLKOUTV_f(root, block_id[5], ordering, geometry, p, parent=block_id[1])

    addPort(root, TYPE_CNTRL, id=port_id[7],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="", value="")

    CCLink = addLink(root, TYPE_LINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[2],
                     target=port_id[3],
                     style="", value="drawlink")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="349.63473", y="600.47089")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="349.49528", y="565.10704")
    CCLink = addLink(root, TYPE_LINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[5],
                     target=port_id[1],
                     style="", value="drawlink")
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

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[0],
                     target=port_id[6],
                     style="", value="drawlink")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="378.20616", y="626.18517")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="398.20616", y="626.18517")

    CCLink = addLink(root, TYPE_LINK, id=link_id[3],
                     parent=block_id[1],
                     source=port_id[4],
                     target=port_id[7],
                     style="", value="drawlink")
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
