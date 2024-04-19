from common.AAAAAA import *

def ConstantVoltage(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ConstantVoltage'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'ConstantVoltage', 'DEFAULT',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 1,
                format_real_number(parameters[0]))
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

    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)

    additionalScilabStrings = ["ConstantVoltage", "p", "n"]
    for param in additionalScilabStrings:
        additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=1)
        addDataData(additionalStringNode, param)

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")

    scilabStringParameters = ["V"]
    addScilabStringNode(innerArrayNode, width=1,
                        parameters=scilabStringParameters)

    innerArrayNode = addArrayNode(innerArrayNode,
                                  scilabClass="ScilabList")
    innerNode = addDataNode(innerArrayNode, 'ScilabDouble', height=1, width=1)
    addScilabDoubleNode(innerNode, width=1, realParts=format_real_number(parameters[0]))

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_ConstantVoltage(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = si_format(parameters[0])

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
