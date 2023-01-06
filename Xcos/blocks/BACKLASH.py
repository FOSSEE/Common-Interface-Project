def BACKLASH(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BACKLASH'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      dependsOnU=1,
                      simulationFunctionName='backlash',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    node = addExprsNode(outnode, 'ScilabString', 3, parameters)

    return outnode
