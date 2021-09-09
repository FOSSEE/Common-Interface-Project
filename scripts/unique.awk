#!/usr/bin/awk -f

BEGIN {
    MAIN_CATEGORY_BLOCKS_CSV = "data/main-category-blocks.tsv";
    CATEGORIES_BLOCKS_CSV = "data/categories-blocks.tsv";
    FS = "\t";
    OFS = "\t";
    split("", blocks);
    split("", allblocks);
    split("", allblocksline);
    lines = 0;
    otherlines = 0;
}

{
    category = $2;
    block = $3;
    blockprefix = $4;
    othercategories[++otherlines] = category;
    otherblocks[otherlines] = block;
    if (block in allblocks) {
        if (allblocks[block] == "Commonly Used Blocks") {
            allblocks[block] = category;
            allblocksline[block] = category "\t" block "\t" blockprefix;
        }
    } else {
        blocks[++lines] = block;
        allblocks[block] = category;
        allblocksline[block] = category "\t" block "\t" blockprefix;
    }
}

END {
    for (line = 1; line <= lines; line++) {
        block = blocks[line];
        print line, allblocksline[block] > MAIN_CATEGORY_BLOCKS_CSV;
    }
    for (line = 1; line <= otherlines; line++) {
        block = otherblocks[line];
        print line, othercategories[line], allblocks[block], block > CATEGORIES_BLOCKS_CSV;
    }
}
