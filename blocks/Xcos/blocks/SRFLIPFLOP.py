from blocks.LOGIC import LOGIC
from blocks.DOLLAR_m import DOLLAR_m
from blocks.SPLIT_f import SPLIT_f
from blocks.OUT_f import OUT_f
from blocks.IN_f import IN_f
from common.AAAAAA import *

block_id = ['5cc9645e:16194321244:-7fca', '5cc9645e:16194321245:-7fca',
            '5cc9645e:16194321243:-7f75', '5cc9645e:16194321243:-7f6f',
            '5cc9645e:16194321243:-7f6c', '5cc9645e:16194321243:-7f67',
            '5cc9645e:16194321243:-7f65', '5cc9645e:16194321243:-7f63',
            '5cc9645e:16194321243:-7f61']

port_id = ['-5c91adbd:18eac9e92a4:-7fba', '-5c91adbd:18eac9e92a4:-7fb8',
           '-5c91adbd:18eac9e92a4:-7fb6', '-5c91adbd:18eac9e92a4:-7fb4',
           '-5c91adbd:18eac9e92a4:-7fb2', '-5c91adbd:18eac9e92a4:-7faf',
           '-5c91adbd:18eac9e92a4:-7fad', '-5c91adbd:18eac9e92a4:-7faa',
           '-5c91adbd:18eac9e92a4:-7fa8', '-5c91adbd:18eac9e92a4:-7fa6',
           '-5c91adbd:18eac9e92a4:-7fa4', '-5c91adbd:18eac9e92a4:-7fa1',
           '-5c91adbd:18eac9e92a4:-7f9e', '-5c91adbd:18eac9e92a4:-7f9b',
           '-5c91adbd:18eac9e92a4:-7f98']

link_id = ['-5c91adbd:18eac9e92a4:-7f97', '-5c91adbd:18eac9e92a4:-7f96',
           '-5c91adbd:18eac9e92a4:-7f95', '-5c91adbd:18eac9e92a4:-7f94',
           '-5c91adbd:18eac9e92a4:-7f93', '-5c91adbd:18eac9e92a4:-7f92',
           '-5c91adbd:18eac9e92a4:-7f91']


def SRFLIPFLOP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SRFLIPFLOP'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H,
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

    LOGIC(root, block_id[2], ordering, geometry, ['[0 1;1 0;1 0;1 0;0 1;0 1;0 0;0 0]', '1'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[1],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[2],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[3],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[4],
            parent=block_id[2], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    DOLLAR_m(root, block_id[3], ordering, geometry, ['int8(0)', '1'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[5],
            parent=block_id[3], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[6],
            parent=block_id[3], ordering="1",
            dataType="INT8_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    SPLIT_f(root, block_id[4], ordering, geometry, ['0'])

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[7],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[8],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[9],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[10],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['2']
    OUT_f(root, block_id[5], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[11],
            parent=block_id[5], ordering="1",
            initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['1']
    IN_f(root, block_id[6], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[12],
            parent=block_id[6], ordering="1",
            initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['2']
    IN_f(root, block_id[7], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[13],
            parent=block_id[7], ordering="1",
            initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['1']
    OUT_f(root, block_id[8], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[14],
            parent=block_id[8], ordering="1",
            initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[9],
                     target=port_id[14],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[13],
                     target=port_id[2],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[12],
                     target=port_id[1],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[3],
                     parent=block_id[1],
                     source=port_id[4],
                     target=port_id[11],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[4],
                     parent=block_id[1],
                     source=port_id[8],
                     target=port_id[5],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[5],
                     parent=block_id[1],
                     source=port_id[6],
                     target=port_id[0],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[6],
                     parent=block_id[1],
                     source=port_id[3],
                     target=port_id[7],
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
