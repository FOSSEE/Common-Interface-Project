from common.AAAAAA import *

def Bache(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Bache'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'Bache', 'DEFAULT',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 9, parameters)
    addScilabDNode(outnode, AS_REAL_PARAM, width=9, realParts=[
                   format_real_number(parameters[0]),
                   format_real_number(parameters[1]),
                   format_real_number(parameters[2]),
                   format_real_number(parameters[3]),
                   format_real_number(parameters[4]),
                   format_real_number(parameters[5]),
                   format_real_number(parameters[6]),
                   format_real_number(parameters[7]),
                   format_real_number(parameters[8])
                   ])
    addScilabDNode(outnode, AS_INT_PARAM, width=0, realParts=[])           
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
    addDataData(additionalStringNode, "Bache")
    additionalScilabStrings = ["Ce1", "Ce2"]
    additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=2)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    additionalScilabStrings = ["Cs1", "Cs2", "yNiveau"]
    additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=3)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")

    param = ["Patm", "A", "ze1", "ze2", "zs1", "zs2", "z0", "T0", "p_rho"]
    addSciStringNode(equationsArrayNode, 9, param)
    # param1 = [parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7], parameters[8]]
    # addSciStringNode(equationsArrayNode, 9, param1)
    addNodeScilabDouble(equationsArrayNode, height=9, realParts=[
        format_real_number(parameters[0]),
        format_real_number(parameters[1]),
        format_real_number(parameters[2]),
        format_real_number(parameters[3]),
        format_real_number(parameters[4]),
        format_real_number(parameters[5]),
        format_real_number(parameters[6]),
        format_real_number(parameters[7]),
        format_real_number(parameters[8])])

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_Bache(cell):
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
