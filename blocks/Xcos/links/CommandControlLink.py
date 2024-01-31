from common.AAAAAA import *

def CommandControlLink(outroot, attribid, sourceVertex, targetVertex):
    func_name = 'CommandControlLink'

    outnode = addNode(outroot, func_name, **{'id': attribid},
                      parent=1, source=sourceVertex, target=targetVertex)

    addNode(outnode, 'mxGeometry', **{'as': 'geometry'})

    return outnode
