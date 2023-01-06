def CSCOPXY3D(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPXY3D'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='d',
                      simulationFunctionName='cscopxy3d',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabString', 11, parameters)

    return outnode
