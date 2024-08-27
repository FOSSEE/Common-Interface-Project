from common.AAAAAA import *

def ExplicitLink(outroot, attribid, sourceVertex, targetVertex, arrayelem):
    func_name = 'ExplicitLink'

    outnode = addNode(outroot, func_name, **{'id': attribid},
                      parent=1, source=sourceVertex, target=targetVertex,
                      style=func_name, value='')

    # print(arrayelem)
    mxGeoNode = addNode(outnode, 'mxGeometry', **{'as': 'geometry'})
    addNode(mxGeoNode, 'mxPoint', **{'as': 'sourcePoint', 'x': "0.0", 'y': "0.0"})

    arrayNode = addNode(mxGeoNode, 'Array', **{'as': 'points'})

    for point in arrayelem:
        addNode(arrayNode, 'mxPoint', **{'x': point['x'], 'y': point['y']})

    addNode(mxGeoNode, 'mxPoint', **{'as': 'targetPoint', 'x': "0.0", 'y': "0.0"})

    return outnode
