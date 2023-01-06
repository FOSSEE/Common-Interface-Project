def TCLSS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TCLSS'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='c',
                      dependsOnT=1,
                      simulationFunctionName='tcslti4',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 5, parameters)

    return outnode
