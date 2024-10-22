from common.AAAAAA import *


def CommandPort(outroot, attribid, parentattribid, ordering, geometry,
                value='', forSplitBlock=False):
    func_name = 'CommandPort'

    if forSplitBlock:
        outnode = addNode(outroot, func_name, connectable=0,
                          dataType='UNKNOW_TYPE', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, visible=0)
    else:
        outnode = addNode(outroot, func_name, initialState="-1.0",
                          dataType='UNKNOW_TYPE', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, value=value)

    return outnode


def addCommandPortForSplit(outroot, splitBlock, sourceVertex, targetVertex,
                           sourceType, targetType, inputCount,
                           outputCount, nextAttrib, nextAttribForSplit, waypoints):
    outputCount += 1
    geometry = {}
    geometry['width'] = 8
    geometry['height'] = 8
    geometry['x'] = 7
    geometry['y'] = -4
    CommandPort(outroot, nextAttrib, splitBlock, outputCount, geometry,
                forSplitBlock=True)
    nextAttrib += 1
    nextAttribForSplit += 1
    return (inputCount, outputCount, nextAttrib, nextAttribForSplit)
