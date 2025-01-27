from blocks.IN_f import IN_f
from blocks.LOGIC import LOGIC
from blocks.OUT_f import OUT_f
from blocks.SPLIT_f import SPLIT_f
from blocks.TEXT_f import TEXT_f
from common.AAAAAA import *


def SUPER_f(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'SUPER_f'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(12, 14, 7)
    outnode = addOutNode(outroot, BLOCK_SUPER,
                         attribid, ordering, parent,
                         func_name, 'cscope', 'C_OR_FORTRAN',
                         style, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 0, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
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

    LOGIC(root, block_id[2], ordering, geometry, ['[0;1;1;1]', '1'], parent=block_id[1])
    addExplicitInputPort(root, port_id[0], block_id[2], "1", "-1.0")
    addExplicitInputPort(root, port_id[1], block_id[2], "2", "-1.0")
    addExplicitOutputPort(root, port_id[2], block_id[2], "1", "-1.0")

    LOGIC(root, block_id[3], ordering, geometry, ['[0;0;0;1]', '1'], parent=block_id[1])

    OUT_f(root, block_id[4], ordering, geometry, ['1'], parent=block_id[1])

    IN_f(root, block_id[5], ordering, geometry, ['1'], parent=block_id[1])

    IN_f(root, block_id[6], ordering, geometry, ['2'], parent=block_id[1])

    SPLIT_f(root, block_id[7], ordering, geometry, [], parent=block_id[1])

    LOGIC(root, block_id[8], ordering, geometry, ['[1;0]', '1'], parent=block_id[1])

    TEXT_f(root, block_id[9], ordering, geometry, ['NOT'], parent=block_id[1])

    TEXT_f(root, block_id[10], ordering, geometry, ['AND'], parent=block_id[1])

    TEXT_f(root, block_id[11], ordering, geometry, ['OR'], parent=block_id[1])

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL, a='defaultParent',
                  id=block_id[1],
                  parent=block_id[0])

    return outnode


def get_from_SUPER_f(cell):
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
