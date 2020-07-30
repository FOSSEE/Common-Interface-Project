USE xcosblocks;

SET NAMES 'utf8';

DROP TABLE IF EXISTS blocks;
CREATE TABLE blocks (
    id int not null primary key auto_increment,
    name varchar(50) unique,
    initial_explicit_input_ports int,
    initial_implicit_input_ports int,
    initial_explicit_output_ports int,
    initial_implicit_output_ports int,
    initial_control_ports int,
    initial_command_ports int,
    initial_display_parameter varchar(100),
    variable_explicit_input_ports varchar(100),
    variable_implicit_input_ports varchar(100),
    variable_explicit_output_ports varchar(100),
    variable_implicit_output_ports varchar(100),
    variable_control_ports varchar(100),
    variable_command_ports varchar(100),
    variable_display_parameter varchar(100),
    p000 varchar(100),
    p001 varchar(100),
    p002 varchar(100),
    p003 varchar(100),
    p004 varchar(100),
    p005 varchar(100),
    p006 varchar(100),
    p007 varchar(100),
    p008 varchar(100),
    p009 varchar(100),
    p010 varchar(100),
    p011 varchar(100),
    p012 varchar(100),
    p013 varchar(100),
    p014 varchar(100),
    p015 varchar(100),
    p016 varchar(100),
    p017 varchar(100),
    p018 varchar(100),
    p019 varchar(100),
    p020 varchar(100),
    p021 varchar(100),
    p022 varchar(100),
    p023 varchar(100),
    p024 varchar(100),
    p025 varchar(100),
    p026 varchar(100),
    p027 varchar(100),
    p028 varchar(100),
    p029 varchar(100),
    p030 varchar(100),
    p031 varchar(100),
    p032 varchar(100),
    p033 varchar(100),
    p034 varchar(100),
    p035 varchar(100),
    p036 varchar(100),
    p037 varchar(100),
    p038 varchar(100),
    p039 varchar(100)
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'Xcos Categories - Xcos Blocks.csv'
    INTO TABLE blocks
    FIELDS TERMINATED BY ',' 
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (id, name,
    initial_explicit_input_ports, initial_implicit_input_ports,
    initial_explicit_output_ports, initial_implicit_output_ports,
    initial_control_ports, initial_command_ports,
    initial_display_parameter,
    variable_explicit_input_ports, variable_implicit_input_ports,
    variable_explicit_output_ports, variable_implicit_output_ports,
    variable_control_ports, variable_command_ports,
    variable_display_parameter,
    @tp000, @tp001,
    @tp002, @tp003,
    @tp004, @tp005,
    @tp006, @tp007,
    @tp008, @tp009,
    @tp010, @tp011,
    @tp012, @tp013,
    @tp014, @tp015,
    @tp016, @tp017,
    @tp018, @tp019)
    SET
    p000 = NULLIF(@tp000, ''), p001 = NULLIF(@tp001, ''),
    p002 = NULLIF(@tp002, ''), p003 = NULLIF(@tp003, ''),
    p004 = NULLIF(@tp004, ''), p005 = NULLIF(@tp005, ''),
    p006 = NULLIF(@tp006, ''), p007 = NULLIF(@tp007, ''),
    p008 = NULLIF(@tp008, ''), p009 = NULLIF(@tp009, ''),
    p010 = NULLIF(@tp010, ''), p011 = NULLIF(@tp011, ''),
    p012 = NULLIF(@tp012, ''), p013 = NULLIF(@tp013, ''),
    p014 = NULLIF(@tp014, ''), p015 = NULLIF(@tp015, ''),
    p016 = NULLIF(@tp016, ''), p017 = NULLIF(@tp017, ''),
    p018 = NULLIF(@tp018, ''), p019 = NULLIF(@tp019, '')
    ;

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id int not null primary key auto_increment,
    name varchar(100) unique,
    sort_order int not null
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'Xcos Categories - Xcos Categories.csv'
    INTO TABLE categories
    FIELDS TERMINATED BY ',' 
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (id, name, sort_order);

DROP TABLE IF EXISTS blockcategories;
CREATE TABLE blockcategories (
    id int not null primary key auto_increment,
    blockid int,
    blockname varchar(50),
    categoryid int,
    categoryname varchar(100),
    UNIQUE KEY(blockid, categoryid)
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'Xcos Categories - Categories and Blocks.csv'
    INTO TABLE blockcategories
    FIELDS TERMINATED BY ',' 
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (blockname, categoryname);

UPDATE blockcategories
INNER JOIN blocks ON blockname = blocks.name
INNER JOIN categories ON categoryname = categories.name
SET
blockid = blocks.id,
categoryid = categories.id;

ALTER TABLE blockcategories
ALTER COLUMN blockid int NOT NULL,
DROP COLUMN blockname,
ALTER COLUMN categoryid NOT NULL,
DROP COLUMN categoryname;
