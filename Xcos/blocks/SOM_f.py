def SOM_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SOM_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='cscope',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 0, parameters)

    return outnode
