from common.AAAAAA import *

def Resistor(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Resistor'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'resistor', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM,
                 width=1, realParts=[format_real_number(parameters[0])])
                
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
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)
    param = ['Resistor']
    addSciStringNode(equationsArrayNode, 1, param)

    param1 = ["p"]
    addSciStringNode(equationsArrayNode, 1, param1)
    param = ["n"]
    addSciStringNode(equationsArrayNode, 1, param)
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    scilabStringParameters = ["R"]
    addSciStringNode(innerArrayNode, height=1,
                     parameters=scilabStringParameters)

    innerNode = addArrayNode(innerArrayNode,
                             scilabClass="ScilabList")
    addScilabDoubleNode(innerNode, width=1, realParts=[format_real_number(parameters[0])])
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_Resistor(cell):
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
