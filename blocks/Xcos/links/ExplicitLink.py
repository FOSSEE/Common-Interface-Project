from common.AAAAAA import *

def ExplicitLink(outroot, attribid, sourceVertex, targetVertex):
    func_name = 'ExplicitLink'

    outnode = addNode(outroot, func_name, **{'id': attribid},
                      parent=1, source=sourceVertex, target=targetVertex,
                      style=func_name, value='')

    mxGeoNode = addNode(outnode, 'mxGeometry', **{'as': 'geometry'})
    addNode(mxGeoNode, 'mxPoint', **{'as': 'sourcePoint', 'x': "0.0", 'y': "0.0"})
    addNode(mxGeoNode, 'Array', **{'as': 'points'})
    addNode(mxGeoNode, 'mxPoint', **{'as': 'targetPoint', 'x': "0.0", 'y': "0.0"})

    return outnode
