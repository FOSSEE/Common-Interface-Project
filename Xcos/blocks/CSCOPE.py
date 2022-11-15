def CSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPE'

    outnode = addNode(outroot, 'BasicBlock', dependsOnU=1, **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1,
        simulationFunctionName='cscope', simulationFunctionType='C_OR_FORTRAN', style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=10, width=1)
    addDataData(node, '1 3 5 7 9 11 13 15')
    addDataData(node, '-1')
    addDataData(node, '[]')
    addDataData(node, '[600;400]')
    addDataData(node, parameters[4])
    addDataData(node, parameters[5])
    addDataData(node, '30')
    addDataData(node, '20')
    addDataData(node, '0')
    addDataData(node, '')

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'realParameters'}, height=4, width=1)
    addDataData(node, 0.0)
    addDataData(node, parameters[4], True)
    addDataData(node, parameters[5], True)
    addDataData(node, 30.0)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'integerParameters'}, height=15, width=1)
    addDataData(node, -1.0)
    addDataData(node, 1.0)
    addDataData(node, 20.0)
    addDataData(node, 1.0)
    addDataData(node, 3.0)
    addDataData(node, 5.0)
    addDataData(node, 7.0)
    addDataData(node, 9.0)
    addDataData(node, 11.0)
    addDataData(node, 13.0)
    addDataData(node, 15.0)
    addDataData(node, -1.0)
    addDataData(node, -1.0)
    addDataData(node, 600.0)
    addDataData(node, 400.0)

    node = addNode(outnode, 'Array', **{'as': 'objectsParameters'},
        scilabClass='ScilabList')

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'nbZerosCrossing'}, height=1, width=1)
    addDataData(node, 0.0)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'nmode'}, height=1, width=1)
    addDataData(node, 0.0)

    node = addNode(outnode, 'Array', **{'as': 'oDState'},
        scilabClass='ScilabList')

    node = addNode(outnode, 'Array', **{'as': 'equations'},
        scilabClass='ScilabList')

    node = addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
        height=geometry['height'], width=geometry['width'], x=geometry['x'], y=geometry['y'])

    return outnode

def get_from_CSCOPE(cell):
    scilabString = cell.find('./ScilabString[@as="exprs"]')
    parameters = []
    display_parameter = ''
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)
    return (parameters, display_parameter)
