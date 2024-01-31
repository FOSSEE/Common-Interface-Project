from common.AAAAAA import *

def ExplicitLink(outroot, attribid, sourceVertex, targetVertex):
    func_name = 'ExplicitLink'

    outnode = addNode(outroot, func_name, **{'id': attribid},
                      parent=1, source=sourceVertex, target=targetVertex)

    addNode(outnode, 'mxGeometry', **{'as': 'geometry'})

    return outnode
