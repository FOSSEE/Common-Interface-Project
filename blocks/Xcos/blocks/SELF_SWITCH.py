from blocks.IN_f import IN_f
from blocks.OUT_f import OUT_f
from blocks.CONST_m import CONST_m
from blocks.SWITCH_f import SWITCH_f
from common.AAAAAA import *

block_id = ['-3dc88720:16056248c41:-7e85', '-3dc88720:16056248c42:-7e85',
            '-3dc88720:16056248c40:-7e17', '-3dc88720:16056248c40:-7e15',
            '-3dc88720:16056248c40:-7e13', '-3dc88720:16056248c40:-7e11']

port_id = ['-5c91adbd:18eac9e92a4:-7fe6', '-5c91adbd:18eac9e92a4:-7fe2',
           '-5c91adbd:18eac9e92a4:-7fdf', '-5c91adbd:18eac9e92a4:-7fdc',
           '-5c91adbd:18eac9e92a4:-7fda', '-5c91adbd:18eac9e92a4:-7fd8']

link_id = ['-5c91adbd:18eac9e92a4:-7fd7', '-5c91adbd:18eac9e92a4:-7fd6',
           '-5c91adbd:18eac9e92a4:-7fd5']


def SELF_SWITCH(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SELF_SWITCH'
    if parameters[0] == 'on':
        style = func_name + '_ON'
    else:
        style = func_name + '_OFF'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    subnode = addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    addScilabBoolNode(subnode, 1, parameters)
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

    array = ['1']
    IN_f(root, block_id[2], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[0],
           parent=block_id[2], ordering="1",
           initialState="0.0",
           style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    array = ['1']
    OUT_f(root, block_id[3], ordering, geometry, array)

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[1],
           parent=block_id[3], ordering="1",
           initialState="0.0",
           style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    array = ['0']
    CONST_m(root, block_id[4], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[2],
            parent=block_id[4], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    array = ['2', '1']
    SWITCH_f(root, block_id[5], ordering, geometry, array)

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[3],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITINPORT, id=port_id[4],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[5],
            parent=block_id[5], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[5],
                     target=port_id[1],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[1],
                     parent=block_id[1],
                     source=port_id[2],
                     target=port_id[4],
                     style="ExplicitLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[2],
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

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL,
                       id=block_id[1], a="defaultParent",
                       parent=block_id[0])

    return outnode


def get_from_SELF_SWITCH(cell):
    style = cell.attrib['style']
    if style == 'SELF_SWITCH_ON':
        value = 'on'
    else:
        value = 'off'

    parameters = [value]

    style = cell.attrib.get('style')
    display_parameter = 'on' if style == 'SELF_SWITCH_ON' else 'off'

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
