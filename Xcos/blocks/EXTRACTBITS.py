def EXTRACTBITS(outroot, attribid, ordering, geometry, parameters):
    func_name = 'EXTRACTBITS'
    
    d_type = ['UH','LH','MSB','LSB','RB']
    type1 = ['32','16','8','u32','u16','u8']
    type2 = ['32','16','8','32','16','8']
    bits_extract = ''
    bit_int = ''
    
    para1 = int(float(parameters[0]))
    para2 = int(float(parameters[1]))
    para4 = int(float(parameters[3]))
    if para2==2 or para2==4:
        bits_extract = type2[para1-3] + '_' + d_type[para2-1]
    else:
        if para4 == 0:
            bits_extract = type2[para1-3] + '_' + d_type[para2-1]
            
        else:
            bits_extract = type1[para1-3] + '_' + d_type[para2-1]

        bit_int = str(para4)
    
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        dependsOnU=1,
        blockType='c',
        simulationFunctionName='extract_bit_' + bits_extract + bit_int,
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=4, width=1)
    
    for i in range(4):
        addDataData(node, parameters[i])
    
    return outnode

