from blocks.EDGE_TRIGGER import EDGE_TRIGGER
from blocks.DOLLAR_m import DOLLAR_m
from blocks.LOGIC import LOGIC
from blocks.SPLIT_f import SPLIT_f
from blocks.LOGICAL_OP import LOGICAL_OP
from blocks.IN_f import IN_f
from blocks.OUT_f import OUT_f
from common.AAAAAA import *

block_id = ['3dd766ce:16069f39bc0:-7db3', '3dd766ce:16069f39bc1:-7db3',
            '3dd766ce:16069f39bbf:-7d64', '3dd766ce:16069f39bbf:-7d61',
            '3dd766ce:16069f39bbf:-7d5e', '3dd766ce:16069f39bbf:-7d58',
            '3dd766ce:16069f39bbf:-7d53', '3dd766ce:16069f39bbf:-7d50',
            '3dd766ce:16069f39bbf:-7d4b', '3dd766ce:16069f39bbf:-7d49',
            '3dd766ce:16069f39bbf:-7d47', '3dd766ce:16069f39bbf:-7d45',
            '3dd766ce:16069f39bbf:-7d43']

port_id = ['5f0e1c8f:18e5f578986:-7f74', '5f0e1c8f:18e5f578986:-7f72',
           '5f0e1c8f:18e5f578986:-7f6f', '5f0e1c8f:18e5f578986:-7f6e',
           '5f0e1c8f:18e5f578986:-7f58', '5f0e1c8f:18e5f578986:-7f56',
           '5f0e1c8f:18e5f578986:-7f54', '5f0e1c8f:18e5f578986:-7f52',
           '5f0e1c8f:18e5f578986:-7f51', '5f0e1c8f:18e5f578986:-7f4e',
           '5f0e1c8f:18e5f578986:-7f4c', '5f0e1c8f:18e5f578986:-7f4a',
           '5f0e1c8f:18e5f578986:-7f48', '5f0e1c8f:18e5f578986:-7f45',
           '5f0e1c8f:18e5f578986:-7f43', '5f0e1c8f:18e5f578986:-7f40',
           '5f0e1c8f:18e5f578986:-7f3e', '5f0e1c8f:18e5f578986:-7f3c',
           '5f0e1c8f:18e5f578986:-7f3a', '5f0e1c8f:18e5f578986:-7f37',
           '5f0e1c8f:18e5f578986:-7f34', '5f0e1c8f:18e5f578986:-7f31',
           '5f0e1c8f:18e5f578986:-7f2e', '5f0e1c8f:18e5f578986:-7f2b']

link_id = ['5f0e1c8f:18e5f578986:-7f2a', '5f0e1c8f:18e5f578986:-7f29',
           '5f0e1c8f:18e5f578986:-7f28', '5f0e1c8f:18e5f578986:-7f27',
           '5f0e1c8f:18e5f578986:-7f26', '5f0e1c8f:18e5f578986:-7f25',
           '5f0e1c8f:18e5f578986:-7f24', '5f0e1c8f:18e5f578986:-7f23',
           '5f0e1c8f:18e5f578986:-7f22', '5f0e1c8f:18e5f578986:-7f21',
           '5f0e1c8f:18e5f578986:-7f20']


def JKFLIPFLOP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'JKFLIPFLOP'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H,
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
    addArrayNode(outnode, scilabClass="ScilabList",
                                      **{'as': 'equations'})
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

    DOLLAR_m(root, block_id[2], ordering, geometry, parameters)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[1],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    EDGE_TRIGGER(root, block_id[3], ordering, geometry, parameters)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[2],
            parent=block_id[3], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CMD, id=port_id[3],
            parent=block_id[3], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    array = ['[0;1;1;1;0;0;1;0]', '0']
    LOGIC(root, block_id[4], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[4],
            parent=block_id[4], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

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

    addPort(root, TYPE_CNTRL, id=port_id[8],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    SPLIT_f(root, block_id[5], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[9],
            parent=block_id[5], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[10],
            parent=block_id[5], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[11],
            parent=block_id[5], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[12],
            parent=block_id[5], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['1', '5', '5', '0']
    LOGICAL_OP(root, block_id[6], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[13],
            parent=block_id[6], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[14],
            parent=block_id[6], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    SPLIT_f(root, block_id[7], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[15],
            parent=block_id[7], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[16],
            parent=block_id[7], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[17],
            parent=block_id[7], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[18],
            parent=block_id[7], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    IN_f(root, block_id[8], ordering, geometry, ['2'])

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[19],
            parent=block_id[8], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    IN_f(root, block_id[9], ordering, geometry, ['2'])

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[20],
            parent=block_id[9], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    IN_f(root, block_id[10], ordering, geometry, ['3'])

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[21],
            parent=block_id[10], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    OUT_f(root, block_id[11], ordering, geometry, ['1'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[22],
            parent=block_id[11], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    OUT_f(root, block_id[12], ordering, geometry, ['1'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[23],
            parent=block_id[12], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[14],
                     target=port_id[23],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[11],
                     target=port_id[22],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[21],
                     target=port_id[6],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[3],
                     parent=block_id[1],
                     source=port_id[20],
                     target=port_id[5],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[4],
                     parent=block_id[1],
                     source=port_id[19],
                     target=port_id[2],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[5],
                     parent=block_id[1],
                     source=port_id[17],
                     target=port_id[13],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[6],
                     parent=block_id[1],
                     source=port_id[16],
                     target=port_id[9],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[7],
                     parent=block_id[1],
                     source=port_id[3],
                     target=port_id[8],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[8],
                     parent=block_id[1],
                     source=port_id[10],
                     target=port_id[0],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[9],
                     parent=block_id[1],
                     source=port_id[1],
                     target=port_id[4],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[10],
                     parent=block_id[1],
                     source=port_id[7],
                     target=port_id[15],
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


def get_from_JKFLIPFLOP(cell):
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
