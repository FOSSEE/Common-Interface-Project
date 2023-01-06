def fortran_block(outroot, attribid, ordering, geometry, parameters):
    func_name = 'fortran_block'

    code = parameters[4]
    codeLines = code.split('\n')

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='c',
                      simulationFunctionName=parameters[3],
                      simulationFunctionType='DYNAMIC_FORTRAN_1',
                      style=func_name)

    node = addExprsArrayNode(outnode, 'ScilabString', 4, parameters, codeLines)

    return outnode
