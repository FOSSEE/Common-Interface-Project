from blocks.CLKOUTV_f import CLKOUTV_f
from blocks.CLOCK_c import CLOCK_c
from common.AAAAAA import *

# block_id = ['-64ce6d85:145ef6f2b50:-7ee7', '-64ce6d85:145ef6f2b51:-7ee7',
#             '-64ce6d85:145ef6f2b4f:-7f54']


def SUPER_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SUPER_f'
    block_id, port_id, link_id = generate_id(3, 0, 0)
    outnode = addOutNode(outroot, BLOCK_SUPER,
                         attribid, ordering, 1,
                         func_name, 'cscope', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C)

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

    CLOCK_c(root, block_id[2], ordering, geometry, parameters)

    CLOCK_c(root, block_id[2], ordering, geometry, parameters)

    CLKOUTV_f(root, block_id[1], ordering, geometry, parameters)

    CLKOUTV_f(root, block_id[1], ordering, geometry, parameters)
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
