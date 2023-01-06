def CLKINV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKINV_f'

    outnode = addNode(outroot, 'EventInBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='input',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode
