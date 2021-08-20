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
SELECT CONCAT('  "pinD": {', @NewLineChar,
              '    "align": "right",', @NewLineChar,
              '    "verticalAlign": "bottom",', @NewLineChar,
              '    "rotation": 0', @NewLineChar,
              '  },');
SELECT CONCAT('  "pinL": {', @NewLineChar,
              '    "align": "right",', @NewLineChar,
              '    "verticalAlign": "bottom",', @NewLineChar,
              '    "rotation": 0', @NewLineChar,
              '  },');
SELECT CONCAT('  "pinR": {', @NewLineChar,
              '    "align": "left",', @NewLineChar,
              '    "verticalAlign": "bottom",', @NewLineChar,
              '    "rotation": 0', @NewLineChar,
              '  },');
SELECT CONCAT('  "pinU": {', @NewLineChar,
              '    "align": "right",', @NewLineChar,
              '    "verticalAlign": "top",', @NewLineChar,
              '    "rotation": 0', @NewLineChar,
              '  },');
SELECT CONCAT('  "', C.name, '-', BP.name, '-', B.name, '": {', @NewLineChar,
              '    "shape": "image",', @NewLineChar,
              '    "fontColor": "blue",', @NewLineChar,
              '    "imageVerticalAlign": "bottom",', @NewLineChar,
              '    "verticalAlign": "bottom",', @NewLineChar,
              '    "imageAlign": "bottom",', @NewLineChar,
              '    "align": "bottom",', @NewLineChar,
              '    "spacingLeft": 25,', @NewLineChar,
              '    "image": "/django_static/', C.name, '/', BP.name, '-', B.name, '-1-A.svg"', @NewLineChar,
              '  },')
    FROM xcosblocks_block B
    JOIN xcosblocks_blockprefix BP ON BP.id = B.blockprefix_id
    JOIN xcosblocks_category C ON C.id = B.main_category_id
    ORDER BY C.sort_order, B.name;
SELECT '}';
