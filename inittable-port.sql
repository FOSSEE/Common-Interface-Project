DROP TABLE IF EXISTS xcosblocks_newblockport_tmp;

CREATE TABLE xcosblocks_newblockport_tmp (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "category_name" varchar(100) NOT NULL,
    "block_name" varchar(100) NOT NULL,
    "port_order" integer NOT NULL,
    "port_name" varchar(100) NOT NULL,
    "port_number" varchar(10) NOT NULL,
    "port_x" integer NOT NULL,
    "port_y" integer NOT NULL,
    "port_orientation" varchar(100) NOT NULL,
    "port_part" integer NOT NULL,
    "port_dmg" integer NOT NULL,
    "port_type" varchar(100) NOT NULL,
    CONSTRAINT "unique_blocktemp_port_order" UNIQUE ("block_name", "port_order")
);

.mode csv
.separator "\t"
.import ../data/blocks-ports.tsv xcosblocks_newblockport_tmp

DELETE FROM xcosblocks_newblockport;

INSERT INTO xcosblocks_newblockport
    (id, block_id, port_order, port_name, port_number, port_x, port_y, port_orientation, port_part, port_dmg, port_type)
    SELECT xcosblocks_newblockport_tmp.id, xcosblocks_newblock.id, port_order, port_name, port_number, port_x, port_y, port_orientation, port_part, port_dmg, port_type
    FROM xcosblocks_newblockport_tmp
    JOIN xcosblocks_newblock ON xcosblocks_newblock.name = xcosblocks_newblockport_tmp.block_name;

DROP TABLE xcosblocks_newblockport_tmp;
