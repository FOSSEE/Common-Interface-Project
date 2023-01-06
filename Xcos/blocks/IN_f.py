def IN_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'IN_f'

    outnode = addNode(outroot, 'ExplicitInBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='input',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
