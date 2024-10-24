from common.AAAAAA import *


def SineVoltage(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'SineVoltage'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'SineVoltage', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnU='1', dependsOnT='0')

    addExprsNode(outnode, TYPE_STRING, 5, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 5, realParts=[
                 parameters[0], parameters[1], parameters[2],
                 parameters[3], parameters[4]])
    array = ['0']
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
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
    param = ['SineVoltage']
    addSciStringNode(equationsArrayNode, 1, param)

    param1 = ["p"]
    addSciStringNode(equationsArrayNode, 1, param1)
    param = ["n"]
    addSciStringNode(equationsArrayNode, 1, param)
    # Create the inner Array node for ScilabList
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    scilabStringParameters = ["V", "phase",
                              "freqHz", "offset",
                              "startTime"]
    addSciStringNode(innerArrayNode, height=5,
                     parameters=scilabStringParameters)
    nestedArrayNode = addArrayNode(innerArrayNode, scilabClass="ScilabList")
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=[parameters[0]])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=[parameters[1]])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=[parameters[2]])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=[parameters[3]])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=[parameters[4]])

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_SineVoltage(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0] + ',' + parameters[0]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
