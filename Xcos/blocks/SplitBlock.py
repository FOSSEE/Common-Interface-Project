def SplitBlock(outroot, attribid, ordering, geometry):
    func_name = 'SplitBlock'

    outnode = addNode(outroot, func_name, connectable=0, **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      simulationFunctionType='DEFAULT',
                      style='',
                      value='',
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
