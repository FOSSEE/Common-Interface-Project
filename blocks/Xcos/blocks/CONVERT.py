from common.AAAAAA import *

def CONVERT(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CONVERT'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'convert', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_CONVERT(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    types = ['decim.', 'decim.', 'int32', 'int16',
             'int8', 'uint32', 'uint16', 'uint8']
    input_t = int(float(parameters[0]))
    output_t = int(float(parameters[1]))

    input_type = types[input_t-1]
    output_type = types[output_t-1]

    display_parameter = input_type + ',' + output_type

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
