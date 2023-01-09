def CommandPort(outroot, attribid, parentattribid, ordering, geometry,
                value='', forSplitBlock=False):
    func_name = 'CommandPort'

    if forSplitBlock:
        outnode = addNode(outroot, func_name, connectable=0,
                          dataType='UNKNOW_TYPE', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, visible=0)
    else:
        outnode = addNode(outroot, func_name,
                          dataType='UNKNOW_TYPE', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, value=value)

    node = addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
                   height=geometry['height'], width=geometry['width'],
                   x=geometry['x'], y=geometry['y'])

    return outnode
