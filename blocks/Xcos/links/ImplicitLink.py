from common.AAAAAA import *

def ImplicitLink(outroot, attribid, sourceVertex, targetVertex):
    func_name = 'ImplicitLink'

    outnode = addNode(outroot, func_name, **{'id': attribid},
                      parent=1, source=sourceVertex, target=targetVertex)

    addNode(outnode, 'mxGeometry', **{'as': 'geometry'})

    return outnode
