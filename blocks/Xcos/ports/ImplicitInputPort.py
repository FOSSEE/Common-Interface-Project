from common.AAAAAA import *


def ImplicitInputPort(outroot, attribid, parentattribid, ordering, geometry,
                      addDataLines=False, value='', forSplitBlock=False):
    func_name = 'ImplicitInputPort'

    if forSplitBlock:
        outnode = addNode(outroot, func_name, connectable=0,
                          dataType='UNKNOW_TYPE', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, visible=0)
    elif addDataLines:
        outnode = addNode(outroot, func_name, **{'id': attribid},
                          parent=parentattribid, ordering=ordering,
                          dataType='REAL_MATRIX', dataColumns=1,
                          dataLines=1, style=func_name,
                          value=value)
    else:
        outnode = addNode(outroot, func_name, **{'id': attribid},
                          parent=parentattribid, ordering=ordering,
                          dataType='REAL_MATRIX', dataColumns=1,
                          initialState="-1.0", style=func_name,
                          value=value)

    return outnode


def addImplicitInputPortForSplit(outroot, splitBlock, sourceVertex, targetVertex,
                                 sourceType, targetType, inputCount,
                                 outputCount, nextAttrib, nextAttribForSplit, waypoints):
    inputCount += 1
    geometry = {}
    geometry['width'] = 8
    geometry['height'] = 8
    geometry['x'] = -8
    geometry['y'] = -4
    ImplicitInputPort(outroot, nextAttrib, splitBlock, inputCount, geometry,
                      forSplitBlock=True)
    nextAttrib += 1
    nextAttribForSplit += 1
    return (inputCount, outputCount, nextAttrib, nextAttribForSplit)
