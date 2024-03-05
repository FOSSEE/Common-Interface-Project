from common.AAAAAA import *

def Ground(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Ground'
    parameters = [""]
    outnode = addOutNode(outroot, BLOCK_GROUND,
                         attribid, ordering, 1,
                         func_name, 'Ground', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
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
    param = ['Ground']
    addSciStringNode(equationsArrayNode, 1, param)

    param1 = ["p"]
    addSciStringNode(equationsArrayNode, 1, param1)
    addScilabDBNode(equationsArrayNode, 0)
    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")
    addScilabDBNode(innerArrayNode, 0)
    addArrayNode(innerArrayNode, scilabClass="ScilabList")
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_Ground(cell):
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
