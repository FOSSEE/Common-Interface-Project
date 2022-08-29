def SplitBlock(outroot, attribid, ordering, geometry):
    func_name = 'SplitBlock'

    outnode = addNode(outroot, func_name, **{'id': attribid},
        ordering=ordering, parent=1,
        simulationFunctionType='DEFAULT')

    node = addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
        height=geometry['height'], width=geometry['width'], x=geometry['x'], y=geometry['y'])

    return outnode


