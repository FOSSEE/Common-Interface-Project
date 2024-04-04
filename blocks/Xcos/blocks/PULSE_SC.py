from blocks.CONST_m import CONST_m
from blocks.Ground_g import Ground_g
from blocks.SELECT_m import SELECT_m
from blocks.SampleCLK import SampleCLK
from blocks.OUT_f import OUT_f
from common.AAAAAA import *

block_id = ['23f170f2:16054d9b97b:-7d2e', '23f170f2:16054d9b97c:-7d2e',
            '23f170f2:16054d9b97a:-7d2a', '23f170f2:16054d9b97a:-7d28',
            '23f170f2:16054d9b97a:-7d26', '23f170f2:16054d9b97a:-7d20',
            '23f170f2:16054d9b97a:-7d1e', '23f170f2:16054d9b97a:-7d1c']

port_id = ['5631d1e9:18ea7a6d774:-7fd7', '5631d1e9:18ea7a6d774:-7fd4',
           '5631d1e9:18ea7a6d774:-7fd1', '5631d1e9:18ea7a6d774:-7fcf',
           '5631d1e9:18ea7a6d774:-7fcd', '5631d1e9:18ea7a6d774:-7fcc',
           '5631d1e9:18ea7a6d774:-7fcb', '5631d1e9:18ea7a6d774:-7fc9',
           '5631d1e9:18ea7a6d774:-7fc7', '5631d1e9:18ea7a6d774:-7fc4']

link_id = ['5631d1e9:18ea7a6d774:-7fc3', '5631d1e9:18ea7a6d774:-7fc2',
           '5631d1e9:18ea7a6d774:-7fc1', '5631d1e9:18ea7a6d774:-7fc0',
           '5631d1e9:18ea7a6d774:-7fbf']


def PULSE_SC(outroot, attribid, ordering, geometry, parameters):
    func_name = 'PULSE_SC'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H)

    addExprsNode(outnode, TYPE_STRING, 4, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, ['1'])
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
    superAddNode(Array, TYPE_ADD, value="E2=E+W/100*F")
    superAddNode(Array, TYPE_ADD,
                 value="if (W<0 | W>100) then error('Width must be between 0 and 100');end")
    superAddNode(Array, TYPE_ADD,
                 value="if (E2 >= F) then error ('Offset must be lower than (frequency*(1-Width/100))'); end")

    mxGraphModel = addmxGraphModelNode(SuperBlockDiagram,
                                       TYPE_MODEL, a="model")
    root = addNode(mxGraphModel, TYPE_ROOT)
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[0])
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[1],
                  parent=block_id[0])

    array = ['A']
    CONST_m(root, block_id[2], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    Ground_g(root, block_id[3], ordering, geometry, parameters)

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[1],
            parent=block_id[3], ordering="1",
            initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['-1', '2', '1']
    SELECT_m(root, block_id[4], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[2],
            parent=block_id[4], ordering="1",
            initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[3],
            parent=block_id[4], ordering="1",
            initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[4],
            parent=block_id[4], ordering="1",
            initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CNTRL, id=port_id[5],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CNTRL, id=port_id[6],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    SampleCLK(root, block_id[5], ordering, geometry, parameters)

    addPort(root, TYPE_CMD, id=port_id[7],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    SampleCLK(root, block_id[6], ordering, geometry, parameters)

    addPort(root, TYPE_CMD, id=port_id[8],
            parent=block_id[6], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    array = ['1']
    OUT_f(root, block_id[7], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[9],
            parent=block_id[7], ordering="1",
            initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[4],
                     target=port_id[9],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[7],
                     target=port_id[5],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_LINK, id=link_id[2],
                     parent=block_id[1],
                     source=port_id[8],
                     target=port_id[6],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[3],
                     parent=block_id[1],
                     source=port_id[0],
                     target=port_id[3],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[4],
                     parent=block_id[1],
                     source=port_id[1],
                     target=port_id[2],
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


def get_from_PULSE_SC(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
