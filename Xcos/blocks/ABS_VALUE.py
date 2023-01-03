def ABS_VALUE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ABS_VALUE'

    outnode = addNode(outroot, 'BasicBlock', dependsOnU=1, **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1, 
        simulationFunctionName='absolute_value', simulationFunctionType='C_OR_FORTRAN', style=func_name, blockType='c')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=1, width=1)
    addDataData(node, parameters[0])

    return outnode
