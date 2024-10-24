from blocks.ANDLOG_f import ANDLOG_f
from blocks.CLKIN_f import CLKIN_f
from blocks.CLKOUT_f import CLKOUT_f
from blocks.IFTHEL_f import IFTHEL_f
from blocks.CLKSPLIT_f import CLKSPLIT_f
from common.AAAAAA import *


def ANDBLK(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'ANDBLK'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(8, 13, 6)
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

    ANDLOG_f(root, block_id[2], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CNTRL, id=port_id[1],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CNTRL, id=port_id[2],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    CLKIN_f(root, block_id[3], ordering, geometry, ['1'])

    addPort(root, TYPE_CMD, id=port_id[3],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    CLKOUT_f(root, block_id[4], ordering, geometry, ['1'])

    addPort(root, TYPE_CNTRL, id=port_id[4],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    CLKIN_f(root, block_id[5], ordering, geometry, ['2'])

    addPort(root, TYPE_CMD, id=port_id[5],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    array = ['1', '1']
    IFTHEL_f(root, block_id[6], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[6],
           parent=block_id[6], ordering="1",
           initialState="0.0",
           style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    addPort(root, TYPE_CNTRL, id=port_id[7],
            parent=block_id[6], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CMD, id=port_id[8],
            parent=block_id[6], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    addPort(root, TYPE_CMD, id=port_id[9],
            parent=block_id[6], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    CLKSPLIT_f(root, block_id[7], ordering, geometry, array)

    addPort(root, TYPE_CNTRL, id=port_id[10],
            parent=block_id[7], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CMD, id=port_id[11],
            parent=block_id[7], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    addPort(root, TYPE_CMD, id=port_id[12],
            parent=block_id[7], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    CCLink = addLink(root, TYPE_LINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[12],
                     target=port_id[7],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[11],
                     target=port_id[2],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[0],
                     target=port_id[6],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[3],
                     parent=block_id[1],
                     source=port_id[8],
                     target=port_id[4],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[4],
                     parent=block_id[1],
                     source=port_id[5],
                     target=port_id[10],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[5],
                     parent=block_id[1],
                     source=port_id[3],
                     target=port_id[1],
                     style="CommandControlLink", value="")
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


def get_from_ANDBLK(cell):
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
