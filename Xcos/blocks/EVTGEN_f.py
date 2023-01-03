def EVTGEN_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EVTGEN_f'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='d',
                    ordering=ordering, parent=1,
                    simulationFunctionName='trash',
                    simulationFunctionType='DEFAULT',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'},height=1,width=1)

    for i in range(1):
        addDataData(node,parameters[i])
        
    return outnode

