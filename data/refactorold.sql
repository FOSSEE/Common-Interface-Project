UPDATE xcosblocks_block
SET p000_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 0;

DELETE FROM xcosblocks_blockparameter;
DELETE FROM SQLITE_SEQUENCE WHERE name = 'xcosblocks_blockparameter';
INSERT INTO xcosblocks_blockparameter (block_id)
SELECT DISTINCT block_id
FROM xcosblocks_newblockparameter
ORDER BY block_id;

UPDATE xcosblocks_blockparameter
SET p000 = N.p_label,
p000_help = N.p_help,
p000_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 0;

UPDATE xcosblocks_block
SET p001_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 1;

UPDATE xcosblocks_blockparameter
SET p001 = N.p_label,
p001_help = N.p_help,
p001_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 1;

UPDATE xcosblocks_block
SET p002_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 2;

UPDATE xcosblocks_blockparameter
SET p002 = N.p_label,
p002_help = N.p_help,
p002_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 2;

UPDATE xcosblocks_block
SET p003_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 3;

UPDATE xcosblocks_blockparameter
SET p003 = N.p_label,
p003_help = N.p_help,
p003_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 3;

UPDATE xcosblocks_block
SET p004_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 4;

UPDATE xcosblocks_blockparameter
SET p004 = N.p_label,
p004_help = N.p_help,
p004_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 4;

UPDATE xcosblocks_block
SET p005_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 5;

UPDATE xcosblocks_blockparameter
SET p005 = N.p_label,
p005_help = N.p_help,
p005_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 5;

UPDATE xcosblocks_block
SET p006_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 6;

UPDATE xcosblocks_blockparameter
SET p006 = N.p_label,
p006_help = N.p_help,
p006_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 6;

UPDATE xcosblocks_block
SET p007_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 7;

UPDATE xcosblocks_blockparameter
SET p007 = N.p_label,
p007_help = N.p_help,
p007_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 7;

UPDATE xcosblocks_block
SET p008_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 8;

UPDATE xcosblocks_blockparameter
SET p008 = N.p_label,
p008_help = N.p_help,
p008_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 8;

UPDATE xcosblocks_block
SET p009_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 9;

UPDATE xcosblocks_blockparameter
SET p009 = N.p_label,
p009_help = N.p_help,
p009_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 9;

UPDATE xcosblocks_block
SET p010_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 10;

UPDATE xcosblocks_blockparameter
SET p010 = N.p_label,
p010_help = N.p_help,
p010_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 10;

UPDATE xcosblocks_block
SET p011_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 11;

UPDATE xcosblocks_blockparameter
SET p011 = N.p_label,
p011_help = N.p_help,
p011_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 11;

UPDATE xcosblocks_block
SET p012_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 12;

UPDATE xcosblocks_blockparameter
SET p012 = N.p_label,
p012_help = N.p_help,
p012_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 12;

UPDATE xcosblocks_block
SET p013_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 13;

UPDATE xcosblocks_blockparameter
SET p013 = N.p_label,
p013_help = N.p_help,
p013_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 13;

UPDATE xcosblocks_block
SET p014_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 14;

UPDATE xcosblocks_blockparameter
SET p014 = N.p_label,
p014_help = N.p_help,
p014_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 14;

UPDATE xcosblocks_block
SET p015_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 15;

UPDATE xcosblocks_blockparameter
SET p015 = N.p_label,
p015_help = N.p_help,
p015_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 15;

UPDATE xcosblocks_block
SET p016_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 16;

UPDATE xcosblocks_blockparameter
SET p016 = N.p_label,
p016_help = N.p_help,
p016_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 16;

UPDATE xcosblocks_block
SET p017_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 17;

UPDATE xcosblocks_blockparameter
SET p017 = N.p_label,
p017_help = N.p_help,
p017_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 17;

UPDATE xcosblocks_block
SET p018_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 18;

UPDATE xcosblocks_blockparameter
SET p018 = N.p_label,
p018_help = N.p_help,
p018_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 18;

UPDATE xcosblocks_block
SET p019_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 19;

UPDATE xcosblocks_blockparameter
SET p019 = N.p_label,
p019_help = N.p_help,
p019_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 19;

UPDATE xcosblocks_block
SET p020_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 20;

UPDATE xcosblocks_blockparameter
SET p020 = N.p_label,
p020_help = N.p_help,
p020_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 20;

UPDATE xcosblocks_block
SET p021_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 21;

UPDATE xcosblocks_blockparameter
SET p021 = N.p_label,
p021_help = N.p_help,
p021_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 21;

UPDATE xcosblocks_block
SET p022_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 22;

UPDATE xcosblocks_blockparameter
SET p022 = N.p_label,
p022_help = N.p_help,
p022_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 22;

UPDATE xcosblocks_block
SET p023_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 23;

UPDATE xcosblocks_blockparameter
SET p023 = N.p_label,
p023_help = N.p_help,
p023_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 23;

UPDATE xcosblocks_block
SET p024_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 24;

UPDATE xcosblocks_blockparameter
SET p024 = N.p_label,
p024_help = N.p_help,
p024_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 24;

UPDATE xcosblocks_block
SET p025_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 25;

UPDATE xcosblocks_blockparameter
SET p025 = N.p_label,
p025_help = N.p_help,
p025_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 25;

UPDATE xcosblocks_block
SET p026_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 26;

UPDATE xcosblocks_blockparameter
SET p026 = N.p_label,
p026_help = N.p_help,
p026_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 26;

UPDATE xcosblocks_block
SET p027_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 27;

UPDATE xcosblocks_blockparameter
SET p027 = N.p_label,
p027_help = N.p_help,
p027_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 27;

UPDATE xcosblocks_block
SET p028_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 28;

UPDATE xcosblocks_blockparameter
SET p028 = N.p_label,
p028_help = N.p_help,
p028_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 28;

UPDATE xcosblocks_block
SET p029_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 29;

UPDATE xcosblocks_blockparameter
SET p029 = N.p_label,
p029_help = N.p_help,
p029_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 29;

UPDATE xcosblocks_block
SET p030_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 30;

UPDATE xcosblocks_blockparameter
SET p030 = N.p_label,
p030_help = N.p_help,
p030_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 30;

UPDATE xcosblocks_block
SET p031_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 31;

UPDATE xcosblocks_blockparameter
SET p031 = N.p_label,
p031_help = N.p_help,
p031_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 31;

UPDATE xcosblocks_block
SET p032_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 32;

UPDATE xcosblocks_blockparameter
SET p032 = N.p_label,
p032_help = N.p_help,
p032_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 32;

UPDATE xcosblocks_block
SET p033_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 33;

UPDATE xcosblocks_blockparameter
SET p033 = N.p_label,
p033_help = N.p_help,
p033_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 33;

UPDATE xcosblocks_block
SET p034_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 34;

UPDATE xcosblocks_blockparameter
SET p034 = N.p_label,
p034_help = N.p_help,
p034_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 34;

UPDATE xcosblocks_block
SET p035_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 35;

UPDATE xcosblocks_blockparameter
SET p035 = N.p_label,
p035_help = N.p_help,
p035_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 35;

UPDATE xcosblocks_block
SET p036_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 36;

UPDATE xcosblocks_blockparameter
SET p036 = N.p_label,
p036_help = N.p_help,
p036_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 36;

UPDATE xcosblocks_block
SET p037_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 37;

UPDATE xcosblocks_blockparameter
SET p037 = N.p_label,
p037_help = N.p_help,
p037_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 37;

UPDATE xcosblocks_block
SET p038_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 38;

UPDATE xcosblocks_blockparameter
SET p038 = N.p_label,
p038_help = N.p_help,
p038_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 38;

UPDATE xcosblocks_block
SET p039_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 39;

UPDATE xcosblocks_blockparameter
SET p039 = N.p_label,
p039_help = N.p_help,
p039_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 39;

UPDATE xcosblocks_block
SET p040_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 40;

UPDATE xcosblocks_blockparameter
SET p040 = N.p_label,
p040_help = N.p_help,
p040_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 40;

UPDATE xcosblocks_block
SET p041_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 41;

UPDATE xcosblocks_blockparameter
SET p041 = N.p_label,
p041_help = N.p_help,
p041_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 41;

UPDATE xcosblocks_block
SET p042_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 42;

UPDATE xcosblocks_blockparameter
SET p042 = N.p_label,
p042_help = N.p_help,
p042_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 42;

UPDATE xcosblocks_block
SET p043_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 43;

UPDATE xcosblocks_blockparameter
SET p043 = N.p_label,
p043_help = N.p_help,
p043_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 43;

UPDATE xcosblocks_block
SET p044_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 44;

UPDATE xcosblocks_blockparameter
SET p044 = N.p_label,
p044_help = N.p_help,
p044_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 44;

UPDATE xcosblocks_block
SET p045_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 45;

UPDATE xcosblocks_blockparameter
SET p045 = N.p_label,
p045_help = N.p_help,
p045_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 45;

UPDATE xcosblocks_block
SET p046_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 46;

UPDATE xcosblocks_blockparameter
SET p046 = N.p_label,
p046_help = N.p_help,
p046_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 46;

UPDATE xcosblocks_block
SET p047_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 47;

UPDATE xcosblocks_blockparameter
SET p047 = N.p_label,
p047_help = N.p_help,
p047_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 47;

UPDATE xcosblocks_block
SET p048_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 48;

UPDATE xcosblocks_blockparameter
SET p048 = N.p_label,
p048_help = N.p_help,
p048_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 48;

UPDATE xcosblocks_block
SET p049_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 49;

UPDATE xcosblocks_blockparameter
SET p049 = N.p_label,
p049_help = N.p_help,
p049_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 49;

UPDATE xcosblocks_block
SET p050_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 50;

UPDATE xcosblocks_blockparameter
SET p050 = N.p_label,
p050_help = N.p_help,
p050_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 50;

UPDATE xcosblocks_block
SET p051_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 51;

UPDATE xcosblocks_blockparameter
SET p051 = N.p_label,
p051_help = N.p_help,
p051_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 51;

UPDATE xcosblocks_block
SET p052_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 52;

UPDATE xcosblocks_blockparameter
SET p052 = N.p_label,
p052_help = N.p_help,
p052_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 52;

UPDATE xcosblocks_block
SET p053_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 53;

UPDATE xcosblocks_blockparameter
SET p053 = N.p_label,
p053_help = N.p_help,
p053_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 53;

UPDATE xcosblocks_block
SET p054_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 54;

UPDATE xcosblocks_blockparameter
SET p054 = N.p_label,
p054_help = N.p_help,
p054_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 54;

UPDATE xcosblocks_block
SET p055_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 55;

UPDATE xcosblocks_blockparameter
SET p055 = N.p_label,
p055_help = N.p_help,
p055_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 55;

UPDATE xcosblocks_block
SET p056_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 56;

UPDATE xcosblocks_blockparameter
SET p056 = N.p_label,
p056_help = N.p_help,
p056_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 56;

UPDATE xcosblocks_block
SET p057_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 57;

UPDATE xcosblocks_blockparameter
SET p057 = N.p_label,
p057_help = N.p_help,
p057_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 57;

UPDATE xcosblocks_block
SET p058_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 58;

UPDATE xcosblocks_blockparameter
SET p058 = N.p_label,
p058_help = N.p_help,
p058_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 58;

UPDATE xcosblocks_block
SET p059_value_initial = N.p_value_initial
FROM (SELECT block_id, p_order, p_value_initial FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_block.id
AND N.p_order = 59;

UPDATE xcosblocks_blockparameter
SET p059 = N.p_label,
p059_help = N.p_help,
p059_type_id = N.p_type_id
FROM (SELECT block_id, p_order, p_label, p_help, p_type_id FROM xcosblocks_newblockparameter) AS N
WHERE N.block_id = xcosblocks_blockparameter.block_id
AND N.p_order = 59;

