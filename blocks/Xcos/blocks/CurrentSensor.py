from common.AAAAAA import *

def CurrentSensor(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CurrentSensor'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'CurrentSensor', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)

    addSciDBNode(outnode, TYPE_DOUBLE, AS_NBZERO,
                 1, realParts=[0.0])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_NMODE,
                 1, realParts=[0.0])

    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    equationsArrayNode = addArrayNode(outnode, scilabClass="ScilabTList",
                                      **{'as': 'equations'})
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)
    additionalScilabStrings = ["CurrentSensor", "p"]
    for param in additionalScilabStrings:
        additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=1)
        addDataData(additionalStringNode, param)
    additionalStringNode = addDataNode(equationsArrayNode, 'ScilabString',
                                       height=2, width=1)
    param = ["n", "i"]
    for para in param:
        addDataData(additionalStringNode, para)

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    addScilabDBNode(innerArrayNode, 0)
    addArrayNode(innerArrayNode, scilabClass="ScilabList")
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])
    return outnode


def get_from_CurrentSensor(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
