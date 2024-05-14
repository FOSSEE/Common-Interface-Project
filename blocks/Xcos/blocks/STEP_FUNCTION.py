from blocks.STEP import STEP
from blocks.OUT_f import OUT_f
from common.AAAAAA import *

block_id = ['-3088270e:166584c7421:-7f30', '-3088270e:166584c7422:-7f30',
            '-3088270e:166584c7420:-7f2b', '-3088270e:166584c7420:-7f27',
            '-1e985524:130d9355381:-7ae5', '-1e985524:130d9355382:-7ae5',
            '-28bb03c0:130e63286b9:-7f9e', '-28bb03c0:130e63286b9:-7f9b',
            '-3088270e:166584c7422:-7e77']  # first three ids
port_id = ['63290cd8:18f13db2a0d:-7ff3', '63290cd8:18f13db2a0d:-7ff2',
           '63290cd8:18f13db2a0d:-7ff1', '63290cd8:18f13db2a0d:-7fee',
           '-6f1a4b5d:18f04c0dca9:-7ff0', '-6f1a4b5d:18f04c0dca9:-7fef',
           '-6f1a4b5d:18f04c0dca9:-7fee', '-6f1a4b5d:18f04c0dca9:-7feb',
           ]  # first three ids
link_id = ['63290cd8:18f13db2a0d:-7fed', '63290cd8:18f13db2a0d:-7fec',
           '-6f1a4b5d:18f04c0dca9:-7fea', '-6f1a4b5d:18f04c0dca9:-7fe9']


def STEP_FUNCTION(outroot, attribid, ordering, geometry, parameters):
    func_name = 'STEP_FUNCTION'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_C, dependsOnU='0',
                         dependsOnT='0')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
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

    STEP(root, block_id[2], ordering, geometry, parameters, parent=block_id[1])

    addPort(root, TYPE_EXPLICITOUTPORT, id=port_id[0],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="1", initialState="0.0",
            style="ExplicitOutputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
            value="")

    addPort(root, TYPE_CNTRL, id=port_id[1],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    addPort(root, TYPE_CMD, id=port_id[2],
            parent=block_id[2], ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="5.0",
            style="CommandPort", value="")

    OUT_f(root, block_id[3], ordering, geometry, parameters, parent=block_id[1])

    adPort(root, TYPE_EXPLICITINPORT, id=port_id[3],
           parent=block_id[3], ordering="1",
           initialState="0.0",
           style="ExplicitInputPort;align=right;verticalAlign=middle;spacing=10.0;rotation=0",
           value="")

    CCLink = addLink(root, TYPE_LINK, id=link_id[0],
                     parent=block_id[1],
                     source=port_id[2],
                     target=port_id[1],
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    arrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(arrayNode, 'mxPoint',
                 x="180.0", y="220.0")
    addPointNode(arrayNode, 'mxPoint',
                 x="140.0", y="220.0")
    addPointNode(arrayNode, 'mxPoint',
                 x="140.0", y="140.0")
    addPointNode(arrayNode, 'mxPoint',
                 x="180.0", y="140.0")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")

    CCLink = addLink(root, TYPE_EXLINK, id=link_id[1],
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

    addNodemxCell(SuperBlockDiagram, TYPE_MXCELL, a='defaultParent',
                  id=block_id[1],
                  parent=block_id[0])

    return outnode


def get_from_STEP_FUNCTION(cell):
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