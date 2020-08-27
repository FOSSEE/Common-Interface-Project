USE xcosblocks;

SET NAMES 'utf8';

DROP TABLE IF EXISTS blocktypenames;
CREATE TABLE blocktypenames (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) UNIQUE
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'Xcos Categories - Xcos Datatypes.csv'
    INTO TABLE blocktypenames
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (id, name);

DROP TABLE IF EXISTS blocks;
CREATE TABLE blocks (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) UNIQUE,
    initial_explicit_input_ports int,
    initial_implicit_input_ports int,
    initial_explicit_output_ports int,
    initial_implicit_output_ports int,
    initial_control_ports int,
    initial_command_ports int,
    initial_display_parameter varchar(100)
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
    @variable_explicit_input_ports, @variable_implicit_input_ports,
    @variable_explicit_output_ports, @variable_implicit_output_ports,
    @variable_control_ports, @variable_command_ports,
    @variable_display_parameter,
    @tp000, @p000typename,
    @tp001, @p001typename,
    @tp002, @p002typename,
    @tp003, @p003typename,
    @tp004, @p004typename,
    @tp005, @p005typename,
    @tp006, @p006typename,
    @tp007, @p007typename,
    @tp008, @p008typename,
    @tp009, @p009typename,
    @tp010, @p010typename,
    @tp011, @p011typename,
    @tp012, @p012typename,
    @tp013, @p013typename,
    @tp014, @p014typename,
    @tp015, @p015typename,
    @tp016, @p016typename,
    @tp017, @p017typename,
    @tp018, @p018typename,
    @tp019, @p019typename);

DROP TABLE IF EXISTS blockparameters;
CREATE TABLE blockparameters (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    block_id int UNIQUE,
    block_name varchar(100) UNIQUE,
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
    INTO TABLE blockparameters
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (id, block_name,
    @initial_explicit_input_ports, @initial_implicit_input_ports,
    @initial_explicit_output_ports, @initial_implicit_output_ports,
    @initial_control_ports, @initial_command_ports,
    @initial_display_parameter,
    @variable_explicit_input_ports, @variable_implicit_input_ports,
    @variable_explicit_output_ports, @variable_implicit_output_ports,
    @variable_control_ports, @variable_command_ports,
    @variable_display_parameter,
    @tp000, p000typename,
    @tp001, p001typename,
    @tp002, p002typename,
    @tp003, p003typename,
    @tp004, p004typename,
    @tp005, p005typename,
    @tp006, p006typename,
    @tp007, p007typename,
    @tp008, p008typename,
    @tp009, p009typename,
    @tp010, p010typename,
    @tp011, p011typename,
    @tp012, p012typename,
    @tp013, p013typename,
    @tp014, p014typename,
    @tp015, p015typename,
    @tp016, p016typename,
    @tp017, p017typename,
    @tp018, p018typename,
    @tp019, p019typename)
    SET p000 = NULLIF(@tp000, ''),
        p001 = NULLIF(@tp001, ''),
        p002 = NULLIF(@tp002, ''),
        p003 = NULLIF(@tp003, ''),
        p004 = NULLIF(@tp004, ''),
        p005 = NULLIF(@tp005, ''),
        p006 = NULLIF(@tp006, ''),
        p007 = NULLIF(@tp007, ''),
        p008 = NULLIF(@tp008, ''),
        p009 = NULLIF(@tp009, ''),
        p010 = NULLIF(@tp010, ''),
        p011 = NULLIF(@tp011, ''),
        p012 = NULLIF(@tp012, ''),
        p013 = NULLIF(@tp013, ''),
        p014 = NULLIF(@tp014, ''),
        p015 = NULLIF(@tp015, ''),
        p016 = NULLIF(@tp016, ''),
        p017 = NULLIF(@tp017, ''),
        p018 = NULLIF(@tp018, ''),
        p019 = NULLIF(@tp019, '');

UPDATE blockparameters
INNER JOIN blocks ON block_name = blocks.name
    SET block_id = blocks.id;

UPDATE blockparameters
INNER JOIN blocktypenames ON p000typename = blocktypenames.name
    SET p000typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p001typename = blocktypenames.name
    SET p001typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p002typename = blocktypenames.name
    SET p002typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p003typename = blocktypenames.name
    SET p003typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p004typename = blocktypenames.name
    SET p004typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p005typename = blocktypenames.name
    SET p005typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p006typename = blocktypenames.name
    SET p006typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p007typename = blocktypenames.name
    SET p007typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p008typename = blocktypenames.name
    SET p008typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p009typename = blocktypenames.name
    SET p009typeid = blocktypenames.id;

UPDATE blockparameters
INNER JOIN blocktypenames ON p010typename = blocktypenames.name
    SET p010typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p011typename = blocktypenames.name
    SET p011typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p012typename = blocktypenames.name
    SET p012typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p013typename = blocktypenames.name
    SET p013typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p014typename = blocktypenames.name
    SET p014typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p015typename = blocktypenames.name
    SET p015typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p016typename = blocktypenames.name
    SET p016typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p017typename = blocktypenames.name
    SET p017typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p018typename = blocktypenames.name
    SET p018typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p019typename = blocktypenames.name
    SET p019typeid = blocktypenames.id;

UPDATE blockparameters
INNER JOIN blocktypenames ON p020typename = blocktypenames.name
    SET p020typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p021typename = blocktypenames.name
    SET p021typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p022typename = blocktypenames.name
    SET p022typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p023typename = blocktypenames.name
    SET p023typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p024typename = blocktypenames.name
    SET p024typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p025typename = blocktypenames.name
    SET p025typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p026typename = blocktypenames.name
    SET p026typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p027typename = blocktypenames.name
    SET p027typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p028typename = blocktypenames.name
    SET p028typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p029typename = blocktypenames.name
    SET p029typeid = blocktypenames.id;

UPDATE blockparameters
INNER JOIN blocktypenames ON p030typename = blocktypenames.name
    SET p030typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p031typename = blocktypenames.name
    SET p031typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p032typename = blocktypenames.name
    SET p032typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p033typename = blocktypenames.name
    SET p033typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p034typename = blocktypenames.name
    SET p034typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p035typename = blocktypenames.name
    SET p035typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p036typename = blocktypenames.name
    SET p036typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p037typename = blocktypenames.name
    SET p037typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p038typename = blocktypenames.name
    SET p038typeid = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p039typename = blocktypenames.name
    SET p039typeid = blocktypenames.id;

SELECT block_name, p000, p000typeid, p000typename
FROM blockparameters
    WHERE (p000 IS NULL AND p000typeid IS NOT NULL) OR (p000 IS NOT NULL AND p000typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p001, p001typeid, p001typename
FROM blockparameters
    WHERE (p001 IS NULL AND p001typeid IS NOT NULL) OR (p001 IS NOT NULL AND p001typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p002, p002typeid, p002typename
FROM blockparameters
    WHERE (p002 IS NULL AND p002typeid IS NOT NULL) OR (p002 IS NOT NULL AND p002typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p003, p003typeid, p003typename
FROM blockparameters
    WHERE (p003 IS NULL AND p003typeid IS NOT NULL) OR (p003 IS NOT NULL AND p003typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p004, p004typeid, p004typename
FROM blockparameters
    WHERE (p004 IS NULL AND p004typeid IS NOT NULL) OR (p004 IS NOT NULL AND p004typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p005, p005typeid, p005typename
FROM blockparameters
    WHERE (p005 IS NULL AND p005typeid IS NOT NULL) OR (p005 IS NOT NULL AND p005typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p006, p006typeid, p006typename
FROM blockparameters
    WHERE (p006 IS NULL AND p006typeid IS NOT NULL) OR (p006 IS NOT NULL AND p006typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p007, p007typeid, p007typename
FROM blockparameters
    WHERE (p007 IS NULL AND p007typeid IS NOT NULL) OR (p007 IS NOT NULL AND p007typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p008, p008typeid, p008typename
FROM blockparameters
    WHERE (p008 IS NULL AND p008typeid IS NOT NULL) OR (p008 IS NOT NULL AND p008typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p009, p009typeid, p009typename
FROM blockparameters
    WHERE (p009 IS NULL AND p009typeid IS NOT NULL) OR (p009 IS NOT NULL AND p009typeid IS NULL)
    ORDER BY 1
    LIMIT 5;

SELECT block_name, p010, p010typeid, p010typename
FROM blockparameters
    WHERE (p010 IS NULL AND p010typeid IS NOT NULL) OR (p010 IS NOT NULL AND p010typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p011, p011typeid, p011typename
FROM blockparameters
    WHERE (p011 IS NULL AND p011typeid IS NOT NULL) OR (p011 IS NOT NULL AND p011typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p012, p012typeid, p012typename
FROM blockparameters
    WHERE (p012 IS NULL AND p012typeid IS NOT NULL) OR (p012 IS NOT NULL AND p012typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p013, p013typeid, p013typename
FROM blockparameters
    WHERE (p013 IS NULL AND p013typeid IS NOT NULL) OR (p013 IS NOT NULL AND p013typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p014, p014typeid, p014typename
FROM blockparameters
    WHERE (p014 IS NULL AND p014typeid IS NOT NULL) OR (p014 IS NOT NULL AND p014typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p015, p015typeid, p015typename
FROM blockparameters
    WHERE (p015 IS NULL AND p015typeid IS NOT NULL) OR (p015 IS NOT NULL AND p015typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p016, p016typeid, p016typename
FROM blockparameters
    WHERE (p016 IS NULL AND p016typeid IS NOT NULL) OR (p016 IS NOT NULL AND p016typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p017, p017typeid, p017typename
FROM blockparameters
    WHERE (p017 IS NULL AND p017typeid IS NOT NULL) OR (p017 IS NOT NULL AND p017typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p018, p018typeid, p018typename
FROM blockparameters
    WHERE (p018 IS NULL AND p018typeid IS NOT NULL) OR (p018 IS NOT NULL AND p018typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p019, p019typeid, p019typename
FROM blockparameters
    WHERE (p019 IS NULL AND p019typeid IS NOT NULL) OR (p019 IS NOT NULL AND p009typeid IS NULL)
    ORDER BY 1
    LIMIT 5;

SELECT block_name, p020, p020typeid, p020typename
FROM blockparameters
    WHERE (p020 IS NULL AND p020typeid IS NOT NULL) OR (p020 IS NOT NULL AND p020typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p021, p021typeid, p021typename
FROM blockparameters
    WHERE (p021 IS NULL AND p021typeid IS NOT NULL) OR (p021 IS NOT NULL AND p021typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p022, p022typeid, p022typename
FROM blockparameters
    WHERE (p022 IS NULL AND p022typeid IS NOT NULL) OR (p022 IS NOT NULL AND p022typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p023, p023typeid, p023typename
FROM blockparameters
    WHERE (p023 IS NULL AND p023typeid IS NOT NULL) OR (p023 IS NOT NULL AND p023typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p024, p024typeid, p024typename
FROM blockparameters
    WHERE (p024 IS NULL AND p024typeid IS NOT NULL) OR (p024 IS NOT NULL AND p024typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p025, p025typeid, p025typename
FROM blockparameters
    WHERE (p025 IS NULL AND p025typeid IS NOT NULL) OR (p025 IS NOT NULL AND p025typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p026, p026typeid, p026typename
FROM blockparameters
    WHERE (p026 IS NULL AND p026typeid IS NOT NULL) OR (p026 IS NOT NULL AND p026typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p027, p027typeid, p027typename
FROM blockparameters
    WHERE (p027 IS NULL AND p027typeid IS NOT NULL) OR (p027 IS NOT NULL AND p027typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p028, p028typeid, p028typename
FROM blockparameters
    WHERE (p028 IS NULL AND p028typeid IS NOT NULL) OR (p028 IS NOT NULL AND p028typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p029, p029typeid, p029typename
FROM blockparameters
    WHERE (p029 IS NULL AND p029typeid IS NOT NULL) OR (p029 IS NOT NULL AND p029typeid IS NULL)
    ORDER BY 1
    LIMIT 5;

SELECT block_name, p030, p030typeid, p030typename
FROM blockparameters
    WHERE (p030 IS NULL AND p030typeid IS NOT NULL) OR (p030 IS NOT NULL AND p030typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p031, p031typeid, p031typename
FROM blockparameters
    WHERE (p031 IS NULL AND p031typeid IS NOT NULL) OR (p031 IS NOT NULL AND p031typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p032, p032typeid, p032typename
FROM blockparameters
    WHERE (p032 IS NULL AND p032typeid IS NOT NULL) OR (p032 IS NOT NULL AND p032typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p033, p033typeid, p033typename
FROM blockparameters
    WHERE (p033 IS NULL AND p033typeid IS NOT NULL) OR (p033 IS NOT NULL AND p033typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p034, p034typeid, p034typename
FROM blockparameters
    WHERE (p034 IS NULL AND p034typeid IS NOT NULL) OR (p034 IS NOT NULL AND p034typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p035, p035typeid, p035typename
FROM blockparameters
    WHERE (p035 IS NULL AND p035typeid IS NOT NULL) OR (p035 IS NOT NULL AND p035typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p036, p036typeid, p036typename
FROM blockparameters
    WHERE (p036 IS NULL AND p036typeid IS NOT NULL) OR (p036 IS NOT NULL AND p036typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p037, p037typeid, p037typename
FROM blockparameters
    WHERE (p037 IS NULL AND p037typeid IS NOT NULL) OR (p037 IS NOT NULL AND p037typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p038, p038typeid, p038typename
FROM blockparameters
    WHERE (p038 IS NULL AND p038typeid IS NOT NULL) OR (p038 IS NOT NULL AND p038typeid IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p039, p039typeid, p039typename
FROM blockparameters
    WHERE (p039 IS NULL AND p039typeid IS NOT NULL) OR (p039 IS NOT NULL AND p039typeid IS NULL)
    ORDER BY 1
    LIMIT 5;

ALTER TABLE blockparameters
    DROP COLUMN block_name,
    DROP COLUMN p000typename,
    DROP COLUMN p001typename,
    DROP COLUMN p002typename,
    DROP COLUMN p003typename,
    DROP COLUMN p004typename,
    DROP COLUMN p005typename,
    DROP COLUMN p006typename,
    DROP COLUMN p007typename,
    DROP COLUMN p008typename,
    DROP COLUMN p009typename,
    DROP COLUMN p010typename,
    DROP COLUMN p011typename,
    DROP COLUMN p012typename,
    DROP COLUMN p013typename,
    DROP COLUMN p014typename,
    DROP COLUMN p015typename,
    DROP COLUMN p016typename,
    DROP COLUMN p017typename,
    DROP COLUMN p018typename,
    DROP COLUMN p019typename,
    DROP COLUMN p020typename,
    DROP COLUMN p021typename,
    DROP COLUMN p022typename,
    DROP COLUMN p023typename,
    DROP COLUMN p024typename,
    DROP COLUMN p025typename,
    DROP COLUMN p026typename,
    DROP COLUMN p027typename,
    DROP COLUMN p028typename,
    DROP COLUMN p029typename,
    DROP COLUMN p030typename,
    DROP COLUMN p031typename,
    DROP COLUMN p032typename,
    DROP COLUMN p033typename,
    DROP COLUMN p034typename,
    DROP COLUMN p035typename,
    DROP COLUMN p036typename,
    DROP COLUMN p037typename,
    DROP COLUMN p038typename,
    DROP COLUMN p039typename;

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) UNIQUE,
    sort_order int NOT NULL
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
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    categoryid int,
    categoryname varchar(100),
    blockid int,
    blockname varchar(100),
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
    SET categoryid = categories.id,
        blockid = blocks.id;

ALTER TABLE blockcategories
    MODIFY COLUMN categoryid int NOT NULL,
    DROP COLUMN categoryname,
    MODIFY COLUMN blockid int NOT NULL,
    DROP COLUMN blockname;
