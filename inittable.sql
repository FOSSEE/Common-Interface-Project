DELETE FROM xcosblocks_blockparameter;
DELETE FROM xcosblocks_blockport;
DELETE FROM xcosblocks_block_categories;
DELETE FROM xcosblocks_block;
DELETE FROM xcosblocks_blockprefixparameter;
DELETE FROM xcosblocks_blockprefix;
DELETE FROM xcosblocks_category;
DELETE FROM xcosblocks_parameterdatatype;

ALTER TABLE xcosblocks_blockparameter AUTO_INCREMENT = 1;
ALTER TABLE xcosblocks_blockport AUTO_INCREMENT = 1;
ALTER TABLE xcosblocks_block_categories AUTO_INCREMENT = 1;
ALTER TABLE xcosblocks_block AUTO_INCREMENT = 1;
ALTER TABLE xcosblocks_blockprefixparameter AUTO_INCREMENT = 1;
ALTER TABLE xcosblocks_blockprefix AUTO_INCREMENT = 1;
ALTER TABLE xcosblocks_category AUTO_INCREMENT = 1;
ALTER TABLE xcosblocks_parameterdatatype AUTO_INCREMENT = 1;

SET @blocktype_name = 'eSim';

INSERT IGNORE INTO xcosblocks_blocktype (name) VALUES (@blocktype_name);

SELECT id INTO @blocktype_id FROM xcosblocks_blocktype WHERE name = @blocktype_name;

LOAD DATA LOCAL INFILE 'data/datatypes.csv'
    INTO TABLE xcosblocks_parameterdatatype
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, name, @tmp1);

LOAD DATA LOCAL INFILE 'data/categories.csv'
    INTO TABLE xcosblocks_category
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, name, sort_order, @tmp1);

LOAD DATA LOCAL INFILE 'data/blockprefixes.csv'
    INTO TABLE xcosblocks_blockprefix
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, name, @tmp2, @tmp3,
    @p000_key, @p000, @p000_type, p000_value_initial,
    @p001_key, @p001, @p001_type, p001_value_initial,
    @p002_key, @p002, @p002_type, p002_value_initial,
    @p003_key, @p003, @p003_type, p003_value_initial,
    @p004_key, @p004, @p004_type, p004_value_initial,
    @p005_key, @p005, @p005_type, p005_value_initial,
    @p006_key, @p006, @p006_type, p006_value_initial,
    @p007_key, @p007, @p007_type, p007_value_initial,
    @p008_key, @p008, @p008_type, p008_value_initial,
    @p009_key, @p009, @p009_type, p009_value_initial,
    @p010_key, @p010, @p010_type, p010_value_initial,
    @p011_key, @p011, @p011_type, p011_value_initial,
    @p012_key, @p012, @p012_type, p012_value_initial,
    @p013_key, @p013, @p013_type, p013_value_initial,
    @p014_key, @p014, @p014_type, p014_value_initial,
    @p015_key, @p015, @p015_type, p015_value_initial,
    @p016_key, @p016, @p016_type, p016_value_initial,
    @p017_key, @p017, @p017_type, p017_value_initial,
    @p018_key, @p018, @p018_type, p018_value_initial,
    @p019_key, @p019, @p019_type, p019_value_initial,
    @p020_key, @p020, @p020_type, p020_value_initial,
    @p021_key, @p021, @p021_type, p021_value_initial,
    @p022_key, @p022, @p022_type, p022_value_initial,
    @p023_key, @p023, @p023_type, p023_value_initial,
    @p024_key, @p024, @p024_type, p024_value_initial,
    @p025_key, @p025, @p025_type, p025_value_initial,
    @p026_key, @p026, @p026_type, p026_value_initial,
    @p027_key, @p027, @p027_type, p027_value_initial,
    @p028_key, @p028, @p028_type, p028_value_initial,
    @p029_key, @p029, @p029_type, p029_value_initial,
    @p030_key, @p030, @p030_type, p030_value_initial,
    @p031_key, @p031, @p031_type, p031_value_initial,
    @p032_key, @p032, @p032_type, p032_value_initial,
    @p033_key, @p033, @p033_type, p033_value_initial,
    @p034_key, @p034, @p034_type, p034_value_initial,
    @p035_key, @p035, @p035_type, p035_value_initial,
    @p036_key, @p036, @p036_type, p036_value_initial,
    @p037_key, @p037, @p037_type, p037_value_initial,
    @p038_key, @p038, @p038_type, p038_value_initial,
    @p039_key, @p039, @p039_type, p039_value_initial,
    @p040_key, @p040, @p040_type, p040_value_initial,
    @p041_key, @p041, @p041_type, p041_value_initial);

LOAD DATA LOCAL INFILE 'data/blockprefixes.csv'
    INTO TABLE xcosblocks_blockprefixparameter
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (blockprefix_id, @name, @tmp2, @tmp3,
    @p000_key, p000, @p000_type, @p000_value_initial,
    @p001_key, p001, @p001_type, @p001_value_initial,
    @p002_key, p002, @p002_type, @p002_value_initial,
    @p003_key, p003, @p003_type, @p003_value_initial,
    @p004_key, p004, @p004_type, @p004_value_initial,
    @p005_key, p005, @p005_type, @p005_value_initial,
    @p006_key, p006, @p006_type, @p006_value_initial,
    @p007_key, p007, @p007_type, @p007_value_initial,
    @p008_key, p008, @p008_type, @p008_value_initial,
    @p009_key, p009, @p009_type, @p009_value_initial,
    @p010_key, p010, @p010_type, @p010_value_initial,
    @p011_key, p011, @p011_type, @p011_value_initial,
    @p012_key, p012, @p012_type, @p012_value_initial,
    @p013_key, p013, @p013_type, @p013_value_initial,
    @p014_key, p014, @p014_type, @p014_value_initial,
    @p015_key, p015, @p015_type, @p015_value_initial,
    @p016_key, p016, @p016_type, @p016_value_initial,
    @p017_key, p017, @p017_type, @p017_value_initial,
    @p018_key, p018, @p018_type, @p018_value_initial,
    @p019_key, p019, @p019_type, @p019_value_initial,
    @p020_key, p020, @p020_type, @p020_value_initial,
    @p021_key, p021, @p021_type, @p021_value_initial,
    @p022_key, p022, @p022_type, @p022_value_initial,
    @p023_key, p023, @p023_type, @p023_value_initial,
    @p024_key, p024, @p024_type, @p024_value_initial,
    @p025_key, p025, @p025_type, @p025_value_initial,
    @p026_key, p026, @p026_type, @p026_value_initial,
    @p027_key, p027, @p027_type, @p027_value_initial,
    @p028_key, p028, @p028_type, @p028_value_initial,
    @p029_key, p029, @p029_type, @p029_value_initial,
    @p030_key, p030, @p030_type, @p030_value_initial,
    @p031_key, p031, @p031_type, @p031_value_initial,
    @p032_key, p032, @p032_type, @p032_value_initial,
    @p033_key, p033, @p033_type, @p033_value_initial,
    @p034_key, p034, @p034_type, @p034_value_initial,
    @p035_key, p035, @p035_type, @p035_value_initial,
    @p036_key, p036, @p036_type, @p036_value_initial,
    @p037_key, p037, @p037_type, @p037_value_initial,
    @p038_key, p038, @p038_type, @p038_value_initial,
    @p039_key, p039, @p039_type, @p039_value_initial,
    @p040_key, p040, @p040_type, @p040_value_initial,
    @p041_key, p041, @p041_type, @p041_value_initial)
    SET
    p000_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p000_type),
    p001_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p001_type),
    p002_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p002_type),
    p003_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p003_type),
    p004_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p004_type),
    p005_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p005_type),
    p006_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p006_type),
    p007_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p007_type),
    p008_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p008_type),
    p009_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p009_type),
    p010_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p010_type),
    p011_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p011_type),
    p012_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p012_type),
    p013_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p013_type),
    p014_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p014_type),
    p015_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p015_type),
    p016_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p016_type),
    p017_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p017_type),
    p018_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p018_type),
    p019_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p019_type),
    p020_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p020_type),
    p021_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p021_type),
    p022_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p022_type),
    p023_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p023_type),
    p024_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p024_type),
    p025_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p025_type),
    p026_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p026_type),
    p027_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p027_type),
    p028_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p028_type),
    p029_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p029_type),
    p030_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p030_type),
    p031_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p031_type),
    p032_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p032_type),
    p033_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p033_type),
    p034_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p034_type),
    p035_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p035_type),
    p036_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p036_type),
    p037_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p037_type),
    p038_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p038_type),
    p039_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p039_type),
    p040_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p040_type),
    p041_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p041_type);

LOAD DATA LOCAL INFILE 'data/main-category-blocks.csv'
    INTO TABLE xcosblocks_block
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @main_category_name, name, @blockprefix_name, initial_display_parameter,
    @p000_key, @p000, @p000_type, p000_value_initial,
    @p001_key, @p001, @p001_type, p001_value_initial,
    @p002_key, @p002, @p002_type, p002_value_initial,
    @p003_key, @p003, @p003_type, p003_value_initial,
    @p004_key, @p004, @p004_type, p004_value_initial,
    @p005_key, @p005, @p005_type, p005_value_initial,
    @p006_key, @p006, @p006_type, p006_value_initial,
    @p007_key, @p007, @p007_type, p007_value_initial,
    @p008_key, @p008, @p008_type, p008_value_initial,
    @p009_key, @p009, @p009_type, p009_value_initial,
    @p010_key, @p010, @p010_type, p010_value_initial,
    @p011_key, @p011, @p011_type, p011_value_initial,
    @p012_key, @p012, @p012_type, p012_value_initial,
    @p013_key, @p013, @p013_type, p013_value_initial,
    @p014_key, @p014, @p014_type, p014_value_initial,
    @p015_key, @p015, @p015_type, p015_value_initial,
    @p016_key, @p016, @p016_type, p016_value_initial,
    @p017_key, @p017, @p017_type, p017_value_initial,
    @p018_key, @p018, @p018_type, p018_value_initial,
    @p019_key, @p019, @p019_type, p019_value_initial,
    @p020_key, @p020, @p020_type, p020_value_initial,
    @p021_key, @p021, @p021_type, p021_value_initial,
    @p022_key, @p022, @p022_type, p022_value_initial,
    @p023_key, @p023, @p023_type, p023_value_initial,
    @p024_key, @p024, @p024_type, p024_value_initial,
    @p025_key, @p025, @p025_type, p025_value_initial,
    @p026_key, @p026, @p026_type, p026_value_initial,
    @p027_key, @p027, @p027_type, p027_value_initial,
    @p028_key, @p028, @p028_type, p028_value_initial,
    @p029_key, @p029, @p029_type, p029_value_initial,
    @p030_key, @p030, @p030_type, p030_value_initial,
    @p031_key, @p031, @p031_type, p031_value_initial,
    @p032_key, @p032, @p032_type, p032_value_initial,
    @p033_key, @p033, @p033_type, p033_value_initial,
    @p034_key, @p034, @p034_type, p034_value_initial,
    @p035_key, @p035, @p035_type, p035_value_initial,
    @p036_key, @p036, @p036_type, p036_value_initial,
    @p037_key, @p037, @p037_type, p037_value_initial,
    @p038_key, @p038, @p038_type, p038_value_initial,
    @p039_key, @p039, @p039_type, p039_value_initial,
    @p040_key, @p040, @p040_type, p040_value_initial,
    @p041_key, @p041, @p041_type, p041_value_initial)
    SET block_width = 40,
    block_height = 40,
    blocktype_id = @blocktype_id,
    blockprefix_id = (SELECT id FROM xcosblocks_blockprefix WHERE name = @blockprefix_name),
    main_category_id = (SELECT id from xcosblocks_category WHERE name = @main_category_name);

LOAD DATA LOCAL INFILE 'data/main-category-blocks.csv'
    INTO TABLE xcosblocks_blockparameter
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (block_id, @main_category_name, @name, @blockprefix_name, @initial_display_parameter,
    @p000_key, p000, @p000_type, @p000_value_initial,
    @p001_key, p001, @p001_type, @p001_value_initial,
    @p002_key, p002, @p002_type, @p002_value_initial,
    @p003_key, p003, @p003_type, @p003_value_initial,
    @p004_key, p004, @p004_type, @p004_value_initial,
    @p005_key, p005, @p005_type, @p005_value_initial,
    @p006_key, p006, @p006_type, @p006_value_initial,
    @p007_key, p007, @p007_type, @p007_value_initial,
    @p008_key, p008, @p008_type, @p008_value_initial,
    @p009_key, p009, @p009_type, @p009_value_initial,
    @p010_key, p010, @p010_type, @p010_value_initial,
    @p011_key, p011, @p011_type, @p011_value_initial,
    @p012_key, p012, @p012_type, @p012_value_initial,
    @p013_key, p013, @p013_type, @p013_value_initial,
    @p014_key, p014, @p014_type, @p014_value_initial,
    @p015_key, p015, @p015_type, @p015_value_initial,
    @p016_key, p016, @p016_type, @p016_value_initial,
    @p017_key, p017, @p017_type, @p017_value_initial,
    @p018_key, p018, @p018_type, @p018_value_initial,
    @p019_key, p019, @p019_type, @p019_value_initial,
    @p020_key, p020, @p020_type, @p020_value_initial,
    @p021_key, p021, @p021_type, @p021_value_initial,
    @p022_key, p022, @p022_type, @p022_value_initial,
    @p023_key, p023, @p023_type, @p023_value_initial,
    @p024_key, p024, @p024_type, @p024_value_initial,
    @p025_key, p025, @p025_type, @p025_value_initial,
    @p026_key, p026, @p026_type, @p026_value_initial,
    @p027_key, p027, @p027_type, @p027_value_initial,
    @p028_key, p028, @p028_type, @p028_value_initial,
    @p029_key, p029, @p029_type, @p029_value_initial,
    @p030_key, p030, @p030_type, @p030_value_initial,
    @p031_key, p031, @p031_type, @p031_value_initial,
    @p032_key, p032, @p032_type, @p032_value_initial,
    @p033_key, p033, @p033_type, @p033_value_initial,
    @p034_key, p034, @p034_type, @p034_value_initial,
    @p035_key, p035, @p035_type, @p035_value_initial,
    @p036_key, p036, @p036_type, @p036_value_initial,
    @p037_key, p037, @p037_type, @p037_value_initial,
    @p038_key, p038, @p038_type, @p038_value_initial,
    @p039_key, p039, @p039_type, @p039_value_initial,
    @p040_key, p040, @p040_type, @p040_value_initial,
    @p041_key, p041, @p041_type, @p041_value_initial)
    SET
    p000_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p000_type),
    p001_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p001_type),
    p002_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p002_type),
    p003_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p003_type),
    p004_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p004_type),
    p005_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p005_type),
    p006_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p006_type),
    p007_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p007_type),
    p008_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p008_type),
    p009_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p009_type),
    p010_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p010_type),
    p011_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p011_type),
    p012_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p012_type),
    p013_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p013_type),
    p014_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p014_type),
    p015_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p015_type),
    p016_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p016_type),
    p017_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p017_type),
    p018_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p018_type),
    p019_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p019_type),
    p020_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p020_type),
    p021_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p021_type),
    p022_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p022_type),
    p023_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p023_type),
    p024_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p024_type),
    p025_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p025_type),
    p026_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p026_type),
    p027_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p027_type),
    p028_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p028_type),
    p029_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p029_type),
    p030_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p030_type),
    p031_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p031_type),
    p032_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p032_type),
    p033_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p033_type),
    p034_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p034_type),
    p035_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p035_type),
    p036_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p036_type),
    p037_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p037_type),
    p038_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p038_type),
    p039_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p039_type),
    p040_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p040_type),
    p041_type_id = (SELECT id FROM xcosblocks_parameterdatatype WHERE name = @p041_type);

LOAD DATA LOCAL INFILE 'data/categories-blocks.csv'
    INTO TABLE xcosblocks_block_categories
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @category_name, @main_category_name, @block_name)
    SET block_id = (SELECT xcosblocks_block.id FROM xcosblocks_block JOIN xcosblocks_category ON main_category_id = xcosblocks_category.id WHERE xcosblocks_block.name = @block_name AND xcosblocks_category.name = @main_category_name AND blocktype_id = @blocktype_id),
    category_id = (SELECT id from xcosblocks_category WHERE name = @category_name);

LOAD DATA LOCAL INFILE 'data/blocks-ports.csv'
    INTO TABLE xcosblocks_blockport
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @main_category_name, @block_name, port_order, port_name, port_number, port_x, port_y, port_orientation, port_part, port_dmg, port_type)
    SET block_id = (SELECT xcosblocks_block.id FROM xcosblocks_block JOIN xcosblocks_category ON main_category_id = xcosblocks_category.id WHERE xcosblocks_block.name = @block_name AND xcosblocks_category.name = @main_category_name AND blocktype_id = @blocktype_id);

CREATE TEMPORARY TABLE tmp_xcosblocks_block (
    id int NOT NULL PRIMARY KEY,
    block_width int NOT NULL,
    block_height int NOT NULL
);

LOAD DATA LOCAL INFILE 'data/getsize.csv'
    INTO TABLE tmp_xcosblocks_block
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (@main_category_name, @block_name, block_width, block_height)
    SET id = (SELECT xcosblocks_block.id FROM xcosblocks_block JOIN xcosblocks_category ON main_category_id = xcosblocks_category.id WHERE xcosblocks_block.name = @block_name AND xcosblocks_category.name = @main_category_name AND blocktype_id = @blocktype_id);

DELETE FROM xcosblocks_blockprefixparameter
    WHERE (p000 IS NULL OR p000 = '') AND
    (p001 IS NULL OR p001 = '') AND
    (p002 IS NULL OR p002 = '') AND
    (p003 IS NULL OR p003 = '') AND
    (p004 IS NULL OR p004 = '') AND
    (p005 IS NULL OR p005 = '') AND
    (p006 IS NULL OR p006 = '') AND
    (p007 IS NULL OR p007 = '') AND
    (p008 IS NULL OR p008 = '') AND
    (p009 IS NULL OR p009 = '') AND
    (p010 IS NULL OR p010 = '') AND
    (p011 IS NULL OR p011 = '') AND
    (p012 IS NULL OR p012 = '') AND
    (p013 IS NULL OR p013 = '') AND
    (p014 IS NULL OR p014 = '') AND
    (p015 IS NULL OR p015 = '') AND
    (p016 IS NULL OR p016 = '') AND
    (p017 IS NULL OR p017 = '') AND
    (p018 IS NULL OR p018 = '') AND
    (p019 IS NULL OR p019 = '') AND
    (p020 IS NULL OR p020 = '') AND
    (p021 IS NULL OR p021 = '') AND
    (p022 IS NULL OR p022 = '') AND
    (p023 IS NULL OR p023 = '') AND
    (p024 IS NULL OR p024 = '') AND
    (p025 IS NULL OR p025 = '') AND
    (p026 IS NULL OR p026 = '') AND
    (p027 IS NULL OR p027 = '') AND
    (p028 IS NULL OR p028 = '') AND
    (p029 IS NULL OR p029 = '') AND
    (p030 IS NULL OR p030 = '') AND
    (p031 IS NULL OR p031 = '') AND
    (p032 IS NULL OR p032 = '') AND
    (p033 IS NULL OR p033 = '') AND
    (p034 IS NULL OR p034 = '') AND
    (p035 IS NULL OR p035 = '') AND
    (p036 IS NULL OR p036 = '') AND
    (p037 IS NULL OR p037 = '') AND
    (p038 IS NULL OR p038 = '') AND
    (p039 IS NULL OR p039 = '') AND
    (p040 IS NULL OR p040 = '') AND
    (p041 IS NULL OR p041 = '') AND
    (p042 IS NULL OR p042 = '') AND
    (p043 IS NULL OR p043 = '') AND
    (p044 IS NULL OR p044 = '') AND
    (p045 IS NULL OR p045 = '') AND
    (p046 IS NULL OR p046 = '') AND
    (p047 IS NULL OR p047 = '') AND
    (p048 IS NULL OR p048 = '') AND
    (p049 IS NULL OR p049 = '') AND
    (p050 IS NULL OR p050 = '') AND
    (p051 IS NULL OR p051 = '') AND
    (p052 IS NULL OR p052 = '') AND
    (p053 IS NULL OR p053 = '') AND
    (p054 IS NULL OR p054 = '') AND
    (p055 IS NULL OR p055 = '') AND
    (p056 IS NULL OR p056 = '') AND
    (p057 IS NULL OR p057 = '') AND
    (p058 IS NULL OR p058 = '') AND
    (p059 IS NULL OR p059 = '');

DELETE FROM xcosblocks_blockparameter
    WHERE (p000 IS NULL OR p000 = '') AND
    (p001 IS NULL OR p001 = '') AND
    (p002 IS NULL OR p002 = '') AND
    (p003 IS NULL OR p003 = '') AND
    (p004 IS NULL OR p004 = '') AND
    (p005 IS NULL OR p005 = '') AND
    (p006 IS NULL OR p006 = '') AND
    (p007 IS NULL OR p007 = '') AND
    (p008 IS NULL OR p008 = '') AND
    (p009 IS NULL OR p009 = '') AND
    (p010 IS NULL OR p010 = '') AND
    (p011 IS NULL OR p011 = '') AND
    (p012 IS NULL OR p012 = '') AND
    (p013 IS NULL OR p013 = '') AND
    (p014 IS NULL OR p014 = '') AND
    (p015 IS NULL OR p015 = '') AND
    (p016 IS NULL OR p016 = '') AND
    (p017 IS NULL OR p017 = '') AND
    (p018 IS NULL OR p018 = '') AND
    (p019 IS NULL OR p019 = '') AND
    (p020 IS NULL OR p020 = '') AND
    (p021 IS NULL OR p021 = '') AND
    (p022 IS NULL OR p022 = '') AND
    (p023 IS NULL OR p023 = '') AND
    (p024 IS NULL OR p024 = '') AND
    (p025 IS NULL OR p025 = '') AND
    (p026 IS NULL OR p026 = '') AND
    (p027 IS NULL OR p027 = '') AND
    (p028 IS NULL OR p028 = '') AND
    (p029 IS NULL OR p029 = '') AND
    (p030 IS NULL OR p030 = '') AND
    (p031 IS NULL OR p031 = '') AND
    (p032 IS NULL OR p032 = '') AND
    (p033 IS NULL OR p033 = '') AND
    (p034 IS NULL OR p034 = '') AND
    (p035 IS NULL OR p035 = '') AND
    (p036 IS NULL OR p036 = '') AND
    (p037 IS NULL OR p037 = '') AND
    (p038 IS NULL OR p038 = '') AND
    (p039 IS NULL OR p039 = '') AND
    (p040 IS NULL OR p040 = '') AND
    (p041 IS NULL OR p041 = '') AND
    (p042 IS NULL OR p042 = '') AND
    (p043 IS NULL OR p043 = '') AND
    (p044 IS NULL OR p044 = '') AND
    (p045 IS NULL OR p045 = '') AND
    (p046 IS NULL OR p046 = '') AND
    (p047 IS NULL OR p047 = '') AND
    (p048 IS NULL OR p048 = '') AND
    (p049 IS NULL OR p049 = '') AND
    (p050 IS NULL OR p050 = '') AND
    (p051 IS NULL OR p051 = '') AND
    (p052 IS NULL OR p052 = '') AND
    (p053 IS NULL OR p053 = '') AND
    (p054 IS NULL OR p054 = '') AND
    (p055 IS NULL OR p055 = '') AND
    (p056 IS NULL OR p056 = '') AND
    (p057 IS NULL OR p057 = '') AND
    (p058 IS NULL OR p058 = '') AND
    (p059 IS NULL OR p059 = '');

UPDATE xcosblocks_block B
    JOIN xcosblocks_blockprefix BP ON BP.id = B.blockprefix_id
    JOIN xcosblocks_category C ON C.id = B.main_category_id
    SET B.block_name = CONCAT(C.id, '-', BP.id, '-', B.name),
    B.block_image_path = CONCAT(C.name, '/', BP.name, '-', B.name, '-1-A.svg');

UPDATE xcosblocks_block B
    JOIN tmp_xcosblocks_block TB ON TB.id = B.id
    SET B.block_width = TB.block_width,
    B.block_height = TB.block_height;

UPDATE xcosblocks_block B
    JOIN xcosblocks_blockprefix BPR ON BPR.id = B.blockprefix_id
    SET B.p000_value_initial = BPR.p000_value_initial,
    B.p001_value_initial = BPR.p001_value_initial,
    B.p002_value_initial = BPR.p002_value_initial,
    B.p003_value_initial = BPR.p003_value_initial,
    B.p004_value_initial = BPR.p004_value_initial,
    B.p005_value_initial = BPR.p005_value_initial,
    B.p006_value_initial = BPR.p006_value_initial,
    B.p007_value_initial = BPR.p007_value_initial,
    B.p008_value_initial = BPR.p008_value_initial,
    B.p009_value_initial = BPR.p009_value_initial,
    B.p010_value_initial = BPR.p010_value_initial,
    B.p011_value_initial = BPR.p011_value_initial,
    B.p012_value_initial = BPR.p012_value_initial,
    B.p013_value_initial = BPR.p013_value_initial,
    B.p014_value_initial = BPR.p014_value_initial,
    B.p015_value_initial = BPR.p015_value_initial,
    B.p016_value_initial = BPR.p016_value_initial,
    B.p017_value_initial = BPR.p017_value_initial,
    B.p018_value_initial = BPR.p018_value_initial,
    B.p019_value_initial = BPR.p019_value_initial,
    B.p020_value_initial = BPR.p020_value_initial,
    B.p021_value_initial = BPR.p021_value_initial,
    B.p022_value_initial = BPR.p022_value_initial,
    B.p023_value_initial = BPR.p023_value_initial,
    B.p024_value_initial = BPR.p024_value_initial,
    B.p025_value_initial = BPR.p025_value_initial,
    B.p026_value_initial = BPR.p026_value_initial,
    B.p027_value_initial = BPR.p027_value_initial,
    B.p028_value_initial = BPR.p028_value_initial,
    B.p029_value_initial = BPR.p029_value_initial,
    B.p030_value_initial = BPR.p030_value_initial,
    B.p031_value_initial = BPR.p031_value_initial,
    B.p032_value_initial = BPR.p032_value_initial,
    B.p033_value_initial = BPR.p033_value_initial,
    B.p034_value_initial = BPR.p034_value_initial,
    B.p035_value_initial = BPR.p035_value_initial,
    B.p036_value_initial = BPR.p036_value_initial,
    B.p037_value_initial = BPR.p037_value_initial,
    B.p038_value_initial = BPR.p038_value_initial,
    B.p039_value_initial = BPR.p039_value_initial,
    B.p040_value_initial = BPR.p040_value_initial,
    B.p041_value_initial = BPR.p041_value_initial,
    B.p042_value_initial = BPR.p042_value_initial,
    B.p043_value_initial = BPR.p043_value_initial,
    B.p044_value_initial = BPR.p044_value_initial,
    B.p045_value_initial = BPR.p045_value_initial,
    B.p046_value_initial = BPR.p046_value_initial,
    B.p047_value_initial = BPR.p047_value_initial,
    B.p048_value_initial = BPR.p048_value_initial,
    B.p049_value_initial = BPR.p049_value_initial,
    B.p050_value_initial = BPR.p050_value_initial,
    B.p051_value_initial = BPR.p051_value_initial,
    B.p052_value_initial = BPR.p052_value_initial,
    B.p053_value_initial = BPR.p053_value_initial,
    B.p054_value_initial = BPR.p054_value_initial,
    B.p055_value_initial = BPR.p055_value_initial,
    B.p056_value_initial = BPR.p056_value_initial,
    B.p057_value_initial = BPR.p057_value_initial,
    B.p058_value_initial = BPR.p058_value_initial,
    B.p059_value_initial = BPR.p059_value_initial
    WHERE (BPR.p000_value_initial IS NOT NULL AND BPR.p000_value_initial != '') OR
    (BPR.p001_value_initial IS NOT NULL AND BPR.p001_value_initial != '') OR
    (BPR.p002_value_initial IS NOT NULL AND BPR.p002_value_initial != '') OR
    (BPR.p003_value_initial IS NOT NULL AND BPR.p003_value_initial != '') OR
    (BPR.p004_value_initial IS NOT NULL AND BPR.p004_value_initial != '') OR
    (BPR.p005_value_initial IS NOT NULL AND BPR.p005_value_initial != '') OR
    (BPR.p006_value_initial IS NOT NULL AND BPR.p006_value_initial != '') OR
    (BPR.p007_value_initial IS NOT NULL AND BPR.p007_value_initial != '') OR
    (BPR.p008_value_initial IS NOT NULL AND BPR.p008_value_initial != '') OR
    (BPR.p009_value_initial IS NOT NULL AND BPR.p009_value_initial != '') OR
    (BPR.p010_value_initial IS NOT NULL AND BPR.p010_value_initial != '') OR
    (BPR.p011_value_initial IS NOT NULL AND BPR.p011_value_initial != '') OR
    (BPR.p012_value_initial IS NOT NULL AND BPR.p012_value_initial != '') OR
    (BPR.p013_value_initial IS NOT NULL AND BPR.p013_value_initial != '') OR
    (BPR.p014_value_initial IS NOT NULL AND BPR.p014_value_initial != '') OR
    (BPR.p015_value_initial IS NOT NULL AND BPR.p015_value_initial != '') OR
    (BPR.p016_value_initial IS NOT NULL AND BPR.p016_value_initial != '') OR
    (BPR.p017_value_initial IS NOT NULL AND BPR.p017_value_initial != '') OR
    (BPR.p018_value_initial IS NOT NULL AND BPR.p018_value_initial != '') OR
    (BPR.p019_value_initial IS NOT NULL AND BPR.p019_value_initial != '') OR
    (BPR.p020_value_initial IS NOT NULL AND BPR.p020_value_initial != '') OR
    (BPR.p021_value_initial IS NOT NULL AND BPR.p021_value_initial != '') OR
    (BPR.p022_value_initial IS NOT NULL AND BPR.p022_value_initial != '') OR
    (BPR.p023_value_initial IS NOT NULL AND BPR.p023_value_initial != '') OR
    (BPR.p024_value_initial IS NOT NULL AND BPR.p024_value_initial != '') OR
    (BPR.p025_value_initial IS NOT NULL AND BPR.p025_value_initial != '') OR
    (BPR.p026_value_initial IS NOT NULL AND BPR.p026_value_initial != '') OR
    (BPR.p027_value_initial IS NOT NULL AND BPR.p027_value_initial != '') OR
    (BPR.p028_value_initial IS NOT NULL AND BPR.p028_value_initial != '') OR
    (BPR.p029_value_initial IS NOT NULL AND BPR.p029_value_initial != '') OR
    (BPR.p030_value_initial IS NOT NULL AND BPR.p030_value_initial != '') OR
    (BPR.p031_value_initial IS NOT NULL AND BPR.p031_value_initial != '') OR
    (BPR.p032_value_initial IS NOT NULL AND BPR.p032_value_initial != '') OR
    (BPR.p033_value_initial IS NOT NULL AND BPR.p033_value_initial != '') OR
    (BPR.p034_value_initial IS NOT NULL AND BPR.p034_value_initial != '') OR
    (BPR.p035_value_initial IS NOT NULL AND BPR.p035_value_initial != '') OR
    (BPR.p036_value_initial IS NOT NULL AND BPR.p036_value_initial != '') OR
    (BPR.p037_value_initial IS NOT NULL AND BPR.p037_value_initial != '') OR
    (BPR.p038_value_initial IS NOT NULL AND BPR.p038_value_initial != '') OR
    (BPR.p039_value_initial IS NOT NULL AND BPR.p039_value_initial != '') OR
    (BPR.p040_value_initial IS NOT NULL AND BPR.p040_value_initial != '') OR
    (BPR.p041_value_initial IS NOT NULL AND BPR.p041_value_initial != '') OR
    (BPR.p042_value_initial IS NOT NULL AND BPR.p042_value_initial != '') OR
    (BPR.p043_value_initial IS NOT NULL AND BPR.p043_value_initial != '') OR
    (BPR.p044_value_initial IS NOT NULL AND BPR.p044_value_initial != '') OR
    (BPR.p045_value_initial IS NOT NULL AND BPR.p045_value_initial != '') OR
    (BPR.p046_value_initial IS NOT NULL AND BPR.p046_value_initial != '') OR
    (BPR.p047_value_initial IS NOT NULL AND BPR.p047_value_initial != '') OR
    (BPR.p048_value_initial IS NOT NULL AND BPR.p048_value_initial != '') OR
    (BPR.p049_value_initial IS NOT NULL AND BPR.p049_value_initial != '') OR
    (BPR.p050_value_initial IS NOT NULL AND BPR.p050_value_initial != '') OR
    (BPR.p051_value_initial IS NOT NULL AND BPR.p051_value_initial != '') OR
    (BPR.p052_value_initial IS NOT NULL AND BPR.p052_value_initial != '') OR
    (BPR.p053_value_initial IS NOT NULL AND BPR.p053_value_initial != '') OR
    (BPR.p054_value_initial IS NOT NULL AND BPR.p054_value_initial != '') OR
    (BPR.p055_value_initial IS NOT NULL AND BPR.p055_value_initial != '') OR
    (BPR.p056_value_initial IS NOT NULL AND BPR.p056_value_initial != '') OR
    (BPR.p057_value_initial IS NOT NULL AND BPR.p057_value_initial != '') OR
    (BPR.p058_value_initial IS NOT NULL AND BPR.p058_value_initial != '') OR
    (BPR.p059_value_initial IS NOT NULL AND BPR.p059_value_initial != '');

INSERT INTO xcosblocks_blockparameter (block_id,
    p000, p000_type_id, p001, p001_type_id, p002, p002_type_id, p003, p003_type_id,
    p004, p004_type_id, p005, p005_type_id, p006, p006_type_id, p007, p007_type_id,
    p008, p008_type_id, p009, p009_type_id, p010, p010_type_id, p011, p011_type_id,
    p012, p012_type_id, p013, p013_type_id, p014, p014_type_id, p015, p015_type_id,
    p016, p016_type_id, p017, p017_type_id, p018, p018_type_id, p019, p019_type_id,
    p020, p020_type_id, p021, p021_type_id, p022, p022_type_id, p023, p023_type_id,
    p024, p024_type_id, p025, p025_type_id, p026, p026_type_id, p027, p027_type_id,
    p028, p028_type_id, p029, p029_type_id, p030, p030_type_id, p031, p031_type_id,
    p032, p032_type_id, p033, p033_type_id, p034, p034_type_id, p035, p035_type_id,
    p036, p036_type_id, p037, p037_type_id, p038, p038_type_id, p039, p039_type_id,
    p040, p040_type_id, p041, p041_type_id, p042, p042_type_id, p043, p043_type_id,
    p044, p044_type_id, p045, p045_type_id, p046, p046_type_id, p047, p047_type_id,
    p048, p048_type_id, p049, p049_type_id, p050, p050_type_id, p051, p051_type_id,
    p052, p052_type_id, p053, p053_type_id, p054, p054_type_id, p055, p055_type_id,
    p056, p056_type_id, p057, p057_type_id, p058, p058_type_id, p059, p059_type_id)
    SELECT B.id,
    BPRPA.p000, BPRPA.p000_type_id, BPRPA.p001, BPRPA.p001_type_id, BPRPA.p002, BPRPA.p002_type_id, BPRPA.p003, BPRPA.p003_type_id,
    BPRPA.p004, BPRPA.p004_type_id, BPRPA.p005, BPRPA.p005_type_id, BPRPA.p006, BPRPA.p006_type_id, BPRPA.p007, BPRPA.p007_type_id,
    BPRPA.p008, BPRPA.p008_type_id, BPRPA.p009, BPRPA.p009_type_id, BPRPA.p010, BPRPA.p010_type_id, BPRPA.p011, BPRPA.p011_type_id,
    BPRPA.p012, BPRPA.p012_type_id, BPRPA.p013, BPRPA.p013_type_id, BPRPA.p014, BPRPA.p014_type_id, BPRPA.p015, BPRPA.p015_type_id,
    BPRPA.p016, BPRPA.p016_type_id, BPRPA.p017, BPRPA.p017_type_id, BPRPA.p018, BPRPA.p018_type_id, BPRPA.p019, BPRPA.p019_type_id,
    BPRPA.p020, BPRPA.p020_type_id, BPRPA.p021, BPRPA.p021_type_id, BPRPA.p022, BPRPA.p022_type_id, BPRPA.p023, BPRPA.p023_type_id,
    BPRPA.p024, BPRPA.p024_type_id, BPRPA.p025, BPRPA.p025_type_id, BPRPA.p026, BPRPA.p026_type_id, BPRPA.p027, BPRPA.p027_type_id,
    BPRPA.p028, BPRPA.p028_type_id, BPRPA.p029, BPRPA.p029_type_id, BPRPA.p030, BPRPA.p030_type_id, BPRPA.p031, BPRPA.p031_type_id,
    BPRPA.p032, BPRPA.p032_type_id, BPRPA.p033, BPRPA.p033_type_id, BPRPA.p034, BPRPA.p034_type_id, BPRPA.p035, BPRPA.p035_type_id,
    BPRPA.p036, BPRPA.p036_type_id, BPRPA.p037, BPRPA.p037_type_id, BPRPA.p038, BPRPA.p038_type_id, BPRPA.p039, BPRPA.p039_type_id,
    BPRPA.p040, BPRPA.p040_type_id, BPRPA.p041, BPRPA.p041_type_id, BPRPA.p042, BPRPA.p042_type_id, BPRPA.p043, BPRPA.p043_type_id,
    BPRPA.p044, BPRPA.p044_type_id, BPRPA.p045, BPRPA.p045_type_id, BPRPA.p046, BPRPA.p046_type_id, BPRPA.p047, BPRPA.p047_type_id,
    BPRPA.p048, BPRPA.p048_type_id, BPRPA.p049, BPRPA.p049_type_id, BPRPA.p050, BPRPA.p050_type_id, BPRPA.p051, BPRPA.p051_type_id,
    BPRPA.p052, BPRPA.p052_type_id, BPRPA.p053, BPRPA.p053_type_id, BPRPA.p054, BPRPA.p054_type_id, BPRPA.p055, BPRPA.p055_type_id,
    BPRPA.p056, BPRPA.p056_type_id, BPRPA.p057, BPRPA.p057_type_id, BPRPA.p058, BPRPA.p058_type_id, BPRPA.p059, BPRPA.p059_type_id
    FROM xcosblocks_block B
    JOIN xcosblocks_blockprefixparameter BPRPA ON BPRPA.blockprefix_id = B.blockprefix_id;
