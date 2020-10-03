// list(), list(), list(), list() = Xcos_AFFICH_m(5.2, list(1), list(), list(1), list([1, 1], 1, 1, 1, 5, 1, 0), list(1))
// list(), list(), list(), list() = Xcos_AFFICH_m(5.2, list(1), list(), list(), list([1, 1], 1, 1, 1, 5, 1, 1), list(1))

function [explicit_output_vector, implicit_output_vector, command_vector, new_state_vector] = Xcos_AFFICH_m(time, explicit_input_vector, implicit_input_vector, control_vector, block_parameters, state_vector)
    assert_checkequal(1, size(explicit_input_vector));
    assert_checkequal(0, size(implicit_input_vector));
    assert_checkequal(7, size(block_parameters));
    inherit = block_parameters(7);
    if inherit ~= 0 then
        control_ports = 0;
    else
        control_ports = 1;
    end
    assert_checkequal(control_ports, size(control_vector));

    if size(state_vector) == 0 then
        state_vector = list(0);
    end

    last_time =  state_vector(1);
    if inherit ~= 0 then
        control = 1;
        if time < minimum_time then
            next_state = 0;
        elseif (time - last_time) < time_difference then
            next_state = 0;
        else
            next_state = 1;
        end
    else
        control = control_vector(1);
    end

    if control == 1 then
        value = explicit_input_vector(1);
    else
        value = state_vector(1);
    end

    explicit_output_vector = list()
    implicit_output_vector = list()
    command_vector = list()
    new_state_vector = list(time)
endfunction
