USE xcosblocks;

SET NAMES 'utf8';

DROP TABLE IF EXISTS blocktypenames;
CREATE TABLE blocktypenames (
    id int not null primary key auto_increment,
    name varchar(100) unique
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'Xcos Categories - Xcos Blocks.csv'
    INTO TABLE blocks
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (id, name);

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
    p000typeid int,
    p000typename varchar(100),
    p001 varchar(100),
    p001typeid int,
    p001typename varchar(100),
    p002 varchar(100),
    p002typeid int,
    p002typename varchar(100),
    p003 varchar(100),
    p003typeid int,
    p003typename varchar(100),
    p004 varchar(100),
    p004typeid int,
    p004typename varchar(100),
    p005 varchar(100),
    p005typeid int,
    p005typename varchar(100),
    p006 varchar(100),
    p006typeid int,
    p006typename varchar(100),
    p007 varchar(100),
    p007typeid int,
    p007typename varchar(100),
    p008 varchar(100),
    p008typeid int,
    p008typename varchar(100),
    p009 varchar(100),
    p009typeid int,
    p009typename varchar(100),
    p010 varchar(100),
    p010typeid int,
    p010typename varchar(100),
    p011 varchar(100),
    p011typeid int,
    p011typename varchar(100),
    p012 varchar(100),
    p012typeid int,
    p012typename varchar(100),
    p013 varchar(100),
    p013typeid int,
    p013typename varchar(100),
    p014 varchar(100),
    p014typeid int,
    p014typename varchar(100),
    p015 varchar(100),
    p015typeid int,
    p015typename varchar(100),
    p016 varchar(100),
    p016typeid int,
    p016typename varchar(100),
    p017 varchar(100),
    p017typeid int,
    p017typename varchar(100),
    p018 varchar(100),
    p018typeid int,
    p018typename varchar(100),
    p019 varchar(100),
    p019typeid int,
    p019typename varchar(100),
    p020 varchar(100),
    p020typeid int,
    p020typename varchar(100),
    p021 varchar(100),
    p021typeid int,
    p021typename varchar(100),
    p022 varchar(100),
    p022typeid int,
    p022typename varchar(100),
    p023 varchar(100),
    p023typeid int,
    p023typename varchar(100),
    p024 varchar(100),
    p024typeid int,
    p024typename varchar(100),
    p025 varchar(100),
    p025typeid int,
    p025typename varchar(100),
    p026 varchar(100),
    p026typeid int,
    p026typename varchar(100),
    p027 varchar(100),
    p027typeid int,
    p027typename varchar(100),
    p028 varchar(100),
    p028typeid int,
    p028typename varchar(100),
    p029 varchar(100),
    p029typeid int,
    p029typename varchar(100),
    p030 varchar(100),
    p030typeid int,
    p030typename varchar(100),
    p031 varchar(100),
    p031typeid int,
    p031typename varchar(100),
    p032 varchar(100),
    p032typeid int,
    p032typename varchar(100),
    p033 varchar(100),
    p033typeid int,
    p033typename varchar(100),
    p034 varchar(100),
    p034typeid int,
    p034typename varchar(100),
    p035 varchar(100),
    p035typeid int,
    p035typename varchar(100),
    p036 varchar(100),
    p036typeid int,
    p036typename varchar(100),
    p037 varchar(100),
    p037typeid int,
    p037typename varchar(100),
    p038 varchar(100),
    p038typeid int,
    p038typename varchar(100),
    p039 varchar(100),
    p039typeid int,
    p039typename varchar(100)
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
    @tp000, @tp000typename,
    @tp001, @tp001typename,
    @tp002, @tp002typename,
    @tp003, @tp003typename,
    @tp004, @tp004typename,
    @tp005, @tp005typename,
    @tp006, @tp006typename,
    @tp007, @tp007typename,
    @tp008, @tp008typename,
    @tp009, @tp009typename,
    @tp010, @tp010typename,
    @tp011, @tp011typename,
    @tp012, @tp012typename,
    @tp013, @tp013typename,
    @tp014, @tp014typename,
    @tp015, @tp015typename,
    @tp016, @tp016typename,
    @tp017, @tp017typename,
    @tp018, @tp018typename,
    @tp019, @tp019typename)
    SET
    p000 = NULLIF(@tp000, ''), p000typename = NULLIF(@tp000typename, ''),
    p001 = NULLIF(@tp001, ''), p001typename = NULLIF(@tp001typename, ''),
    p002 = NULLIF(@tp002, ''), p002typename = NULLIF(@tp002typename, ''),
    p003 = NULLIF(@tp003, ''), p003typename = NULLIF(@tp003typename, ''),
    p004 = NULLIF(@tp004, ''), p004typename = NULLIF(@tp004typename, ''),
    p005 = NULLIF(@tp005, ''), p005typename = NULLIF(@tp005typename, ''),
    p006 = NULLIF(@tp006, ''), p006typename = NULLIF(@tp006typename, ''),
    p007 = NULLIF(@tp007, ''), p007typename = NULLIF(@tp007typename, ''),
    p008 = NULLIF(@tp008, ''), p008typename = NULLIF(@tp008typename, ''),
    p009 = NULLIF(@tp009, ''), p009typename = NULLIF(@tp009typename, ''),
    p010 = NULLIF(@tp010, ''), p010typename = NULLIF(@tp010typename, ''),
    p011 = NULLIF(@tp011, ''), p011typename = NULLIF(@tp011typename, ''),
    p012 = NULLIF(@tp012, ''), p012typename = NULLIF(@tp012typename, ''),
    p013 = NULLIF(@tp013, ''), p013typename = NULLIF(@tp013typename, ''),
    p014 = NULLIF(@tp014, ''), p014typename = NULLIF(@tp014typename, ''),
    p015 = NULLIF(@tp015, ''), p015typename = NULLIF(@tp015typename, ''),
    p016 = NULLIF(@tp016, ''), p016typename = NULLIF(@tp016typename, ''),
    p017 = NULLIF(@tp017, ''), p017typename = NULLIF(@tp017typename, ''),
    p018 = NULLIF(@tp018, ''), p018typename = NULLIF(@tp018typename, ''),
    p019 = NULLIF(@tp019, ''), p019typename = NULLIF(@tp019typename, '');

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
    IGNORE 2 ROWS
    (id, name, sort_order);

DROP TABLE IF EXISTS blockcategories;
CREATE TABLE blockcategories (
    id int not null primary key auto_increment,
    categoryid int,
    categoryname varchar(100),
    blockid int,
    blockname varchar(50),
    CONSTRAINT categoryblock UNIQUE(categoryid, blockid)
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'Xcos Categories - Categories and Blocks.csv'
    INTO TABLE blockcategories
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (categoryname, blockname);

UPDATE blockcategories
INNER JOIN categories ON categoryname = categories.name
INNER JOIN blocks ON blockname = blocks.name
SET
categoryid = categories.id,
blockid = blocks.id;

ALTER TABLE blockcategories
MODIFY COLUMN categoryid int NOT NULL,
DROP COLUMN categoryname,
MODIFY COLUMN blockid int NOT NULL,
DROP COLUMN blockname;
