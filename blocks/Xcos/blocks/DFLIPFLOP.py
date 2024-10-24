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

    block_id, port_id, link_id = generate_id(21, 52, 24)
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

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['1', '1']
    IFTHEL_f(root, block_id[3], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[1],
           parent=block_id[3], ordering="1",
           initialState="0.0",
           style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    addPort(root, TYPE_CNTRL, id=port_id[2],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CMD, id=port_id[3],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    addPort(root, TYPE_CMD, id=port_id[4],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    array = ['2', '1', '5', '0']
    LOGICAL_OP(root, block_id[4], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[5],
            parent=block_id[4], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[6],
            parent=block_id[4], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[7],
            parent=block_id[4], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['5']
    SAMPHOLD_m(root, block_id[5], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[8],
            parent=block_id[5], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[9],
            parent=block_id[5], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CNTRL, id=port_id[10],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    array = ['1', '5', '5', '0']
    LOGICAL_OP(root, block_id[6], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[11],
            parent=block_id[6], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[12],
            parent=block_id[6], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['3']
    IN_f(root, block_id[7], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[13],
           parent=block_id[7], ordering="1",
           initialState="0.0",
           style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    array = ['1']
    IN_f(root, block_id[8], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[14],
           parent=block_id[8], ordering="1",
           initialState="0.0",
           style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    array = ['2']
    OUT_f(root, block_id[9], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[15],
           parent=block_id[9], ordering="1",
           initialState="0.0",
           style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    array = ['1']
    OUT_f(root, block_id[10], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[16],
           parent=block_id[10], ordering="1",
           initialState="0.0",
           style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    ANDBLK(root, block_id[10], ordering, geometry, ['0'])

    addPort(root, TYPE_CNTRL, id=port_id[17],
            parent=block_id[10], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CNTRL, id=port_id[18],
            parent=block_id[10], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CMD, id=port_id[19],
            parent=block_id[10], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    EDGE_TRIGGER(root, block_id[11], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[20],
            parent=block_id[11], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CMD, id=port_id[21],
            parent=block_id[10], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    IN_f(root, block_id[12], ordering, geometry, ['2'])

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[22],
           parent=block_id[12], ordering="1",
           initialState="0.0",
           style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    Extract_Activation(root, block_id[13], ordering, geometry, ['2'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[23],
            parent=block_id[13], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CMD, id=port_id[24],
            parent=block_id[13], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    SUM_f(root, block_id[14], ordering, geometry, ['2'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[25],
            parent=block_id[14], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[26],
            parent=block_id[14], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[27],
            parent=block_id[14], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[28],
            parent=block_id[14], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    SPLIT_f(root, block_id[15], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[29],
            parent=block_id[15], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[30],
            parent=block_id[15], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[31],
            parent=block_id[15], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[32],
            parent=block_id[15], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    SPLIT_f(root, block_id[16], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[33],
            parent=block_id[16], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[34],
            parent=block_id[16], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[35],
            parent=block_id[16], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[36],
            parent=block_id[16], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['5', '2', '1']
    SELECT_m(root, block_id[17], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[36],
            parent=block_id[17], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[37],
            parent=block_id[17], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[38],
            parent=block_id[17], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CNTRL, id=port_id[39],
            parent=block_id[17], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CNTRL, id=port_id[40],
            parent=block_id[17], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    SPLIT_f(root, block_id[18], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[41],
            parent=block_id[18], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[42],
            parent=block_id[18], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[43],
            parent=block_id[18], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[44],
            parent=block_id[18], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    SPLIT_f(root, block_id[19], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[45],
            parent=block_id[19], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[46],
            parent=block_id[19], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[47],
            parent=block_id[19], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[48],
            parent=block_id[19], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    SPLIT_f(root, block_id[20], ordering, geometry, ['0'])

    addPort(root, TYPE_CNTRL, id=port_id[49],
            parent=block_id[20], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CMD, id=port_id[50],
            parent=block_id[20], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    addPort(root, TYPE_CMD, id=port_id[51],
            parent=block_id[20], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    CCLink = addLink(root, TYPE_LINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[4],
                     target=port_id[40],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[51],
                     target=port_id[39],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[50],
                     target=port_id[10],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[3],
                     parent=block_id[1],
                     source=port_id[47],
                     target=port_id[37],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[4],
                     parent=block_id[1],
                     source=port_id[46],
                     target=port_id[6],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[5],
                     parent=block_id[1],
                     source=port_id[43],
                     target=port_id[16],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[6],
                     parent=block_id[1],
                     source=port_id[42],
                     target=port_id[11],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[7],
                     parent=block_id[1],
                     source=port_id[38],
                     target=port_id[41],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[8],
                     parent=block_id[1],
                     source=port_id[9],
                     target=port_id[36],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[9],
                     parent=block_id[1],
                     source=port_id[28],
                     target=port_id[23],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[10],
                     parent=block_id[1],
                     source=port_id[35],
                     target=port_id[27],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[11],
                     parent=block_id[1],
                     source=port_id[34],
                     target=port_id[1],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[12],
                     parent=block_id[1],
                     source=port_id[31],
                     target=port_id[25],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[13],
                     parent=block_id[1],
                     source=port_id[30],
                     target=port_id[20],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[14],
                     parent=block_id[1],
                     source=port_id[22],
                     target=port_id[29],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[15],
                     parent=block_id[1],
                     source=port_id[24],
                     target=port_id[2],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[16],
                     parent=block_id[1],
                     source=port_id[21],
                     target=port_id[17],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[17],
                     parent=block_id[1],
                     source=port_id[19],
                     target=port_id[49],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[18],
                     parent=block_id[1],
                     source=port_id[3],
                     target=port_id[18],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[19],
                     parent=block_id[1],
                     source=port_id[12],
                     target=port_id[15],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[20],
                     parent=block_id[1],
                     source=port_id[14],
                     target=port_id[5],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[21],
                     parent=block_id[1],
                     source=port_id[13],
                     target=port_id[33],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[22],
                     parent=block_id[1],
                     source=port_id[0],
                     target=port_id[45],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[23],
                     parent=block_id[1],
                     source=port_id[7],
                     target=port_id[8],
                     style="ExplicitLink", value="")
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
