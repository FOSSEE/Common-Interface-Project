def ControlPort(outroot, attribid, parentattribid, ordering, value=''):
    func_name = 'ControlPort'

    outnode = addNode(outroot, func_name, dataType='UNKNOW_TYPE',
        **{'id': attribid}, ordering=ordering, parent=parentattribid,
        style=func_name)

    node = addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
        height='8.0', width='8.0', x='100.0', y='160.0')

    return outnode
