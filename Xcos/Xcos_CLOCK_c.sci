// [], [], [1], [5.2] = Xcos_CLOCK_c(5.2, [], [], [], [0.1, 0.1], [5.1])

function explicit_output_vector, implicit_output_vector, command_vector, new_state_vector = Xcos_CLOCK_c(time, explicit_input_vector, implicit_input_vector, control_vector, block_parameters, state_vector)
    assert_checkequal(0, size(explicit_input_vector, 2));
    assert_checkequal(0, size(implicit_input_vector, 2));
    assert_checkequal(2, size(control_vector, 2));

    last_time = size(state_vector, 2) > 0 ? state_vector(1) : 0;
    next_state = (time < minimum_time) ? 0 : (time - last_time) > time_difference ? 1 : 0;

    explicit_output_vector = []
    implicit_output_vector = []
    command_vector = [next_state]
    new_state_vector = [time]

endfunction




