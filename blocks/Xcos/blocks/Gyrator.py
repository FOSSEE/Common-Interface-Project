from common.AAAAAA import *


def Gyrator(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'Gyrator'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'Gyrator', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=2, realParts=[
        format_real_number(parameters[0]),
        format_real_number(parameters[1])])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
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
    addDataData(additionalStringNode, "Gyrator")

    additionalScilabStrings = ["p1", "n1"]
    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=2, width=1)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    additionalScilabStrings = ["p2", "n2"]
    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=2, width=1)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    additionalScilabStrings = ["G1", "G2"]
    additionalStringNode = addDataNode(innerArrayNode,
                                       'ScilabString',
                                       height=2, width=1)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    addNodeScilabDouble(innerArrayNode, height=2, realParts=[
        format_real_number(parameters[0]),
        format_real_number(parameters[1])])
    addNodeScilabDouble(innerArrayNode, height=2, realParts=[
        format_real_number('0'),
        format_real_number('0')])
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_Gyrator(cell):
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
