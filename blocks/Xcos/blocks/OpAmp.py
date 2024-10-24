from common.AAAAAA import *


def OpAmp(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'OpAmp'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'OpAmp', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    array = ['0']
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0,
                [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    equationsArrayNode = addObjNode(outnode, TYPE_ARRAY,
                                    CLASS_TLIST, AS_EQUATIONS, parameters)
    # Add ScilabString nodes to equationsArrayNode
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)
    param = ['OpAmp']
    addSciStringNode(equationsArrayNode, 1, param)

    param1 = ["in_p", "in_n"]
    addSciStringNode(equationsArrayNode, 2, param1)
    param = ['out']
    addSciStringNode(equationsArrayNode, 1, param)
    # Create the inner Array node for ScilabList
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    addScilabDBNode(innerArrayNode, height=0)
    addScilabDBNode(innerArrayNode, height=0)

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_OpAmp(cell):
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
