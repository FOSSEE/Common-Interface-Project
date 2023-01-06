def DELAY_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DELAY_f'

    outnode = addNode(outroot, 'BasicBlock',
                      **{'id': attribid},
                    interfaceFunctionName=func_name,
                    blockType='h',
                    ordering=ordering, parent=1,
                    simulationFunctionName='csuper',
                    simulationFunctionType='DEFAULT',
                    style=func_name
                      )

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'exprs'},height=0,width=0)

    return outnode
