from common.AAAAAA import *

def ImplicitLink(outroot, attribid, sourceVertex, targetVertex):
    func_name = 'ImplicitLink'

    outnode = addNode(outroot, func_name, **{'id': attribid},
                      parent=1, source=sourceVertex, target=targetVertex,
                      style=func_name, value='')

    mxGeoNode = addNode(outnode, 'mxGeometry', **{'as': 'geometry'})
    addNode(mxGeoNode, 'mxPoint', **{'as': 'sourcePoint', 'x': "0.0", 'y': "0.0"})
    addNode(mxGeoNode, 'mxPoint', **{'as': 'targetPoint', 'x': "0.0", 'y': "0.0"})

    return outnode
