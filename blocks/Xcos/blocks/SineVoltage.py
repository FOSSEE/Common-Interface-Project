from common.AAAAAA import *

def SineVoltage(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SineVoltage'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'SineVoltage', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 5, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 5, realParts=[1.5, 0.0, 15.92356687898089, 0.0, 0.0])
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
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=["1.5"])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=["0.0"])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=["15.92356687898089"])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=["0.0"])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=["0.0"])

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
