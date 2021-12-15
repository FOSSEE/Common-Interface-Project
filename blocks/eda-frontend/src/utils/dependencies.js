import mxGraphFactory from 'mxgraph'

const {
  mxClient,
  mxUtils,
  mxEvent,
  mxDivResizer,
  mxWindow,
  mxEffects,
  mxCodec
} = new mxGraphFactory()

// Added to handle ordering for a few blocks.

window.inBitMap='0';
window.outBitMap='0';

export function showModalWindow(graph, title, content, width, height) {
    const background = document.createElement('div');
    background.style.position = 'absolute';
    background.style.left = '0px';
    background.style.top = '0px';
    background.style.right = '0px';
    background.style.bottom = '0px';
    background.style.background = 'black';
    mxUtils.setOpacity(background, 50);
    document.body.appendChild(background);

    if (mxClient.IS_IE) {
        new mxDivResizer(background);
    }

    const x = Math.max(0, document.body.scrollWidth / 2 - width / 2);
    const y = Math.max(10, (document.body.scrollHeight || document.documentElement.scrollHeight) / 2 - height * 2 / 3);
    const wind = new mxWindow(title, content, x, y, width, height, false, true);
    wind.setClosable(true);

    // Fades the background out after after the window has been closed
    wind.addListener(mxEvent.DESTROY, function(evt) {
        graph.setEnabled(true);
        mxEffects.fadeOut(background, 50, true, 10, 30, true);
    });

    graph.setEnabled(false);
    graph.tooltipHandler.hide();
    wind.setVisible(true);
    return wind;
}

export function updateDetails(graph, cell, details, detailsInstance, styleName, geometryCell, create=false) {
    const enc = new mxCodec(mxUtils.createXmlDocument());
    const node = enc.encode(details);

    const fullStyleName = styleName;
    if (styleName != null) {
        const idx = styleName.indexOf(';');
        if (styleName.startsWith("SELF_SWITCH")) {
            const stateOpen = detailsInstance.stateOpen;
            styleName = stateOpen ? "SELF_SWITCH_OFF" : "SELF_SWITCH_ON";
        }else{
            if (idx !== -1) {
                styleName = styleName.substring(0, idx);
            }
        }
    }

    const stylesheet = graph.getStylesheet();
    const style = stylesheet.styles[styleName];

    const dimensionForBlock = detailsInstance.getDimensionForDisplay();
    const height = dimensionForBlock["height"];
    const width = dimensionForBlock["width"];
    if (geometryCell.height != null && geometryCell.height > 1)
        height = geometryCell.height;
    if (geometryCell.width != null && geometryCell.width > 1)
        width = geometryCell.width;

    /*
     * When a particular block is loaded for the first time, the image in the
     * style of the block will be a path to the image. Set the label in the
     * style property of the block has a html image, and set the image in the
     * style property as null
     *
     * NOTE: Since the image of any block need not be changed for every
     * movement of that block, the image must be set only once.
     */
    if (style != null && style['image'] != null) {
        // Make label as a image html element
        const label = '<img src="' + style['image'] + '" height="' + (height*0.9) + '" width="' + (width*0.9) + '">';

        // Set label
        style['label'] = label;
        style['imagePath'] = style['image'];
        // Set image as null
        style['image'] = null;

        // Add the label as a part of node
        node.setAttribute('label', label);
    }

    /*
     * If a particular block with image tag in its style property has been
     * invoked already, the image tag would be null for any successive
     * instances of the same block. Hence, set the label from the label tag in
     * style which was set when that blockModel was invoked on the first time.
     */
    if (style != null && style['label'] != null) {
        // Set label from the label field in the style property
        node.setAttribute('label', style['label']);
    }

    const parent = graph.getDefaultParent();
    node.setAttribute('parent', parent.id);

    if (create) {
        return graph.insertVertex(parent, null, node, geometryCell.x, geometryCell.y, width, height, fullStyleName);
    }

    cell.setValue(node);
}

// To convert graph points to array which have been converted
// to objects because of dragging the points
export function objToArrayList(graphPoints) {
    const tempPoints=[];
    for (let i=0;i< graphPoints.length; i++)
    {
        if(graphPoints[i].x) {
            tempPoints.push([graphPoints[i].x,graphPoints[i].y]);
        } else {
            tempPoints.push(graphPoints[i]);
        }
    }
    return tempPoints;
}

//For Sigbuilder block
export function getmethod(mtd){
    let METHOD = "";
    switch (mtd){
        case 0: METHOD = "zero order"; break;
        case 1: METHOD = "linear"; break;
        case 2: METHOD = "order 2"; break;
        case 3: METHOD = "not_a_knot"; break;
        case 4: METHOD = "periodic"; break;
        case 5: METHOD = "monotone"; break;
        case 6: METHOD = "fast"; break;
        case 7: METHOD = "clamped"; break;
        default: METHOD = "zero order"; break;
    }
    return METHOD;
}
