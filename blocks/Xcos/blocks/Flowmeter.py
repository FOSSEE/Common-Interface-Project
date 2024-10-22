from common.AAAAAA import *


def Flowmeter(outroot, attribid, ordering, geometry, parameters, parent=1):
    func_name = 'Flowmeter'
    parameters = ['1']

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'Flowmeter', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=1, realParts=[
                   format_real_number(parameters[0])])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
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
    additionalScilabStrings = ["Flowmeter", "C1"]
    for param in additionalScilabStrings:
        additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=1)
        addDataData(additionalStringNode, param)

    additionalSciStrings = ["Mesure", "C2"]
    additionalStringNode1 = addDataNode(equationsArrayNode,
                                        'ScilabString',
                                        height=2, width=1)
    for param1 in additionalSciStrings:
        addDataData(additionalStringNode1, param1)

    # Create the inner Array node for ScilabList
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")

    scilabStringParameters = ["Qini"]
    addScilabStringNode(innerArrayNode, width=1,
                        parameters=scilabStringParameters)

    # Add nested Array node inside innerArrayNode
    addScilabDoubleNode(innerArrayNode, width=1, realParts=["1.0"])
    addScilabDoubleNode(innerArrayNode, width=1, realParts=["0.0"])
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_Flowmeter(cell):
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
