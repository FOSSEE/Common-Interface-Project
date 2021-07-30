#!/usr/bin/awk -f

BEGIN {
    FS = "\t";
    BLOCKPORTSCSVFORMAT = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n";
    STDERR = "/dev/stderr";
    BLOCKPORTSCSV = "data/blocks-ports.csv";

    blockportid = 0;
    port_part = 1;
    port_dmg = 1;
}

{
    category = $1;
    block = $2;
    explicit_input_ports = $3;
    implicit_input_ports = $4;
    explicit_output_ports = $5;
    implicit_output_ports = $6;
    command_ports = $7;
    control_ports = $8;
    block_width = $9;
    block_height = $10;

    port_order = 0;

    input_ports = explicit_input_ports + implicit_input_ports;

    for (i = 0; i < explicit_input_ports; i++) {
        ++port_order;
        port_x = 0;
        port_y = int(block_height * (i + 0.5) / input_ports + 0.5);
        port_orientation = "ExplicitInputPort";
        port_type = "ExplicitInputPort";
        printf BLOCKPORTSCSVFORMAT, ++blockportid, category, block, port_order, port_order, port_order, port_x, port_y, port_orientation, port_part, port_dmg, port_type > BLOCKPORTSCSV;
    }

    for (i = 0; i < implicit_input_ports; i++) {
        ++port_order;
        port_x = 0;
        port_y = int(block_height * (explicit_input_ports + i + 0.5) / input_ports + 0.5);
        port_orientation = "ImplicitInputPort";
        port_type = "ImplicitInputPort";
        printf BLOCKPORTSCSVFORMAT, ++blockportid, category, block, port_order, port_order, port_order, port_x, port_y, port_orientation, port_part, port_dmg, port_type > BLOCKPORTSCSV;
    }

    output_ports = explicit_output_ports + implicit_output_ports;

    for (i = 0; i < explicit_output_ports; i++) {
        ++port_order;
        port_x = block_width;
        port_y = int(block_height * (i + 0.5) / output_ports + 0.5);
        port_orientation = "ExplicitOutputPort";
        port_type = "ExplicitOutputPort";
        printf BLOCKPORTSCSVFORMAT, ++blockportid, category, block, port_order, port_order, port_order, port_x, port_y, port_orientation, port_part, port_dmg, port_type > BLOCKPORTSCSV;
    }

    for (i = 0; i < implicit_output_ports; i++) {
        ++port_order;
        port_x = block_width;
        port_y = int(block_height * (explicit_output_ports + i + 0.5) / output_ports + 0.5);
        port_orientation = "ImplicitOutputPort";
        port_type = "ImplicitOutputPort";
        printf BLOCKPORTSCSVFORMAT, ++blockportid, category, block, port_order, port_order, port_order, port_x, port_y, port_orientation, port_part, port_dmg, port_type > BLOCKPORTSCSV;
    }

    for (i = 0; i < command_ports; i++) {
        ++port_order;
        port_x = int(block_width * (i + 0.5) / command_ports + 0.5);
        port_y = 0;
        port_orientation = "CommandPort";
        port_type = "CommandPort";
        printf BLOCKPORTSCSVFORMAT, ++blockportid, category, block, port_order, port_order, port_order, port_x, port_y, port_orientation, port_part, port_dmg, port_type > BLOCKPORTSCSV;
    }

    for (i = 0; i < control_ports; i++) {
        ++port_order;
        port_x = int(block_width * (i + 0.5) / control_ports + 0.5);
        port_y = block_height;
        port_orientation = "ControlPort";
        port_type = "ControlPort";
        printf BLOCKPORTSCSVFORMAT, ++blockportid, category, block, port_order, port_order, port_order, port_x, port_y, port_orientation, port_part, port_dmg, port_type > BLOCKPORTSCSV;
    }
}
