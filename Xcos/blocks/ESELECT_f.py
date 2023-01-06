def ESELECT_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ESELECT_f'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      blockType='l',
                      simulationFunctionName='eselect',
                      simulationFunctionType='ESELECT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
