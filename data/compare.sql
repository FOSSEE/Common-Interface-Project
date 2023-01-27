UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003", p004 = T."P004",
p005 = T."P005", p006 = T."P006", p007 = T."P007", p008 = T."P008", p009 = T."P009",
p010 = T."P010", p011 = T."P011", p012 = T."P012", p013 = T."P013", p014 = T."P014",
p015 = T."P015", p016 = T."P016", p017 = T."P017", p018 = T."P018"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009",
tmp_block."P010", tmp_block."P011", tmp_block."P012", tmp_block."P013", tmp_block."P014",
tmp_block."P015", tmp_block."P016", tmp_block."P017", tmp_block."P018", tmp_block."P019"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CBLOCK4') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003", p004 = T."P004",
p005 = T."P005", p006 = T."P006", p007 = T."P007", p008 = T."P008", p009 = T."P009",
p010 = T."P010", p011 = T."P011", p012 = T."P012", p013 = T."P013"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009",
tmp_block."P010", tmp_block."P011", tmp_block."P012", tmp_block."P013", tmp_block."P014"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CBLOCK') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003", p004 = T."P004",
p005 = T."P005", p006 = T."P006", p007 = T."P007", p008 = T."P008", p009 = T."P009",
p010 = T."P010"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009",
tmp_block."P010", tmp_block."P011", tmp_block."P012", tmp_block."P013", tmp_block."P014"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CANIMXY') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p009 = T."P009"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CSCOPXY') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003", p004 = T."P004",
p005 = T."P005", p006 = T."P006", p007 = T."P007", p008 = T."P008"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CFSCOPE') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003", p004 = T."P004",
p005 = T."P005", p006 = T."P006", p007 = T."P007", p008 = T."P008"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'Bache') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003", p004 = T."P004",
p005 = T."P005", p006 = T."P006"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'AFFICH_m') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003", p004 = T."P004",
p005 = T."P005"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004",
tmp_block."P005", tmp_block."P006", tmp_block."P007", tmp_block."P008", tmp_block."P009"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'SUBMAT') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'SourceP') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'PuitsP') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002", p003 = T."P003"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'LOGICAL_OP') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'SUMMATION') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'RELATIONALOP') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MAXMIN') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATMUL') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CONSTRAINT2_c') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'ESELECT_f') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'BACKLASH') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'RICC') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'REGISTER') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'PRODUCT') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001", p002 = T."P002"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATRESH') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATTRAN') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATSUM') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATSING') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATEIG') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'IFTHEL_f') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CUMSUM') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'BITSET') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000", p001 = T."P001"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'BITCLEAR') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'SQRT') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'SIGNUM') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'ROOTCOEF') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATPINV') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATLU') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATINV') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATEXPM') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATDIV') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATDIAG') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATDET') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'MATBKSL') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

UPDATE xcosblocks_blockparameter
SET p000 = T."P000"
FROM (SELECT xcosblocks_block.id,
tmp_block."P000", tmp_block."P001", tmp_block."P002", tmp_block."P003", tmp_block."P004"
FROM xcosblocks_block
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE name = 'CONSTRAINT_c') AS T
WHERE xcosblocks_blockparameter.block_id = T.id;

SELECT 'P000', name, xcosblocks_blockparameter.p000, tmp_block."P000"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p000 != tmp_block."P000";

SELECT 'P001', name, xcosblocks_blockparameter.p001, tmp_block."P001"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p001 != tmp_block."P001";

SELECT 'P002', name, xcosblocks_blockparameter.p002, tmp_block."P002"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p002 != tmp_block."P002";

SELECT 'P003', name, xcosblocks_blockparameter.p003, tmp_block."P003"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p003 != tmp_block."P003";

SELECT 'P004', name, xcosblocks_blockparameter.p004, tmp_block."P004"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p004 != tmp_block."P004";

SELECT 'P005', name, xcosblocks_blockparameter.p005, tmp_block."P005"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p005 != tmp_block."P005";

SELECT 'P006', name, xcosblocks_blockparameter.p006, tmp_block."P006"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p006 != tmp_block."P006";

SELECT 'P007', name, xcosblocks_blockparameter.p007, tmp_block."P007"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p007 != tmp_block."P007";

SELECT 'P008', name, xcosblocks_blockparameter.p008, tmp_block."P008"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p008 != tmp_block."P008";

SELECT 'P009', name, xcosblocks_blockparameter.p009, tmp_block."P009"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p009 != tmp_block."P009";

SELECT 'P010', name, xcosblocks_blockparameter.p010, tmp_block."P010"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p010 != tmp_block."P010";

SELECT 'P011', name, xcosblocks_blockparameter.p011, tmp_block."P011"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p011 != tmp_block."P011";

SELECT 'P012', name, xcosblocks_blockparameter.p012, tmp_block."P012"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p012 != tmp_block."P012";

SELECT 'P013', name, xcosblocks_blockparameter.p013, tmp_block."P013"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p013 != tmp_block."P013";

SELECT 'P014', name, xcosblocks_blockparameter.p014, tmp_block."P014"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p014 != tmp_block."P014";

SELECT 'P015', name, xcosblocks_blockparameter.p015, tmp_block."P015"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p015 != tmp_block."P015";

SELECT 'P016', name, xcosblocks_blockparameter.p016, tmp_block."P016"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p016 != tmp_block."P016";

SELECT 'P017', name, xcosblocks_blockparameter.p017, tmp_block."P017"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p017 != tmp_block."P017";

SELECT 'P018', name, xcosblocks_blockparameter.p018, tmp_block."P018"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p018 != tmp_block."P018";

SELECT 'P019', name, xcosblocks_blockparameter.p019, tmp_block."P019"
FROM xcosblocks_blockparameter
JOIN xcosblocks_block ON xcosblocks_block.id = xcosblocks_blockparameter.block_id
JOIN tmp_block ON tmp_block."Block Name" = xcosblocks_block.name
WHERE xcosblocks_blockparameter.p019 != tmp_block."P019";
