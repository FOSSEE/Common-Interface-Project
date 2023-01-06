def AFFICH_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AFFICH_m'

    outnode = addNode(outroot, 'AfficheBlock', dependsOnU=1, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='affich2',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c')

    node = addExprsNode(outnode, 'ScilabString', 7, parameters)

    return outnode
