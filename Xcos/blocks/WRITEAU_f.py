def WRITEAU_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'WRITEAU_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType='d',
                      dependsOnU=1,
                      simulationFunctionName='writeau',
                      simulationFunctionType='TYPE_2',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 2, parameters)

    return outnode
