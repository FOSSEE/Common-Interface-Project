from common.AAAAAA import *


def ImplicitOutputPort(outroot, attribid, parentattribid, ordering, geometry,
                       addDataLines=False, value='', forSplitBlock=False):
    func_name = 'ImplicitOutputPort'

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


def addImplicitOutputPortForSplit(outroot, splitBlock, sourceVertex, targetVertex,
                                  sourceType, targetType, inputCount,
                                  outputCount, nextAttrib, nextAttribForSplit, waypoints):
    outputCount += 1
    geometry = {}
    geometry['width'] = 8
    geometry['height'] = 8
    geometry['x'] = 7
    geometry['y'] = -4
    ImplicitOutputPort(outroot, nextAttrib, splitBlock, outputCount, geometry,
                       forSplitBlock=True)
    nextAttrib += 1
    nextAttribForSplit += 1
    return (inputCount, outputCount, nextAttrib, nextAttribForSplit)
