from common.AAAAAA import *

def VsourceAC(outroot, attribid, ordering, geometry, parameters):
    func_name = 'VsourceAC'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'VsourceAC', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 2, realParts=[280.0, 50.0])
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

    additionalScilabStrings = ["VsourceAC", "p", "n"]
    for param in additionalScilabStrings:
        additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=1)
        addDataData(additionalStringNode, param)
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    param = ["VA", "f"]
    addSciStringNode(innerArrayNode, 2, param)
    innersubArrayNode = addArrayNode(innerArrayNode,
                                     scilabClass="ScilabList")
    addScilabDoubleNode(innersubArrayNode, width=1, realParts=["280.0"])
    addScilabDoubleNode(innersubArrayNode, width=1, realParts=["50.0"])
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_VsourceAC(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[0] + ',' + parameters[1]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
