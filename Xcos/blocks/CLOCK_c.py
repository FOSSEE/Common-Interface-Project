def CLOCK_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLOCK_c'

    outnode = addNode(outroot, 'BasicBlock', blockType='h', **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1,
        simulationFunctionName='csuper', simulationFunctionType='DEFAULT', style=func_name)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'exprs'}, height=0, width=0)

    return outnode

def get_from_CLOCK_c(cell):
    realParameters = cell.find('./Array[@as="realParameters"]')
    scilabList = realParameters.find('./Array[@scilabClass="ScilabList"]')
    scilabMLists = scilabList.findall('./Array[@scilabClass="ScilabMList"]')
    scilabMList2 = scilabMLists[1].find('./Array[@scilabClass="ScilabMList"]')
    scilabString = scilabMList2.find('./ScilabString[@height="2"]')
    parameters = []
    display_parameter = ''
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)
    return (parameters, display_parameter)
