def Diode(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Diode'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      dependsOnU=1,
                      blockType='c',
                      ordering=ordering, parent=1,
                      simulationFunctionName='Diode',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 4, parameters)

    return outnode
