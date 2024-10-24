from common.AAAAAA import *


def scifunc_block_m(outroot, attribid, ordering, geometry, parameters, parent=1, style=None):
    func_name = 'scifunc_block_m'
    if style is None:
        style = func_name

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, parent,
                         func_name, 'cscope', 'C_OR_FORTRAN',
                         style, BLOCKTYPE_C)

    ArrayNode = addObjNode(outnode, TYPE_ARRAY,
                           CLASS_LIST, AS_EXPRS, parameters)
    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=9, width=1)
    for param in parameters:
        addDataData(additionalStringNode, param)
    innerarray = addArrayNode(ArrayNode, scilabClass="ScilabList")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "y1=locus2(u1)")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "xd=[]")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(innerarray,
                                       'ScilabString',
                                       height=2, width=1)
    addDataData(additionalStringNode, " ")
    addDataData(additionalStringNode, "y1=[]")

    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])

    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_INT_PARAM, 1, array)

    ArrayNode = addObjNode(outnode, TYPE_ARRAY,
                           CLASS_LIST, AS_OBJ_PARAM, parameters)
    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "y1=locus2(u1)")

    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, "xd=[]")

    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=1, width=1)
    addDataData(additionalStringNode, " ")

    additionalStringNode = addDataNode(ArrayNode,
                                       'ScilabString',
                                       height=2, width=1)
    addDataData(additionalStringNode, " ")
    addDataData(additionalStringNode, "y1=[]")

    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    # Create the outer Array node for equations
    addArrayNode(outnode, scilabClass="ScilabList",
                 **{'as': 'equations'})
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_scifunc_block_m(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = parameters[10]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
