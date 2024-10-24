from common.AAAAAA import *


def Inductor(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'Inductor'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'Inductor', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnU='1', dependsOnT='0')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 1, realParts=[format_real_number(parameters[0])])
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

    # Add additional ScilabString nodes to equationsArrayNode
    additionalScilabStrings = ["Inductor", "p", "n"]
    for param in additionalScilabStrings:
        additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=1)
        addDataData(additionalStringNode, param)
    nestedArrayNode = addArrayNode(equationsArrayNode,
                                   scilabClass="ScilabList")
    addScilabStringNode(nestedArrayNode, width=1,
                        parameters='L')
    subnestedarray = addArrayNode(nestedArrayNode,
                                  scilabClass="ScilabList")
    addScilabDoubleNode(subnestedarray, width=1, realParts=[format_real_number(parameters[0])])

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_Inductor(cell):
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
