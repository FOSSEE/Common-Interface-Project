from common.AAAAAA import *

def CBLOCK(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CBLOCK'

    if parameters[1] == 'y':
        type = 'IMPLICIT'
    else:
        type = 'EXPLICIT'

    simulation_func_type = 'DYNAMIC_' + type + '_4'

    if parameters[12] == 'y':
        depends_u = '1'
    else:
        depends_u = '0'

    if parameters[13] == 'y':
        depends_t = '1'
    else:
        depends_t = '0'

    code = parameters[14]
    codeLines = code.split('\n')

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, parameters[0], simulation_func_type,
                         func_name, BLOCKTYPE_C,
                         dependsOnU=depends_u,
                         dependsOnT=depends_t)

    addExprsArrayNode(outnode, TYPE_STRING, 14, parameters, codeLines)

    return outnode


def get_from_CBLOCK(cell):
    parameters = getParametersFromExprsNode(cell)

    display_parameter = parameters[0]

    eiv = ''
    iiv = ''
    con = 1 if parameters[4] != '[]' and int(float(parameters[4])) == 1 else 0
    eov = ''
    iov = ''
    com = 1 if parameters[5] != '[]' and int(float(parameters[5])) == 1 else 0

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
