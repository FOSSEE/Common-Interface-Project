def Bache(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Bache'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      simulationFunctionName='Bache',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='c')

    node = addExprsNode(outnode, 'ScilabString', 9, parameters)

    return outnode
