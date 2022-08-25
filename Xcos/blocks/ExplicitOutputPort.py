def ExplicitOutputPort(outroot, attribid, parentattribid, ordering, value=''):
    func_name = 'ExplicitOutputPort'

    outnode = addNode(outroot, func_name, dataColumns=1, dataType='REAL_MATRIX',
        **{'id': attribid}, ordering=ordering, parent=parentattribid,
        style=func_name, value=value)

    node = addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
        height='8.0', width='8.0', x='100.0', y='160.0')

    return outnode
