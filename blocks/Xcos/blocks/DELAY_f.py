from blocks.EVTDLY_f import EVTDLY_f
from blocks.REGISTER_f import REGISTER_f
from blocks.IN_f import IN_f
from blocks.OUT_f import OUT_f
from common.AAAAAA import *

block_id = ['18f5f971:13894cb2d90:-7f6f', '18f5f971:13894cb2d91:-7f6f',
            '-73e75f0:167968eb73f:-7c07', '-73e75f0:167968eb73f:-7c05',
            '-73e75f0:167968eb73f:-7c03', '-73e75f0:167968eb73f:-7bff']
port_id = ['7a86d9c5:18e504d8baa:-7fae']


def DELAY_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DELAY_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
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

    IN_f(root, block_id[2], ordering, geometry, parameters)

    adPort(root, TYPE_EXPLICITOUTPORT, id=port_id[0],
           parent=block_id[2], ordering="1",
           initialState="0.0",
           style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    OUT_f(root, block_id[3], ordering, geometry, parameters)

    REGISTER_f(root, block_id[4], ordering, geometry, parameters)

    EVTDLY_f(root, block_id[5], ordering, geometry, parameters)

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL, a='defaultParent',
                  id=block_id[1],
                  parent=block_id[0])

    return outnode


def get_from_DELAY_f(cell):
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
