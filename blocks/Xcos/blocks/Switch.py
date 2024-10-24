from common.AAAAAA import *


def Switch(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'Switch'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'Switch', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnU='1', dependsOnT='0')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 2, realParts=[0.01, 100000.0])
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
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)

    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "Switch")
    additionalScilabStrings = ["p", "inp"]
    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=2, width=1)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)
    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "n")

    nestedArrayNode = addArrayNode(equationsArrayNode,
                                   scilabClass="ScilabList")
    additionalScilabStrings = ["Ron", "Roff"]
    additionalStringNode = addDataNode(nestedArrayNode,
                                       'ScilabString',
                                       height=2, width=1)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    realParts = ["0.01", "100000.0"]
    additionalStringNode = addDataNode(nestedArrayNode,
                                       'ScilabDouble',
                                       height=2, width=1)
    for i, realPart in enumerate(realParts):
        addDData(additionalStringNode, column=0, line=i, realPart=realPart)

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_Switch(cell):
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
