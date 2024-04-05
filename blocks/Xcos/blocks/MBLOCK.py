from common.AAAAAA import *

def MBLOCK(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MBLOCK'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'Ball_Platform', 'MODELICA',
                         func_name, BLOCKTYPE_C)

    # addExprsNode(outnode, TYPE_STRING, 0, parameters)
    arrayNode = addObjNode(outnode, TYPE_ARRAY, CLASS_TLIST, AS_EXPRS, parameters)
    scilabStringParameters = ["MBLOCK", "in",
                              "intype", "out",
                              "outtype", "param", "paramv", "pprop", "nameF", "funtxt"]
    addScilabStringNode(arrayNode, width=10,
                        parameters=scilabStringParameters)

    scilabStringParameters = [""]
    addScilabStringNode(arrayNode, width=1,
                        parameters=scilabStringParameters)

    scilabStringParameters = [""]
    addScilabStringNode(arrayNode, width=1,
                        parameters=scilabStringParameters)

    scilabStringParameters = [["y1", "y2"]]
    addScilabStringNode(arrayNode, width=1,
                        parameters=scilabStringParameters)

    scilabStringParameters = [["E", "E"]]
    addScilabStringNode(arrayNode, width=1,
                        parameters=scilabStringParameters)

    scilabStringParameters = [""]
    addScilabStringNode(arrayNode, width=1,
                        parameters=scilabStringParameters)

    addArrayNode(arrayNode, scilabClass="ScilabList")

    scilabStringParameters = [""]
    addScilabStringNode(arrayNode, width=1,
                        parameters=scilabStringParameters)

    scilabStringParameters = ["Ball_Platform"]
    addScilabStringNode(arrayNode, width=1,
                        parameters=scilabStringParameters)

    StrParam = ["class Ball_Platform", " parameter Real g=9.8; ",
                " parameter Real m1=0.50; //platformKg ",
                " parameter Real m2=0.30;//Kg",
                " parameter Real k=2; //Kg/sec",
                " Real y1(start=11),v1(start=0);//Platform",
                " Real y2(start=15),v2(start=1);//ball",
                " Real y0;", "", " discrete Real v1p,v2p;", "equation",
                " y0=10; //Nominal position", "//-----------------------------------",
                " der(y1)=v1;", " m1*der(v1)=if noEvent(v1<0.001 and v1>-0.001) then 0",
                " else -m1*g-k*(y1-y0)-0.2*v1;", " der(y2)=v2;",
                " der(v2)=if noEvent(v2<0.001 and v2>-0.001) then 0", " else -g;",
                "", "//-----------------------------------",
                " when y2<y1 then ", " v1p=(m1*v1+2*m2*v2-m2*v1)/(m1+m2);",
                " v2p=(m2*v2+2*m1*v1-m1*v2)/(m1+m2);",
                " reinit(v1,v1p*0.98);", " reinit(v2,v2p*0.98);", " end when;",
                "//-----------------------------------", "end Ball_Platform;"]
    addSciStringNode(arrayNode, height=29,
                        parameters=StrParam)

    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    # Create the outer Array node for equations
    equationsArrayNode = addArrayNode(outnode, scilabClass="ScilabTList",
                                      **{'as': 'equations'})

    # Add ScilabString nodes to equationsArrayNode
    scilabStringParameters = ["modelica", "model",
                              "inputs", "outputs",
                              "parameters"]
    addScilabStringNode(equationsArrayNode, width=5,
                        parameters=scilabStringParameters)

    scilabStringParameters = ["Ball_Platform"]
    addScilabStringNode(equationsArrayNode, width=1,
                        parameters=scilabStringParameters)

    addDataNode(equationsArrayNode, 'ScilabDouble',
                height=0, width=0)

    scilabStringParameters = ["y1", "y2"]
    addSciStringNode(equationsArrayNode, height=2,
                        parameters=scilabStringParameters)

    innerNode = addArrayNode(equationsArrayNode, scilabClass="ScilabList")

    addDataNode(innerNode, 'ScilabDouble',
                height=0, width=0)

    addArrayNode(innerNode, scilabClass="ScilabList")

    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    return outnode


def get_from_MBLOCK(cell):
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
