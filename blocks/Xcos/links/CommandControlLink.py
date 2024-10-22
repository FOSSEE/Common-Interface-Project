from common.AAAAAA import *


def CommandControlLink(outroot, attribid, sourceVertex, targetVertex, waypoints, parent=1):
    func_name = 'CommandControlLink'

    outnode = addNode(outroot, func_name, **{'id': attribid},
                      parent=parent, source=sourceVertex, target=targetVertex,
                      style=func_name, value='')

    mxGeoNode = addNode(outnode, 'mxGeometry', **{'as': 'geometry'})
    addNode(mxGeoNode, 'mxPoint', **{'as': 'sourcePoint', 'x': "0.0", 'y': "0.0"})
    arrayNode = addNode(mxGeoNode, 'Array', **{'as': 'points'})

    for point in waypoints:
        addNode(arrayNode, 'mxPoint', **{'x': point['x'], 'y': point['y']})

    addNode(mxGeoNode, 'mxPoint', **{'as': 'targetPoint', 'x': "0.0", 'y': "0.0"})

    return outnode
