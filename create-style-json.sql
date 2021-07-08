SET @NewLineChar = CHAR(10);

SELECT '{';
SELECT CONCAT('  "defaultVertex": {', @NewLineChar,
              '    "shape": "label",', @NewLineChar,
              '    "perimeter": "rectanglePerimeter",', @NewLineChar,
              '    "strokeColor": "black",', @NewLineChar,
              '    "strokeWidth": 0.5,', @NewLineChar,
              '    "fillColor": "white",', @NewLineChar,
              '    "fontColor": "black",', @NewLineChar,
              '    "noLabel": 0', @NewLineChar,
              '  },');
SELECT CONCAT('  "defaultEdge": {', @NewLineChar,
              '    "labelBackgroundColor": "white",', @NewLineChar,
              '    "edgeStyle": "wireEdgeStyle",', @NewLineChar,
              '    "elbow": "horizontal",', @NewLineChar,
              '    "shape": "connector",', @NewLineChar,
              '    "endArrow": "classicnone",', @NewLineChar,
              '    "fontSize": 20,', @NewLineChar,
              '    "fontStyle": 0,', @NewLineChar,
              '    "align": "center",', @NewLineChar,
              '    "verticalAlign": "middle",', @NewLineChar,
              '    "strokeColor": "black",', @NewLineChar,
              '    "perimeter": "null"', @NewLineChar,
              '  },');
SELECT CONCAT('  "', B.main_category_id, '-', B.blockprefix_id, '-', B.name, '": {', @NewLineChar,
              '    "shape": "image",', @NewLineChar,
              '    "fontColor": "blue",', @NewLineChar,
              '    "imageVerticalAlign": "bottom",', @NewLineChar,
              '    "verticalAlign": "bottom",', @NewLineChar,
              '    "imageAlign": "bottom",', @NewLineChar,
              '    "align": "bottom",', @NewLineChar,
              '    "spacingLeft": 25,', @NewLineChar,
              '    "image": "/django_static/', C.name, '/', BP.name, '-', B.name, '-1-A.svg"', @NewLineChar,
              '  },')
    FROM esimblocks_block B
    JOIN esimblocks_blockprefix BP ON BP.id = B.blockprefix_id
    JOIN esimblocks_category C ON C.id = B.main_category_id
    ORDER BY C.sort_order, B.name;
SELECT '}';

