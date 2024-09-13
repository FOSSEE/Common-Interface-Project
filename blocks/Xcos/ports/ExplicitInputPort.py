from common.AAAAAA import *

def ExplicitInputPort(outroot, attribid, parentattribid, ordering, geometry,
                      addDataLines=False, value='', forSplitBlock=False):
    func_name = 'ExplicitInputPort'

    if forSplitBlock:
        outnode = addNode(outroot, func_name, connectable=0,
                          dataType='UNKNOW_TYPE', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, visible=0)
    elif addDataLines:
        outnode = addNode(outroot, func_name, dataColumns=1, dataLines=1,
                          dataType='REAL_MATRIX', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, value=value)
    else:
        outnode = addNode(outroot, func_name, dataColumns=1,
                          initialState="-1.0", dataType='REAL_MATRIX',
                          **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, value=value)

    return outnode


def addExplicitInputPortForSplit(outroot, splitBlock, sourceVertex, targetVertex,
                                 sourceType, targetType, edgeDict, inputCount,
                                 outputCount, nextAttrib, nextAttribForSplit, arrayelem):
    inputCount += 1
    geometry = {}
    geometry['width'] = 8
    geometry['height'] = 8
    geometry['x'] = -8
    geometry['y'] = -4
    ExplicitInputPort(outroot, nextAttrib, splitBlock, inputCount, geometry,
                      forSplitBlock=True)
    edgeDict[nextAttribForSplit] = ('ExplicitLink', str(sourceVertex), str(nextAttrib),
                                    sourceType, 'ExplicitInputPort', arrayelem)
    nextAttrib += 1
    nextAttribForSplit += 1
    return (inputCount, outputCount, nextAttrib, nextAttribForSplit)
