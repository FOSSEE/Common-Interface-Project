from common.AAAAAA import *

def SplitBlock(outroot, attribid, ordering, geometry):
    outnode = addOutNode(outroot, BLOCK_SPLIT,
                         attribid, ordering, 1,
                         None, None, 'DEFAULT',
                         '', None,
                         value='',
                         connectable=0,
                         vertex=1)
    addExprsNode(outnode, TYPE_DOUBLE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, [])
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS, [])
    addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
            height=geometry['height'], width=geometry['width'],
            x=geometry['x'], y=geometry['y'])

    return outnode


def get_from_SplitBlock(cell):
    parameters = []

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
