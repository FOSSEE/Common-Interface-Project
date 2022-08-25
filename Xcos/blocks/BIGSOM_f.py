def BIGSOM_f(outroot, attribid, ordering):
    func_name = 'BIGSOM_f'

    outnode = addNode(outroot, 'BigSom', dependsOnU=1, **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1,
        simulationFunctionName='sum', simulationFunctionType='TYPE_2', style=func_name,
        value='+')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
    addDataData(node, '[1;-1]')

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'realParameters'}, height=2, width=1)
    addDataData(node, 1.0)
    addDataData(node, -1.0)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'integerParameters'}, height=0, width=0)

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
        height='60.0', width='40.0', x='200.0', y='160.0')
