def ImplicitOutputPort(outroot, attribid, parentattribid, ordering, geometry,
                       addDataLines=False, value='', forSplitBlock=False):
    func_name = 'ImplicitOutputPort'

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
