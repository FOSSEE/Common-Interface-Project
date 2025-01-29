from blocks.STEP import STEP
from blocks.OUT_f import OUT_f
from common.AAAAAA import *

# block_id = ['-3088270e:166584c7421:-7f30', '-3088270e:166584c7422:-7f30',
#             '-3088270e:166584c7420:-7f2b', '-3088270e:166584c7420:-7f27',
#             '-1e985524:130d9355381:-7ae5', '-1e985524:130d9355382:-7ae5',
#             '-28bb03c0:130e63286b9:-7f9e', '-28bb03c0:130e63286b9:-7f9b',
#             '-3088270e:166584c7422:-7e77']  # first three ids
# port_id = ['63290cd8:18f13db2a0d:-7ff3', '63290cd8:18f13db2a0d:-7ff2',
#            '63290cd8:18f13db2a0d:-7ff1', '63290cd8:18f13db2a0d:-7fee',
#            '-6f1a4b5d:18f04c0dca9:-7ff0', '-6f1a4b5d:18f04c0dca9:-7fef',
#            '-6f1a4b5d:18f04c0dca9:-7fee', '-6f1a4b5d:18f04c0dca9:-7feb',
#            ]  # first three ids
# link_id = ['63290cd8:18f13db2a0d:-7fed', '63290cd8:18f13db2a0d:-7fec',
#            '-6f1a4b5d:18f04c0dca9:-7fea', '-6f1a4b5d:18f04c0dca9:-7fe9']


def STEP_FUNCTION(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'STEP_FUNCTION'
    if style is None:
        style = func_name

    block_id, port_id, link_id = generate_id(9, 8, 4)
    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'csuper', 'DEFAULT',
                         style, BLOCKTYPE_H, dependsOnU='0',
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
    superAddNode(Array, TYPE_ADD, value=" ")

    mxGraphModel = addmxGraphModelNode(SuperBlockDiagram,
                                       TYPE_MODEL, a="model")
    root = addNode(mxGraphModel, TYPE_ROOT)
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[0])
    addmxCellNode(root, TYPE_MXCELL,
                  id=block_id[1],
                  parent=block_id[0])

    STEP(root, block_id[2], ordering, geometry, parameters, parent=block_id[1])
    addExplicitOutputPort(root, port_id[0], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="1")
    addControlPort(root, port_id[1], block_id[2], "1", "0.0", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")
    addCommandPort(root, port_id[2], block_id[2], "1", "0.005", dataType="REAL_MATRIX", dataColumns="1", dataLines="-1")

    OUT_f(root, block_id[3], ordering, geometry, ['1'], parent=block_id[1])
    addExplicitInputPort(root, port_id[3], block_id[3], "1", "0.0")

    CCLink = addExplicitLink(root, link_id[1], block_id[1], port_id[0], port_id[3])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="44.0", y="20.0")
    addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="-4.0", y="10.0")

    CCLink = addCommandControlLink(root, link_id[0], block_id[1], port_id[2], port_id[1])
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="20.0", y="-4.0")
    arrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(arrayNode, 'mxPoint',
                 x="116.00000299999998", y="174.39289999999994")
    addPointNode(arrayNode, 'mxPoint',
                 x="77.47839499999999", y="174.39289999999994")
    addPointNode(arrayNode, 'mxPoint',
                 x="77.47839499999999", y="84.69677999999999")
    addPointNode(arrayNode, 'mxPoint',
                 x="116.00000299999998", y="84.69677999999999")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="44.0")

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
