from common.AAAAAA import *

def SourceP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SourceP'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'Source', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 4, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=4, realParts=[
                   format_real_number(parameters[0]),
                   format_real_number(parameters[1]),
                   format_real_number(parameters[2]),
                   format_real_number(parameters[3])
                   ])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ["0"]
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
    addDataData(additionalStringNode, "Source")

    addDataNode(equationsArrayNode, 'ScilabDouble',
                height=0, width=0)
    additionalStringNode1 = addDataNode(equationsArrayNode,
                                        'ScilabString',
                                        height=1, width=1)
    addDataData(additionalStringNode1, "C")

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    additionalSciStrings = ["P0", "T0", "H0", "option_temperature"]
    additionalStringNode = addDataNode(innerArrayNode,
                                       'ScilabString',
                                       height=4, width=1)
    for param in additionalSciStrings:
        addDataData(additionalStringNode, param)

    addNodeScilabDouble(innerArrayNode, height=4, realParts=[
                        format_real_number(parameters[0]),
                        format_real_number(parameters[1]),
                        format_real_number(parameters[2]),
                        format_real_number(parameters[3])
                        ])
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_SourceP(cell):
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
