from blocks.IN_f import IN_f
from blocks.OUT_f import OUT_f
from blocks.CONST_m import CONST_m
from blocks.SWITCH_f import SWITCH_f
from common.AAAAAA import *


def SELF_SWITCH(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'SELF_SWITCH'
    if style is None:
        style = func_name

    if parameters[0] == 'on':
        style = func_name + '_ON'
    else:
        style = func_name + '_OFF'
    block_id, port_id, link_id = generate_id(6, 6, 3)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
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
    addExplicitOutputPort(root, port_id[0], block_id[2], "1", "0.0")

    array = ['1']
    OUT_f(root, block_id[3], ordering, geometry, array)
    addExplicitInputPort(root, port_id[1], block_id[3], "1", "0.0")

    array = ['0']
    CONST_m(root, block_id[4], ordering, geometry, array)
    addExplicitOutputPort(root, port_id[2], block_id[4], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    SWITCH_f(root, block_id[5], ordering, geometry, [parameters[0], '2'])
    addExplicitInputPort(root, port_id[3], block_id[5], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addExplicitInputPort(root, port_id[4], block_id[5], "2", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addExplicitOutputPort(root, port_id[5], block_id[5], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")

    CCLink = addLink(root, LINK_EXPLICIT, id=link_id[0],
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

    CCLink = addLink(root, LINK_EXPLICIT, id=link_id[1],
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

    CCLink = addLink(root, LINK_EXPLICIT, id=link_id[2],
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
