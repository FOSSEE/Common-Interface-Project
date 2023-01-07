def ExplicitInputPort(outroot, attribid, parentattribid, ordering, geometry,
                      addDataLines=False, value='', forSplitBlock=False):
    func_name = 'ExplicitInputPort'

    if forSplitBlock:
        outnode = addNode(outroot, func_name, connectable=0, dataType='UNKNOW_TYPE',
                          **{'id': attribid}, ordering=ordering, parent=parentattribid,
                          style=func_name, visible=0)
    elif addDataLines:
        outnode = addNode(outroot, func_name, dataColumns=1, dataLines=1,
                          dataType='REAL_MATRIX', **{'id': attribid}, ordering=ordering,
                          parent=parentattribid, style=func_name, value=value)
    else:
        outnode = addNode(outroot, func_name, dataColumns=1, dataType='REAL_MATRIX',
                          **{'id': attribid}, ordering=ordering, parent=parentattribid,
                          style=func_name, value=value)

    node = addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
                   height=geometry['height'], width=geometry['width'],
                   x=geometry['x'], y=geometry['y'])

    return outnode


def addExplicitInputPortForSplit(outroot, splitBlock, sourceVertex, targetVertex,
                                 sourceType, targetType, edgeDict, inputCount,
                                 outputCount, nextAttrib, nextAttribForSplit):
    inputCount += 1
    geometry = {}
    geometry['width'] = 8
    geometry['height'] = 8
    geometry['x'] = -8
    geometry['y'] = -4
    ExplicitInputPort(outroot, nextAttrib, splitBlock, inputCount, geometry,
                      forSplitBlock=True)
    edgeDict[nextAttribForSplit] = ('ExplicitLink', sourceVertex, nextAttrib,
                                    sourceType, 'ExplicitInputPort')
    nextAttrib += 1
    nextAttribForSplit += 1
    return (inputCount, outputCount, nextAttrib, nextAttribForSplit)
