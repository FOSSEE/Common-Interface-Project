CREATE DATABASE IF NOT EXISTS esimblocks DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_bin;

USE esimblocks;

SET NAMES 'utf8' COLLATE 'utf8_bin';

DROP TABLE IF EXISTS blocktypenames;
CREATE TABLE blocktypenames (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) UNIQUE
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'eSimBlockTypenames.csv'
    INTO TABLE blocktypenames
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (id, name);

DROP TABLE IF EXISTS blocks;
CREATE TABLE blocks (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) UNIQUE
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'eSimBlocks.csv'
    INTO TABLE blocks
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (name);

DROP TABLE IF EXISTS blockports;
CREATE TABLE blockports (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    block_id int,
    block_name varchar(100) NOT NULL,
    port_order int NOT NULL,
    port_name varchar(100),
    port_number int,
    port_type varchar(100),
    port_orientation varchar(100),
    CONSTRAINT blockports_block_id_port_order UNIQUE(block_id, port_order),
    CONSTRAINT blockports_block_name_port_order UNIQUE(block_name, port_order)
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'eSimBlockPorts.csv'
    INTO TABLE blockports
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (block_name,
    port_order, port_name,
    port_number, port_type,
    port_orientation);

UPDATE blockports
INNER JOIN blocks ON block_name = blocks.name
    SET block_id = blocks.id;

SELECT block_name
FROM blockports
    WHERE block_id IS NULL
    ORDER BY 1
    LIMIT 5;

ALTER TABLE blockports
    MODIFY COLUMN block_id int NOT NULL,
    DROP INDEX blockports_block_name_port_order,
    DROP COLUMN block_name;

DROP TABLE IF EXISTS blockparameters;
CREATE TABLE blockparameters (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    block_id int UNIQUE,
    block_name varchar(100) UNIQUE,
    p000 varchar(100),
    p000_type_id int,
    p000_type_name varchar(100),
    p001 varchar(100),
    p001_type_id int,
    p001_type_name varchar(100),
    p002 varchar(100),
    p002_type_id int,
    p002_type_name varchar(100),
    p003 varchar(100),
    p003_type_id int,
    p003_type_name varchar(100),
    p004 varchar(100),
    p004_type_id int,
    p004_type_name varchar(100),
    p005 varchar(100),
    p005_type_id int,
    p005_type_name varchar(100),
    p006 varchar(100),
    p006_type_id int,
    p006_type_name varchar(100),
    p007 varchar(100),
    p007_type_id int,
    p007_type_name varchar(100),
    p008 varchar(100),
    p008_type_id int,
    p008_type_name varchar(100),
    p009 varchar(100),
    p009_type_id int,
    p009_type_name varchar(100),
    p010 varchar(100),
    p010_type_id int,
    p010_type_name varchar(100),
    p011 varchar(100),
    p011_type_id int,
    p011_type_name varchar(100),
    p012 varchar(100),
    p012_type_id int,
    p012_type_name varchar(100),
    p013 varchar(100),
    p013_type_id int,
    p013_type_name varchar(100),
    p014 varchar(100),
    p014_type_id int,
    p014_type_name varchar(100),
    p015 varchar(100),
    p015_type_id int,
    p015_type_name varchar(100),
    p016 varchar(100),
    p016_type_id int,
    p016_type_name varchar(100),
    p017 varchar(100),
    p017_type_id int,
    p017_type_name varchar(100),
    p018 varchar(100),
    p018_type_id int,
    p018_type_name varchar(100),
    p019 varchar(100),
    p019_type_id int,
    p019_type_name varchar(100),
    p020 varchar(100),
    p020_type_id int,
    p020_type_name varchar(100),
    p021 varchar(100),
    p021_type_id int,
    p021_type_name varchar(100),
    p022 varchar(100),
    p022_type_id int,
    p022_type_name varchar(100),
    p023 varchar(100),
    p023_type_id int,
    p023_type_name varchar(100),
    p024 varchar(100),
    p024_type_id int,
    p024_type_name varchar(100),
    p025 varchar(100),
    p025_type_id int,
    p025_type_name varchar(100),
    p026 varchar(100),
    p026_type_id int,
    p026_type_name varchar(100),
    p027 varchar(100),
    p027_type_id int,
    p027_type_name varchar(100),
    p028 varchar(100),
    p028_type_id int,
    p028_type_name varchar(100),
    p029 varchar(100),
    p029_type_id int,
    p029_type_name varchar(100),
    p030 varchar(100),
    p030_type_id int,
    p030_type_name varchar(100),
    p031 varchar(100),
    p031_type_id int,
    p031_type_name varchar(100),
    p032 varchar(100),
    p032_type_id int,
    p032_type_name varchar(100),
    p033 varchar(100),
    p033_type_id int,
    p033_type_name varchar(100),
    p034 varchar(100),
    p034_type_id int,
    p034_type_name varchar(100),
    p035 varchar(100),
    p035_type_id int,
    p035_type_name varchar(100),
    p036 varchar(100),
    p036_type_id int,
    p036_type_name varchar(100),
    p037 varchar(100),
    p037_type_id int,
    p037_type_name varchar(100),
    p038 varchar(100),
    p038_type_id int,
    p038_type_name varchar(100),
    p039 varchar(100),
    p039_type_id int,
    p039_type_name varchar(100)
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'eSimBlockParameters.csv'
    INTO TABLE blockparameters
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (id, block_name,
    @tp000, p000_type_name,
    @tp001, p001_type_name,
    @tp002, p002_type_name,
    @tp003, p003_type_name,
    @tp004, p004_type_name,
    @tp005, p005_type_name,
    @tp006, p006_type_name,
    @tp007, p007_type_name,
    @tp008, p008_type_name,
    @tp009, p009_type_name,
    @tp010, p010_type_name,
    @tp011, p011_type_name,
    @tp012, p012_type_name,
    @tp013, p013_type_name,
    @tp014, p014_type_name,
    @tp015, p015_type_name,
    @tp016, p016_type_name,
    @tp017, p017_type_name,
    @tp018, p018_type_name,
    @tp019, p019_type_name)
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
INNER JOIN blocktypenames ON p000_type_name = blocktypenames.name
    SET p000_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p001_type_name = blocktypenames.name
    SET p001_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p002_type_name = blocktypenames.name
    SET p002_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p003_type_name = blocktypenames.name
    SET p003_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p004_type_name = blocktypenames.name
    SET p004_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p005_type_name = blocktypenames.name
    SET p005_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p006_type_name = blocktypenames.name
    SET p006_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p007_type_name = blocktypenames.name
    SET p007_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p008_type_name = blocktypenames.name
    SET p008_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p009_type_name = blocktypenames.name
    SET p009_type_id = blocktypenames.id;

UPDATE blockparameters
INNER JOIN blocktypenames ON p010_type_name = blocktypenames.name
    SET p010_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p011_type_name = blocktypenames.name
    SET p011_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p012_type_name = blocktypenames.name
    SET p012_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p013_type_name = blocktypenames.name
    SET p013_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p014_type_name = blocktypenames.name
    SET p014_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p015_type_name = blocktypenames.name
    SET p015_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p016_type_name = blocktypenames.name
    SET p016_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p017_type_name = blocktypenames.name
    SET p017_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p018_type_name = blocktypenames.name
    SET p018_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p019_type_name = blocktypenames.name
    SET p019_type_id = blocktypenames.id;

UPDATE blockparameters
INNER JOIN blocktypenames ON p020_type_name = blocktypenames.name
    SET p020_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p021_type_name = blocktypenames.name
    SET p021_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p022_type_name = blocktypenames.name
    SET p022_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p023_type_name = blocktypenames.name
    SET p023_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p024_type_name = blocktypenames.name
    SET p024_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p025_type_name = blocktypenames.name
    SET p025_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p026_type_name = blocktypenames.name
    SET p026_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p027_type_name = blocktypenames.name
    SET p027_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p028_type_name = blocktypenames.name
    SET p028_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p029_type_name = blocktypenames.name
    SET p029_type_id = blocktypenames.id;

UPDATE blockparameters
INNER JOIN blocktypenames ON p030_type_name = blocktypenames.name
    SET p030_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p031_type_name = blocktypenames.name
    SET p031_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p032_type_name = blocktypenames.name
    SET p032_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p033_type_name = blocktypenames.name
    SET p033_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p034_type_name = blocktypenames.name
    SET p034_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p035_type_name = blocktypenames.name
    SET p035_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p036_type_name = blocktypenames.name
    SET p036_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p037_type_name = blocktypenames.name
    SET p037_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p038_type_name = blocktypenames.name
    SET p038_type_id = blocktypenames.id;
UPDATE blockparameters
INNER JOIN blocktypenames ON p039_type_name = blocktypenames.name
    SET p039_type_id = blocktypenames.id;

SELECT block_name, p000, p000_type_id, p000_type_name
FROM blockparameters
    WHERE (p000 IS NULL AND p000_type_id IS NOT NULL) OR (p000 IS NOT NULL AND p000_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p001, p001_type_id, p001_type_name
FROM blockparameters
    WHERE (p001 IS NULL AND p001_type_id IS NOT NULL) OR (p001 IS NOT NULL AND p001_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p002, p002_type_id, p002_type_name
FROM blockparameters
    WHERE (p002 IS NULL AND p002_type_id IS NOT NULL) OR (p002 IS NOT NULL AND p002_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p003, p003_type_id, p003_type_name
FROM blockparameters
    WHERE (p003 IS NULL AND p003_type_id IS NOT NULL) OR (p003 IS NOT NULL AND p003_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p004, p004_type_id, p004_type_name
FROM blockparameters
    WHERE (p004 IS NULL AND p004_type_id IS NOT NULL) OR (p004 IS NOT NULL AND p004_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p005, p005_type_id, p005_type_name
FROM blockparameters
    WHERE (p005 IS NULL AND p005_type_id IS NOT NULL) OR (p005 IS NOT NULL AND p005_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p006, p006_type_id, p006_type_name
FROM blockparameters
    WHERE (p006 IS NULL AND p006_type_id IS NOT NULL) OR (p006 IS NOT NULL AND p006_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p007, p007_type_id, p007_type_name
FROM blockparameters
    WHERE (p007 IS NULL AND p007_type_id IS NOT NULL) OR (p007 IS NOT NULL AND p007_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p008, p008_type_id, p008_type_name
FROM blockparameters
    WHERE (p008 IS NULL AND p008_type_id IS NOT NULL) OR (p008 IS NOT NULL AND p008_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p009, p009_type_id, p009_type_name
FROM blockparameters
    WHERE (p009 IS NULL AND p009_type_id IS NOT NULL) OR (p009 IS NOT NULL AND p009_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;

SELECT block_name, p010, p010_type_id, p010_type_name
FROM blockparameters
    WHERE (p010 IS NULL AND p010_type_id IS NOT NULL) OR (p010 IS NOT NULL AND p010_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p011, p011_type_id, p011_type_name
FROM blockparameters
    WHERE (p011 IS NULL AND p011_type_id IS NOT NULL) OR (p011 IS NOT NULL AND p011_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p012, p012_type_id, p012_type_name
FROM blockparameters
    WHERE (p012 IS NULL AND p012_type_id IS NOT NULL) OR (p012 IS NOT NULL AND p012_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p013, p013_type_id, p013_type_name
FROM blockparameters
    WHERE (p013 IS NULL AND p013_type_id IS NOT NULL) OR (p013 IS NOT NULL AND p013_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p014, p014_type_id, p014_type_name
FROM blockparameters
    WHERE (p014 IS NULL AND p014_type_id IS NOT NULL) OR (p014 IS NOT NULL AND p014_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p015, p015_type_id, p015_type_name
FROM blockparameters
    WHERE (p015 IS NULL AND p015_type_id IS NOT NULL) OR (p015 IS NOT NULL AND p015_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p016, p016_type_id, p016_type_name
FROM blockparameters
    WHERE (p016 IS NULL AND p016_type_id IS NOT NULL) OR (p016 IS NOT NULL AND p016_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p017, p017_type_id, p017_type_name
FROM blockparameters
    WHERE (p017 IS NULL AND p017_type_id IS NOT NULL) OR (p017 IS NOT NULL AND p017_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p018, p018_type_id, p018_type_name
FROM blockparameters
    WHERE (p018 IS NULL AND p018_type_id IS NOT NULL) OR (p018 IS NOT NULL AND p018_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p019, p019_type_id, p019_type_name
FROM blockparameters
    WHERE (p019 IS NULL AND p019_type_id IS NOT NULL) OR (p019 IS NOT NULL AND p009_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;

SELECT block_name, p020, p020_type_id, p020_type_name
FROM blockparameters
    WHERE (p020 IS NULL AND p020_type_id IS NOT NULL) OR (p020 IS NOT NULL AND p020_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p021, p021_type_id, p021_type_name
FROM blockparameters
    WHERE (p021 IS NULL AND p021_type_id IS NOT NULL) OR (p021 IS NOT NULL AND p021_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p022, p022_type_id, p022_type_name
FROM blockparameters
    WHERE (p022 IS NULL AND p022_type_id IS NOT NULL) OR (p022 IS NOT NULL AND p022_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p023, p023_type_id, p023_type_name
FROM blockparameters
    WHERE (p023 IS NULL AND p023_type_id IS NOT NULL) OR (p023 IS NOT NULL AND p023_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p024, p024_type_id, p024_type_name
FROM blockparameters
    WHERE (p024 IS NULL AND p024_type_id IS NOT NULL) OR (p024 IS NOT NULL AND p024_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p025, p025_type_id, p025_type_name
FROM blockparameters
    WHERE (p025 IS NULL AND p025_type_id IS NOT NULL) OR (p025 IS NOT NULL AND p025_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p026, p026_type_id, p026_type_name
FROM blockparameters
    WHERE (p026 IS NULL AND p026_type_id IS NOT NULL) OR (p026 IS NOT NULL AND p026_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p027, p027_type_id, p027_type_name
FROM blockparameters
    WHERE (p027 IS NULL AND p027_type_id IS NOT NULL) OR (p027 IS NOT NULL AND p027_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p028, p028_type_id, p028_type_name
FROM blockparameters
    WHERE (p028 IS NULL AND p028_type_id IS NOT NULL) OR (p028 IS NOT NULL AND p028_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p029, p029_type_id, p029_type_name
FROM blockparameters
    WHERE (p029 IS NULL AND p029_type_id IS NOT NULL) OR (p029 IS NOT NULL AND p029_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;

SELECT block_name, p030, p030_type_id, p030_type_name
FROM blockparameters
    WHERE (p030 IS NULL AND p030_type_id IS NOT NULL) OR (p030 IS NOT NULL AND p030_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p031, p031_type_id, p031_type_name
FROM blockparameters
    WHERE (p031 IS NULL AND p031_type_id IS NOT NULL) OR (p031 IS NOT NULL AND p031_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p032, p032_type_id, p032_type_name
FROM blockparameters
    WHERE (p032 IS NULL AND p032_type_id IS NOT NULL) OR (p032 IS NOT NULL AND p032_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p033, p033_type_id, p033_type_name
FROM blockparameters
    WHERE (p033 IS NULL AND p033_type_id IS NOT NULL) OR (p033 IS NOT NULL AND p033_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p034, p034_type_id, p034_type_name
FROM blockparameters
    WHERE (p034 IS NULL AND p034_type_id IS NOT NULL) OR (p034 IS NOT NULL AND p034_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p035, p035_type_id, p035_type_name
FROM blockparameters
    WHERE (p035 IS NULL AND p035_type_id IS NOT NULL) OR (p035 IS NOT NULL AND p035_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p036, p036_type_id, p036_type_name
FROM blockparameters
    WHERE (p036 IS NULL AND p036_type_id IS NOT NULL) OR (p036 IS NOT NULL AND p036_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p037, p037_type_id, p037_type_name
FROM blockparameters
    WHERE (p037 IS NULL AND p037_type_id IS NOT NULL) OR (p037 IS NOT NULL AND p037_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p038, p038_type_id, p038_type_name
FROM blockparameters
    WHERE (p038 IS NULL AND p038_type_id IS NOT NULL) OR (p038 IS NOT NULL AND p038_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;
SELECT block_name, p039, p039_type_id, p039_type_name
FROM blockparameters
    WHERE (p039 IS NULL AND p039_type_id IS NOT NULL) OR (p039 IS NOT NULL AND p039_type_id IS NULL)
    ORDER BY 1
    LIMIT 5;

ALTER TABLE blockparameters
    MODIFY COLUMN block_id int UNIQUE NOT NULL,
    DROP COLUMN block_name,
    DROP COLUMN p000_type_name,
    DROP COLUMN p001_type_name,
    DROP COLUMN p002_type_name,
    DROP COLUMN p003_type_name,
    DROP COLUMN p004_type_name,
    DROP COLUMN p005_type_name,
    DROP COLUMN p006_type_name,
    DROP COLUMN p007_type_name,
    DROP COLUMN p008_type_name,
    DROP COLUMN p009_type_name,
    DROP COLUMN p010_type_name,
    DROP COLUMN p011_type_name,
    DROP COLUMN p012_type_name,
    DROP COLUMN p013_type_name,
    DROP COLUMN p014_type_name,
    DROP COLUMN p015_type_name,
    DROP COLUMN p016_type_name,
    DROP COLUMN p017_type_name,
    DROP COLUMN p018_type_name,
    DROP COLUMN p019_type_name,
    DROP COLUMN p020_type_name,
    DROP COLUMN p021_type_name,
    DROP COLUMN p022_type_name,
    DROP COLUMN p023_type_name,
    DROP COLUMN p024_type_name,
    DROP COLUMN p025_type_name,
    DROP COLUMN p026_type_name,
    DROP COLUMN p027_type_name,
    DROP COLUMN p028_type_name,
    DROP COLUMN p029_type_name,
    DROP COLUMN p030_type_name,
    DROP COLUMN p031_type_name,
    DROP COLUMN p032_type_name,
    DROP COLUMN p033_type_name,
    DROP COLUMN p034_type_name,
    DROP COLUMN p035_type_name,
    DROP COLUMN p036_type_name,
    DROP COLUMN p037_type_name,
    DROP COLUMN p038_type_name,
    DROP COLUMN p039_type_name;

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) UNIQUE,
    sort_order int NOT NULL
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'eSimCategories.csv'
    INTO TABLE categories
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (id, name, sort_order);

DROP TABLE IF EXISTS blockcategories;
CREATE TABLE blockcategories (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category_id int,
    category_name varchar(100),
    block_id int,
    block_name varchar(100),
    CONSTRAINT blockcategories_category_id_block_id UNIQUE(category_id, block_id),
    CONSTRAINT blockcategories_category_name_block_name UNIQUE(category_name, block_name)
) ENGINE=InnoDB;

LOAD DATA LOCAL INFILE 'eSimBlockCategories.csv'
    INTO TABLE blockcategories
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (category_name, block_name);

UPDATE blockcategories
INNER JOIN categories ON category_name = categories.name
INNER JOIN blocks ON block_name = blocks.name
    SET category_id = categories.id,
        block_id = blocks.id;

ALTER TABLE blockcategories
    MODIFY COLUMN category_id int NOT NULL,
    DROP COLUMN category_name,
    MODIFY COLUMN block_id int NOT NULL,
    DROP COLUMN block_name;
