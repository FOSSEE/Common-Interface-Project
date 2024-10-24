from common.AAAAAA import *


def PNP(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'PNP'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'PNP', 'DEFAULT',
                         style, BLOCKTYPE_C,
                         dependsOnT='1')

    addExprsNode(outnode, TYPE_STRING, 17, parameters)
    addNodeScilabDB(outnode, AS_REAL_PARAM, height=17, realParts=[
                    format_real_number(parameters[0]), format_real_number(parameters[1]),
                    format_real_number(parameters[2]), format_real_number(parameters[3]),
                    format_real_number(parameters[4]), format_real_number(parameters[5]),
                    format_real_number(parameters[6]), format_real_number(parameters[7]),
                    format_real_number(parameters[8]), format_real_number(parameters[9]),
                    format_real_number(parameters[10]), format_real_number(parameters[11]),
                    format_real_number(parameters[12]), format_real_number(parameters[13]),
                    format_real_number(parameters[14]), format_real_number(parameters[15]),
                    format_real_number(parameters[16])])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)

    addNodeScilabDB(outnode, AS_NBZERO, height=1, realParts=[0.0])
    addNodeScilabDB(outnode, AS_NMODE, height=1, realParts=[0.0])
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

    additionalScilabStrings = ["PNP", "B"]
    for param in additionalScilabStrings:
        additionalStringNode = addDataNode(equationsArrayNode,
                                           'ScilabString',
                                           height=1, width=1)
        addDataData(additionalStringNode, param)

    additionalScilabStrings = ["C", "E"]
    additionalStringNode = addDataNode(equationsArrayNode,
                                       'ScilabString',
                                       height=2, width=1)
    for param in additionalScilabStrings:
        addDataData(additionalStringNode, param)

    innerArrayNode = addArrayNode(equationsArrayNode,
                                  scilabClass="ScilabList")

    param = ["Bf", "Br", "Is", "Vak", "Tauf", "Taur", "Ccs",
             "Cje", "Cjc", "Phie", "Me", "Phic", "Mc", "Gbc",
             "Gbe", "Vt", "EMinMax"]
    addSciStringNode(innerArrayNode, 17, param)

    addNodeScilabDouble(innerArrayNode, height=17, realParts=[
                        format_real_number(parameters[0]), format_real_number(parameters[1]),
                        format_real_number(parameters[2]), format_real_number(parameters[3]),
                        format_real_number(parameters[4]), format_real_number(parameters[5]),
                        format_real_number(parameters[6]), format_real_number(parameters[7]),
                        format_real_number(parameters[8]), format_real_number(parameters[9]),
                        format_real_number(parameters[10]), format_real_number(parameters[11]),
                        format_real_number(parameters[12]), format_real_number(parameters[13]),
                        format_real_number(parameters[14]), format_real_number(parameters[15]),
                        format_real_number(parameters[16])])

    para = [0.0 for _ in range(17)]
    addNodeScilabDouble(innerArrayNode, para, 17)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_PNP(cell):
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
