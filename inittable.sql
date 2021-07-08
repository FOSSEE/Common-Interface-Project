delete from esimblocks_blockparameter;
delete from esimblocks_blockport;
delete from esimblocks_block_categories;
delete from esimblocks_block;
delete from esimblocks_blockprefix;
delete from esimblocks_category;

ALTER TABLE esimblocks_blockparameter AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_blockport AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_block_categories AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_block AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_blockprefix AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_category AUTO_INCREMENT = 1;

LOAD DATA LOCAL INFILE 'categories.csv'
    INTO TABLE esimblocks_category
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, name, sort_order, @tmp1);

SELECT id INTO @esim_blocktype_id FROM esimblocks_blocktype WHERE name = 'eSim';

LOAD DATA LOCAL INFILE 'blockprefixes.csv'
    INTO TABLE esimblocks_blockprefix
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, name, @tmp2);

LOAD DATA LOCAL INFILE 'categories-blocks.csv'
    INTO TABLE esimblocks_block
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @category_name, name, @blockprefix_name)
    SET block_width = 40,
    block_height = 40,
    blocktype_id = @esim_blocktype_id,
    blockprefix_id = (SELECT id FROM esimblocks_blockprefix WHERE name = @blockprefix_name),
    main_category_id = (SELECT id from esimblocks_category WHERE name = @category_name);

LOAD DATA LOCAL INFILE 'categories-blocks.csv'
    INTO TABLE esimblocks_block_categories
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @category_name, @block_name, @blockprefix_name)
    SET block_id = (SELECT esimblocks_block.id FROM esimblocks_block JOIN esimblocks_category ON main_category_id = esimblocks_category.id WHERE esimblocks_block.name = @block_name AND esimblocks_category.name = @category_name AND blocktype_id = @esim_blocktype_id),
    category_id = (SELECT id from esimblocks_category WHERE name = @category_name);

LOAD DATA LOCAL INFILE 'blocks-ports.csv'
    INTO TABLE esimblocks_blockport
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @category_name, @block_name, port_order, port_name, port_number, port_x, port_y, port_orientation, port_part, port_dmg, port_type)
    SET block_id = (SELECT esimblocks_block.id FROM esimblocks_block JOIN esimblocks_category ON main_category_id = esimblocks_category.id WHERE esimblocks_block.name = @block_name AND esimblocks_category.name = @category_name AND blocktype_id = @esim_blocktype_id);

UPDATE esimblocks_block B
    JOIN esimblocks_blockprefix BP ON BP.id = B.blockprefix_id
    JOIN esimblocks_block_categories BC ON B.id = BC.block_id
    JOIN esimblocks_category C ON BC.category_id = C.id
    SET B.block_image_path = CONCAT(C.name, '/', BP.name, '-', B.name, '-1-A.svg');

CREATE TEMPORARY TABLE tmp_esimblocks_block (
    id int NOT NULL PRIMARY KEY,
    block_width int NOT NULL,
    block_height int NOT NULL
);

LOAD DATA LOCAL INFILE 'getsize.csv'
    INTO TABLE tmp_esimblocks_block
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (@category_name, @block_name, block_width, block_height)
    SET id = (SELECT esimblocks_block.id FROM esimblocks_block JOIN esimblocks_category ON main_category_id = esimblocks_category.id WHERE esimblocks_block.name = @block_name AND esimblocks_category.name = @category_name AND blocktype_id = @esim_blocktype_id);

UPDATE esimblocks_block B
    JOIN tmp_esimblocks_block TB ON TB.id = B.id
    SET B.block_width = TB.block_width,
    B.block_height = TB.block_height;
