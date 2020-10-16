// list(), list(), list(1), list(5.2) = Xcos_CLOCK_c(5.2, list(), list(), list(), list(0.1, 0.1), list(5.1))

function [explicit_output_vector, implicit_output_vector, command_vector, new_state_vector] = Xcos_CLOCK_c(output_fd, time, explicit_input_vector, implicit_input_vector, control_vector, block_parameters, state_vector)
    assert_checkequal(0, size(explicit_input_vector));
    assert_checkequal(0, size(implicit_input_vector));
    assert_checkequal(0, size(control_vector));
    assert_checkequal(2, size(block_parameters));

    if size(state_vector) == 0 then
        state_vector = list(0);
    end

    time_difference = block_parameters(1);
    minimum_time = block_parameters(2);
    last_time =  state_vector(1);
    if time < minimum_time then
        next_state = 0;
    elseif (time - last_time) < time_difference then
        next_state = 0;
    else
        next_state = 1;
    end

    explicit_output_vector = list()
    implicit_output_vector = list()
    command_vector = list(next_state)
    new_state_vector = list(time)
endfunction
