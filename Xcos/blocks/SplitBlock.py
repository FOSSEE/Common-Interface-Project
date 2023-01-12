def SplitBlock(outroot, attribid, ordering, geometry):
    outnode = addNode(outroot, BLOCK_SPLIT,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=None,
                      simulationFunctionName=None,
                      simulationFunctionType='DEFAULT',
                      style='',
                      blockType=None,
                      value='',
                      connectable=0,
                      vertex=1)

    addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
            height=geometry['height'], width=geometry['width'],
            x=geometry['x'], y=geometry['y'])

    return outnode


def get_from_SplitBlock(cell):
    parameters = []

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
