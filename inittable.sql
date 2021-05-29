delete from esimblocks_blockparameter;
delete from esimblocks_blockport;
delete from esimblocks_block_categories;
delete from esimblocks_block;
delete from esimblocks_category;

ALTER TABLE esimblocks_blockparameter AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_blockport AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_block_categories AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_block AUTO_INCREMENT = 1;
ALTER TABLE esimblocks_category AUTO_INCREMENT = 1;

LOAD DATA LOCAL INFILE 'categories.csv'
    INTO TABLE esimblocks_category
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, name, sort_order, @tmp1);

select id into @esim_blocktype_id from esimblocks_blocktype where name = 'eSim';

LOAD DATA LOCAL INFILE 'categories-blocks.csv'
    INTO TABLE esimblocks_block
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @tmp1, name)
    SET block_width = 40, block_height = 40, blocktype_id = @esim_blocktype_id;

LOAD DATA LOCAL INFILE 'categories-blocks.csv'
    INTO TABLE esimblocks_block_categories
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @category_name, @block_name)
    SET block_id = (SELECT id FROM esimblocks_block WHERE name = @block_name and blocktype_id = @esim_blocktype_id), category_id = (SELECT id from esimblocks_category WHERE name = @category_name);

LOAD DATA LOCAL INFILE 'blocks-ports.csv'
    INTO TABLE esimblocks_blockport
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    (id, @block_name, port_number, port_name, port_order, port_type, port_orientation)
    SET block_id = (SELECT id FROM esimblocks_block WHERE name = @block_name and blocktype_id = @esim_blocktype_id);
