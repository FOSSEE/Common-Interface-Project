UPDATE xcosblocks_blockparameter
SET p000_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P000 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p001_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P001 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p002_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P002 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p003_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P003 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p004_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P004 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p005_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P005 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p007_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P007 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p008_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P008 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p009_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P009 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p010_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P010 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p012_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P012 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p013_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P013 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p014_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P014 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p014_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P014 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p015_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P015 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

UPDATE xcosblocks_blockparameter
SET p016_type_id = T.type_id
FROM (
    SELECT xcosblocks_blockparameter.id AS id, xcosblocks_parameterdatatype.id AS type_id
    FROM xcosblocks_blockparameter
    JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
    JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
    JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.name = tmp_block."P016 Type"
) AS T
WHERE xcosblocks_blockparameter.id = T.id;

SELECT 'P000', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P000 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p000_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P000 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P001', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P001 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p001_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P001 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P002', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P002 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p002_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P002 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P003', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P003 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p003_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P003 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P004', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P004 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p004_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P004 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P005', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P005 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p005_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P005 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P006', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P006 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p006_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P006 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P007', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P007 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p007_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P007 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P008', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P008 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p008_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P008 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P009', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P009 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p009_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P009 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P010', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P010 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p010_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P010 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P011', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P011 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p011_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P011 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P012', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P012 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p012_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P012 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P013', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P013 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p013_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P013 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P014', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P014 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p014_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P014 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P015', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P015 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p015_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P015 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P016', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P016 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p016_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P016 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P017', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P017 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p017_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P017 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P018', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P018 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p018_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P018 Type"
ORDER BY xcosblocks_block.name;

SELECT 'P019', xcosblocks_block.name, xcosblocks_parameterdatatype.name AS 'OLD TYPE', tmp_block."P019 Type" AS 'NEW TYPE'
FROM xcosblocks_blockparameter
JOIN xcosblocks_parameterdatatype ON xcosblocks_parameterdatatype.id = xcosblocks_blockparameter.p019_type_id
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_parameterdatatype.name != tmp_block."P019 Type"
ORDER BY xcosblocks_block.name;
