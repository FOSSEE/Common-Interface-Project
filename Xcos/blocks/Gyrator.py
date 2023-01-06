def Gyrator(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Gyrator'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnT=1,
                      blockType='c',
                      simulationFunctionName='Gyrator',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
