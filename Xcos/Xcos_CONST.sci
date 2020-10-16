// list(1), list(), list(), list() = Xcos_CONST(5.2, list(), list(), list(), list(1), list())

function [explicit_output_vector, implicit_output_vector, command_vector, new_state_vector] = Xcos_CONST(output_fd, time, explicit_input_vector, implicit_input_vector, control_vector, block_parameters, state_vector)
    assert_checkequal(0, size(explicit_input_vector));
    assert_checkequal(0, size(implicit_input_vector));
    assert_checkequal(0, size(control_vector));
    assert_checkequal(1, size(block_parameters));

    value = block_parameters(1);

    explicit_output_vector = list(value)
    implicit_output_vector = list()
    command_vector = list()
    new_state_vector = list()
endfunction
