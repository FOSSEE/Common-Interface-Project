def CLSS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLSS'

    depends_u = 1
    if int(float(parameters[3])) == 0:
        depends_u = 0

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnT=1,
                      dependsOnU=depends_u,
                      blockType='c',
                      simulationFunctionName='csslti4',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 5, parameters)

    return outnode
