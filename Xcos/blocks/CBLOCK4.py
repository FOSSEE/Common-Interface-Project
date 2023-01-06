def CBLOCK4(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CBLOCK4'

    type = ''
    if parameters[1] == 'y':
        type = 'IMPLICIT'
    else:
        type = 'EXPLICIT'

    depends_t = 0
    if parameters[18] == 'y':
        depends_t = 1
    else:
        depends_t = 0

    depends_u = 0
    if parameters[17] == 'y':
        depends_u = 1
    else:
        depends_u = 0

    simulation_func_type = 'DYNAMIC_' + type + '_4'

    code = parameters[19]
    codeLines = code.split('\n')

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=depends_u,
                      dependsOnT=depends_t,
                      blockType='c',
                      simulationFunctionName=parameters[0],
                      simulationFunctionType=simulation_func_type,
                      style=func_name)

    node = addExprsArrayNode(outnode, 'ScilabString', 19, parameters, codeLines)

    return outnode
