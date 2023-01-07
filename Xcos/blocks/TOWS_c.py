def TOWS_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'TOWS_c'

    para3 = int(parameters[2])

    b_type = ''
    if para3 == 1:
        b_type = 'x'
    else:
        b_type = 'd'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      parent=1,
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType=b_type,
                      simulationFunctionName='tows_c',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
