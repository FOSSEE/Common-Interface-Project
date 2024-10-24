from common.AAAAAA import *


def VVsourceAC(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'VVsourceAC'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'VVsourceAC', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=1, realParts=[
                   format_real_number(parameters[0])])
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
    addDataData(additionalStringNode, "VVsourceAC")

    additionalSciStrings = ["p", "VA"]
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
    innerNode = addDataNode(innerArrayNode, 'ScilabString',
                            height=1, width=1)
    addDataData(innerNode, "f")

    innerArrayNode1 = addArrayNode(innerArrayNode, scilabClass="ScilabList")

    addNodeScilabDouble(innerArrayNode1, height=1, realParts=[
                        format_real_number(parameters[0])])

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_VVsourceAC(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
