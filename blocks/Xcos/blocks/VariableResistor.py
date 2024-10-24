from common.AAAAAA import *


def VariableResistor(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'VariableResistor'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'VariableResistor', 'DEFAULT',
                         style, BLOCKTYPE_C,
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
    equationsArrayNode = addArrayNode(outnode, scilabClass="ScilabTList",
                                      **{'as': 'equations'})

    # Add ScilabString nodes to equationsArrayNode
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)

    # Add additional ScilabString nodes to equationsArrayNode
    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "VariableResistor")

    additionalSciStrings = ["p", "R"]
    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=1, width=2)
    for param in additionalSciStrings:
        addDataData(additionalStringNode, param)
    additionalStringNode1 = addDataNode(equationsArrayNode,
                                        'ScilabString',
                                        height=1, width=1)
    addDataData(additionalStringNode1, "n")

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    addDataNode(innerArrayNode, 'ScilabDouble',
                height=0, width=0)
    addArrayNode(innerArrayNode, scilabClass="ScilabList")

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_VariableResistor(cell):
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
