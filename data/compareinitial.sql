UPDATE xcosblocks_block
SET p000_value_initial = T."P000 Default"
FROM (SELECT "Block Name", "P000 Default" FROM tmp_block WHERE "P000 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p001_value_initial = T."P001 Default"
FROM (SELECT "Block Name", "P001 Default" FROM tmp_block WHERE "P001 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p002_value_initial = T."P002 Default"
FROM (SELECT "Block Name", "P002 Default" FROM tmp_block WHERE "P002 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p003_value_initial = T."P003 Default"
FROM (SELECT "Block Name", "P003 Default" FROM tmp_block WHERE "P003 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p004_value_initial = T."P004 Default"
FROM (SELECT "Block Name", "P004 Default" FROM tmp_block WHERE "P004 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p005_value_initial = T."P005 Default"
FROM (SELECT "Block Name", "P005 Default" FROM tmp_block WHERE "P005 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p006_value_initial = T."P006 Default"
FROM (SELECT "Block Name", "P006 Default" FROM tmp_block WHERE "P006 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p007_value_initial = T."P007 Default"
FROM (SELECT "Block Name", "P007 Default" FROM tmp_block WHERE "P007 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p008_value_initial = T."P008 Default"
FROM (SELECT "Block Name", "P008 Default" FROM tmp_block WHERE "P008 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p009_value_initial = T."P009 Default"
FROM (SELECT "Block Name", "P009 Default" FROM tmp_block WHERE "P009 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p010_value_initial = T."P010 Default"
FROM (SELECT "Block Name", "P010 Default" FROM tmp_block WHERE "P010 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p011_value_initial = T."P011 Default"
FROM (SELECT "Block Name", "P011 Default" FROM tmp_block WHERE "P011 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p012_value_initial = T."P012 Default"
FROM (SELECT "Block Name", "P012 Default" FROM tmp_block WHERE "P012 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p013_value_initial = T."P013 Default"
FROM (SELECT "Block Name", "P013 Default" FROM tmp_block WHERE "P013 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p014_value_initial = T."P014 Default"
FROM (SELECT "Block Name", "P014 Default" FROM tmp_block WHERE "P014 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p015_value_initial = T."P015 Default"
FROM (SELECT "Block Name", "P015 Default" FROM tmp_block WHERE "P015 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p016_value_initial = T."P016 Default"
FROM (SELECT "Block Name", "P016 Default" FROM tmp_block WHERE "P016 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p017_value_initial = T."P017 Default"
FROM (SELECT "Block Name", "P017 Default" FROM tmp_block WHERE "P017 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

UPDATE xcosblocks_block
SET p018_value_initial = T."P018 Default"
FROM (SELECT "Block Name", "P018 Default" FROM tmp_block WHERE "P018 Default" != '') AS T
WHERE xcosblocks_block.name = T."Block Name";

SELECT 'P000', name, p000_value_initial, "P000 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p000_value_initial != "P000 Default"
ORDER BY name;

SELECT 'P001', name, p001_value_initial, "P001 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p001_value_initial != "P001 Default"
ORDER BY name;

SELECT 'P002', name, p002_value_initial, "P002 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p002_value_initial != "P002 Default"
ORDER BY name;

SELECT 'P003', name, p003_value_initial, "P003 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p003_value_initial != "P003 Default"
ORDER BY name;

SELECT 'P004', name, p004_value_initial, "P004 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p004_value_initial != "P004 Default"
ORDER BY name;

SELECT 'P005', name, p005_value_initial, "P005 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p005_value_initial != "P005 Default"
ORDER BY name;

SELECT 'P006', name, p006_value_initial, "P006 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p006_value_initial != "P006 Default"
ORDER BY name;

SELECT 'P007', name, p007_value_initial, "P007 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p007_value_initial != "P007 Default"
ORDER BY name;

SELECT 'P008', name, p008_value_initial, "P008 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p008_value_initial != "P008 Default"
ORDER BY name;

SELECT 'P009', name, p009_value_initial, "P009 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p009_value_initial != "P009 Default"
ORDER BY name;

SELECT 'P010', name, p010_value_initial, "P010 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p010_value_initial != "P010 Default"
ORDER BY name;

SELECT 'P011', name, p011_value_initial, "P011 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p011_value_initial != "P011 Default"
ORDER BY name;

SELECT 'P012', name, p012_value_initial, "P012 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p012_value_initial != "P012 Default"
ORDER BY name;

SELECT 'P013', name, p013_value_initial, "P013 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p013_value_initial != "P013 Default"
ORDER BY name;

SELECT 'P014', name, p014_value_initial, "P014 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p014_value_initial != "P014 Default"
ORDER BY name;

SELECT 'P015', name, p015_value_initial, "P015 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p015_value_initial != "P015 Default"
ORDER BY name;

SELECT 'P016', name, p016_value_initial, "P016 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p016_value_initial != "P016 Default"
ORDER BY name;

SELECT 'P017', name, p017_value_initial, "P017 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p017_value_initial != "P017 Default"
ORDER BY name;

SELECT 'P018', name, p018_value_initial, "P018 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p018_value_initial != "P018 Default"
ORDER BY name;

SELECT 'P019', name, p019_value_initial, "P019 Default"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE p019_value_initial != "P019 Default"
ORDER BY name;
