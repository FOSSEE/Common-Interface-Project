from common.AAAAAA import *

def NMOS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'NMOS'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'NMOS', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 9, parameters)
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

    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "NMOS")

    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "G")

    additionalScilabStrings = ["D", "B", "S"]

    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=3, width=1)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")

    scilabStringParameters = ["W", "L", "Beta", "Vt", "K2", "K5", "dW", "dL", "RDS"]
    addSciStringNode(innerArrayNode, height=9,
                     parameters=scilabStringParameters)

    addNodeScilabDouble(innerArrayNode, height=9, realParts=[format_real_number(parameters[0]),
                        format_real_number(parameters[1]),
                        format_real_number(parameters[2]),
                        format_real_number(parameters[3]),
                        format_real_number(parameters[4]),
                        format_real_number(parameters[5]),
                        format_real_number(parameters[6]),
                        format_real_number(parameters[7]),
                        format_real_number(parameters[8])
                        ])

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_NMOS(cell):
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
