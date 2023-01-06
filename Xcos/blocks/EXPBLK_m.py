def EXPBLK_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXPBLK_m'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='c',
                      dependsOnU=1,
                      ordering=ordering, parent=1,
                      simulationFunctionName='expblk_m',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
