select XC.name CN, XB.name BN, initial_explicit_input_ports EI, initial_implicit_input_ports II, initial_explicit_output_ports EO, initial_implicit_output_ports IO, initial_command_ports CM, initial_control_ports CN, block_width BW, block_height BH
    from xcosblocks_block XB
    join xcosblocks_category XC on XC.id = main_category_id
    order by XB.id;
