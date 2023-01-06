def AFFICH_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'AFFICH_m'

    outnode = addNode(outroot, 'AfficheBlock', dependsOnU=1, **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1,
        simulationFunctionName='affich2', simulationFunctionType='C_OR_FORTRAN', style=func_name, blockType='c')

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=7, width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    addDataData(node, parameters[2])
    addDataData(node, parameters[3])
    addDataData(node, parameters[4])
    addDataData(node, parameters[5])
    addDataData(node, parameters[6])
    
    return outnode
