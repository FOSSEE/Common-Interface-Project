def CEVENTSCOPE(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CEVENTSCOPE'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='cevscpe',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 6, parameters)

    return outnode
