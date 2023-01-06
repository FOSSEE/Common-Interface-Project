def STEP_FUNCTION(outroot, attribid, ordering, geometry, parameters):
    func_name = 'STEP_FUNCTION'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      blockType='c',
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    node = addExprsNode(outnode, 'ScilabDouble', 0, parameters)

    return outnode


def get_from_STEP_FUNCTION(cell):
    realParameters = cell.find('./Array[@as="realParameters"]')
    scilabList = realParameters.find('./Array[@scilabClass="ScilabList"]')
    scilabMList = scilabList.find('./Array[@scilabClass="ScilabMList"]')
    scilabMList2 = scilabMList.find('./Array[@scilabClass="ScilabMList"]')
    scilabString = scilabMList2.find('./ScilabString[@height="3"]')
    parameters = []
    display_parameter = ''
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)
    return (parameters, display_parameter)
