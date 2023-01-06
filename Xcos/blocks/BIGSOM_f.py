def BIGSOM_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'BIGSOM_f'

    outnode = addNode(outroot, 'BigSom', dependsOnU=1, **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='sum',
                      simulationFunctionType='TYPE_2',
                      style=func_name,
                      blockType='c',
                      value='+')

    node = addExprsNode(outnode, 'ScilabString', 1, parameters)

    return outnode


def get_from_BIGSOM_f(cell):
    scilabString = cell.find('./ScilabString[@as="exprs"]')
    parameters = []
    display_parameter = ''
    for data in scilabString:
        value = data.attrib.get('value')
        parameters.append(value)
    return (parameters, display_parameter)
