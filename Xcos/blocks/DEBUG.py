def DEBUG(outroot, attribid, ordering, geometry, parameters):
    func_name = 'DEBUG'

    code = parameters[0]
    codeLines = code.split('\n')

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='d',
                      ordering=ordering, parent=1,
                      simulationFunctionName='%debug_scicos',
                      simulationFunctionType=func_name,
                      style=func_name)

    node = addExprsArrayNode(outnode, 'ScilabString', 1, [''], codeLines)

    return outnode
