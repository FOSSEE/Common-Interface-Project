def BOUNCEXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BOUNCEXY'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='bouncexy',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='d')

    node = addExprsNode(outnode, 'ScilabString', 8, parameters)

    return outnode
