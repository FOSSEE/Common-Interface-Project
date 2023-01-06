def DEBUG(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEBUG'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='d',
                    ordering=ordering, parent=1,
                    simulationFunctionName='%debug_scicos',
                    simulationFunctionType=func_name,
                    style=func_name
                      )

    node = addNode(outnode, 'Array', **{'as': 'exprs'},scilabClass='ScilabList')
    n_node = addDataNode(node,'ScilabString',height=1,width=1)
    addDataData(n_node,'')
    nn_node = addDataNode(node,'ScilabString',height=1,width=1)
    addDataData(nn_node,parameters[0])

    return outnode
