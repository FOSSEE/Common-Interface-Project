INSERT INTO xcosblocks_newblock (
    id, name, blockprefix_id, main_category_id, block_name, initial_display_parameter, simulation_function, block_image_path, block_width, block_height
)
SELECT id, name, blockprefix_id, main_category_id, block_name, initial_display_parameter, simulation_function, block_image_path, block_width, block_height
FROM xcosblocks_block;

INSERT INTO xcosblocks_newblock_categories (
    id, newblock_id, category_id
)
SELECT id, block_id, category_id
FROM xcosblocks_block_categories;

INSERT INTO xcosblocks_newblockparameter (
    block_id, p_order, p_label, p_type_id, p_help, p_value_initial
)
SELECT block_id, 0, p000, p000_type_id, p000_help, p000_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p000 IS NOT NULL
AND p000 != ''
UNION
SELECT block_id, 1, p001, p001_type_id, p001_help, p001_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p001 IS NOT NULL
AND p001 != ''
UNION
SELECT block_id, 2, p002, p002_type_id, p002_help, p002_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p002 IS NOT NULL
AND p002 != ''
UNION
SELECT block_id, 3, p003, p003_type_id, p003_help, p003_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p003 IS NOT NULL
AND p003 != ''
UNION
SELECT block_id, 4, p004, p004_type_id, p004_help, p004_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p004 IS NOT NULL
AND p004 != ''
UNION
SELECT block_id, 5, p005, p005_type_id, p005_help, p005_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p005 IS NOT NULL
AND p005 != ''
UNION
SELECT block_id, 6, p006, p006_type_id, p006_help, p006_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p006 IS NOT NULL
AND p006 != ''
UNION
SELECT block_id, 7, p007, p007_type_id, p007_help, p007_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p007 IS NOT NULL
AND p007 != ''
UNION
SELECT block_id, 8, p008, p008_type_id, p008_help, p008_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p008 IS NOT NULL
AND p008 != ''
UNION
SELECT block_id, 9, p009, p009_type_id, p009_help, p009_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p009 IS NOT NULL
AND p009 != ''
UNION
SELECT block_id, 10, p010, p010_type_id, p010_help, p010_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p010 IS NOT NULL
AND p010 != ''
UNION
SELECT block_id, 11, p011, p011_type_id, p011_help, p011_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p011 IS NOT NULL
AND p011 != ''
UNION
SELECT block_id, 12, p012, p012_type_id, p012_help, p012_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p012 IS NOT NULL
AND p012 != ''
UNION
SELECT block_id, 13, p013, p013_type_id, p013_help, p013_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p013 IS NOT NULL
AND p013 != ''
UNION
SELECT block_id, 14, p014, p014_type_id, p014_help, p014_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p014 IS NOT NULL
AND p014 != ''
UNION
SELECT block_id, 15, p015, p015_type_id, p015_help, p015_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p015 IS NOT NULL
AND p015 != ''
UNION
SELECT block_id, 16, p016, p016_type_id, p016_help, p016_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p016 IS NOT NULL
AND p016 != ''
UNION
SELECT block_id, 17, p017, p017_type_id, p017_help, p017_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p017 IS NOT NULL
AND p017 != ''
UNION
SELECT block_id, 18, p018, p018_type_id, p018_help, p018_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p018 IS NOT NULL
AND p018 != ''
UNION
SELECT block_id, 19, p019, p019_type_id, p019_help, p019_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p019 IS NOT NULL
AND p019 != ''
UNION
SELECT block_id, 20, p020, p020_type_id, p020_help, p020_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p020 IS NOT NULL
AND p020 != ''
UNION
SELECT block_id, 21, p021, p021_type_id, p021_help, p021_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p021 IS NOT NULL
AND p021 != ''
UNION
SELECT block_id, 22, p022, p022_type_id, p022_help, p022_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p022 IS NOT NULL
AND p022 != ''
UNION
SELECT block_id, 23, p023, p023_type_id, p023_help, p023_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p023 IS NOT NULL
AND p023 != ''
UNION
SELECT block_id, 24, p024, p024_type_id, p024_help, p024_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p024 IS NOT NULL
AND p024 != ''
UNION
SELECT block_id, 25, p025, p025_type_id, p025_help, p025_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p025 IS NOT NULL
AND p025 != ''
UNION
SELECT block_id, 26, p026, p026_type_id, p026_help, p026_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p026 IS NOT NULL
AND p026 != ''
UNION
SELECT block_id, 27, p027, p027_type_id, p027_help, p027_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p027 IS NOT NULL
AND p027 != ''
UNION
SELECT block_id, 28, p028, p028_type_id, p028_help, p028_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p028 IS NOT NULL
AND p028 != ''
UNION
SELECT block_id, 29, p029, p029_type_id, p029_help, p029_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p029 IS NOT NULL
AND p029 != ''
UNION
SELECT block_id, 30, p030, p030_type_id, p030_help, p030_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p030 IS NOT NULL
AND p030 != ''
UNION
SELECT block_id, 31, p031, p031_type_id, p031_help, p031_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p031 IS NOT NULL
AND p031 != ''
UNION
SELECT block_id, 32, p032, p032_type_id, p032_help, p032_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p032 IS NOT NULL
AND p032 != ''
UNION
SELECT block_id, 33, p033, p033_type_id, p033_help, p033_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p033 IS NOT NULL
AND p033 != ''
UNION
SELECT block_id, 34, p034, p034_type_id, p034_help, p034_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p034 IS NOT NULL
AND p034 != ''
UNION
SELECT block_id, 35, p035, p035_type_id, p035_help, p035_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p035 IS NOT NULL
AND p035 != ''
UNION
SELECT block_id, 36, p036, p036_type_id, p036_help, p036_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p036 IS NOT NULL
AND p036 != ''
UNION
SELECT block_id, 37, p037, p037_type_id, p037_help, p037_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p037 IS NOT NULL
AND p037 != ''
UNION
SELECT block_id, 38, p038, p038_type_id, p038_help, p038_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p038 IS NOT NULL
AND p038 != ''
UNION
SELECT block_id, 39, p039, p039_type_id, p039_help, p039_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p039 IS NOT NULL
AND p039 != ''
UNION
SELECT block_id, 40, p040, p040_type_id, p040_help, p040_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p040 IS NOT NULL
AND p040 != ''
UNION
SELECT block_id, 41, p041, p041_type_id, p041_help, p041_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p041 IS NOT NULL
AND p041 != ''
UNION
SELECT block_id, 42, p042, p042_type_id, p042_help, p042_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p042 IS NOT NULL
AND p042 != ''
UNION
SELECT block_id, 43, p043, p043_type_id, p043_help, p043_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p043 IS NOT NULL
AND p043 != ''
UNION
SELECT block_id, 44, p044, p044_type_id, p044_help, p044_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p044 IS NOT NULL
AND p044 != ''
UNION
SELECT block_id, 45, p045, p045_type_id, p045_help, p045_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p045 IS NOT NULL
AND p045 != ''
UNION
SELECT block_id, 46, p046, p046_type_id, p046_help, p046_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p046 IS NOT NULL
AND p046 != ''
UNION
SELECT block_id, 47, p047, p047_type_id, p047_help, p047_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p047 IS NOT NULL
AND p047 != ''
UNION
SELECT block_id, 48, p048, p048_type_id, p048_help, p048_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p048 IS NOT NULL
AND p048 != ''
UNION
SELECT block_id, 49, p049, p049_type_id, p049_help, p049_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p049 IS NOT NULL
AND p049 != ''
UNION
SELECT block_id, 50, p050, p050_type_id, p050_help, p050_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p050 IS NOT NULL
AND p050 != ''
UNION
SELECT block_id, 51, p051, p051_type_id, p051_help, p051_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p051 IS NOT NULL
AND p051 != ''
UNION
SELECT block_id, 52, p052, p052_type_id, p052_help, p052_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p052 IS NOT NULL
AND p052 != ''
UNION
SELECT block_id, 53, p053, p053_type_id, p053_help, p053_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p053 IS NOT NULL
AND p053 != ''
UNION
SELECT block_id, 54, p054, p054_type_id, p054_help, p054_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p054 IS NOT NULL
AND p054 != ''
UNION
SELECT block_id, 55, p055, p055_type_id, p055_help, p055_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p055 IS NOT NULL
AND p055 != ''
UNION
SELECT block_id, 56, p056, p056_type_id, p056_help, p056_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p056 IS NOT NULL
AND p056 != ''
UNION
SELECT block_id, 57, p057, p057_type_id, p057_help, p057_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p057 IS NOT NULL
AND p057 != ''
UNION
SELECT block_id, 58, p058, p058_type_id, p058_help, p058_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p058 IS NOT NULL
AND p058 != ''
UNION
SELECT block_id, 59, p059, p059_type_id, p059_help, p059_value_initial
FROM xcosblocks_block
JOIN xcosblocks_blockparameter ON xcosblocks_blockparameter.block_id = xcosblocks_block.id
WHERE p059 IS NOT NULL
AND p059 != ''
ORDER BY 1, 2;

INSERT INTO xcosblocks_newblockport (
    id, block_id, port_order, port_name, port_number, port_x, port_y, port_orientation, port_part, port_dmg, port_type
)
SELECT id, block_id, port_order, port_name, port_number, port_x, port_y, port_orientation, port_part, port_dmg, port_type
FROM xcosblocks_blockport;
