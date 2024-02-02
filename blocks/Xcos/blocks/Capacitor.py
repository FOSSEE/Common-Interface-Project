from common.AAAAAA import *
def Capacitor(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Capacitor'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'Capacitor', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 1,
                format_real_number(parameters[0]))
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    # Create the outer Array node for equations
    equationsArrayNode = addArrayNode(outnode, scilabClass="ScilabTList",
                                      **{'as': 'equations'})

    # Add ScilabString nodes to equationsArrayNode
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)

    # Add additional ScilabString nodes to equationsArrayNode
    additionalScilabStrings = ["Capacitor", "p", "n"]
    for param in additionalScilabStrings:
        additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=1)
        addDataData(additionalStringNode, param)

    # Create the inner Array node for ScilabList
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")

    scilabStringParameters = ["C", "v"]
    addScilabStringNode(innerArrayNode, width=2,
                        parameters=scilabStringParameters)

    # Add nested Array node inside innerArrayNode
    nestedArrayNode = addArrayNode(innerArrayNode,
                                   scilabClass="ScilabList")
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=["4.7E-6"])
    addScilabDoubleNode(nestedArrayNode, width=1, realParts=["2.0"])
    addScilabDoubleNode(innerArrayNode, width=2, realParts=["0.0", "1.0"])
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])
    return outnode


def get_from_Capacitor(cell):
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
