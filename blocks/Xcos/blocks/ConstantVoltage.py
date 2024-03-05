from common.AAAAAA import *

def ConstantVoltage(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ConstantVoltage'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'ConstantVoltage', 'DEFAULT',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM,
                 1, realParts=[5.0])

    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0,
                [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    addSciDBNode(outnode, TYPE_DOUBLE, AS_NBZERO,
                 1, realParts=[0.0])
    addSciDBNode(outnode, TYPE_DOUBLE, AS_NMODE,
                 1, realParts=[0.0])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    equationsArrayNode = addObjNode(outnode, TYPE_ARRAY,
                                    CLASS_TLIST, AS_EQUATIONS, parameters)
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)
    param = ['ConstantVoltage']
    addSciStringNode(equationsArrayNode, 1, param)

    param1 = ["p"]
    addSciStringNode(equationsArrayNode, 1, param1)
    param = ["n"]
    addSciStringNode(equationsArrayNode, 1, param)
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    scilabStringParameters = ["V"]
    addSciStringNode(innerArrayNode, height=1,
                     parameters=scilabStringParameters)
    innerNode = addArrayNode(innerArrayNode,
                             scilabClass="ScilabList")
    addScilabDoubleNode(innerNode, width=1, realParts=["5.0"])
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
