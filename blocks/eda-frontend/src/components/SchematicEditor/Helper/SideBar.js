/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import 'mxgraph/javascript/src/css/common.css'

import mxGraphFactory from 'mxgraph'
import { defaultScale, getSvgMetadata } from './SvgParser.js'

const {
  mxClient,
  mxUtils,
  mxEvent,
  mxDragSource
} = new mxGraphFactory()

let graph

export function sideBar (getGraph) {
  graph = getGraph
}

export function AddComponent (component, imgref) {
  const img = imgref

  const graphF = function (evt) {
    const x = mxEvent.getClientX(evt)
    const y = mxEvent.getClientY(evt)
    const elt = document.elementFromPoint(x, y)
    if (mxUtils.isAncestorNode(graph.container, elt)) {
      return graph
    }
    return null
  }
  const funct = function (graph, evt, target, x, y) {
    const parent = graph.getDefaultParent()
    const model = graph.getModel()

    const v1 = null

    model.beginUpdate()
    try {
      // NOTE: For non-HTML labels the image must be displayed via the style
      // rather than the label markup, so use 'image=' + image for the style.
      // as follows: v1 = graph.insertVertex(parent, null, label,
      // pt.x, pt.y, 120, 120, 'image=' + image)

      // ***IMP
      // GET THE SIZE OF SVG FOROM METADATA AND THEN DIVIDE BOTH WIDTH AND HEIGHT BE SAME RATIO
      // THEN USE THAT VALUE BELOW

      getSvgMetadata(graph, parent, evt, target, x, y, component)

      // **IMP VERTICS DRAWING IS MOVED TO xml_parser.js
      // WILL BE REFACTORED IN SOME TIME.
    } finally {
      model.endUpdate()
    }

    graph.setSelectionCell(v1)
    /* const preview = new mxPrintPreview(graph)
    preview.open() */
  }

  // Creates a DOM node that acts as the drag source
  // Disables built-in DnD in IE (this is needed for cross-frame DnD, see below)
  if (mxClient.IS_IE) {
    mxEvent.addListener(img, 'dragstart', function (evt) {
      evt.returnValue = false
    })
  }

  // Creates the element that is being for the actual preview.
  const dragElt = document.createElement('div')
  dragElt.style.border = 'dashed black 1px'
  dragElt.style.width = (component.block_width / defaultScale) + 'px'
  dragElt.style.height = (component.block_height / defaultScale) + 'px'

  // Drag source is configured to use dragElt for preview and as drag icon
  // if scalePreview (last) argument is true. Dx and dy are null to force
  // the use of the defaults. Note that dx and dy are only used for the
  // drag icon but not for the preview.

  const ds = mxUtils.makeDraggable(
    img,
    graphF,
    funct,
    dragElt,
    null,
    null,
    graph.autoscroll,
    true
  )

  // Redirects feature to global switch. Note that this feature should only be used
  // if the the x and y arguments are used in funct to insert the cell.
  ds.isGuidesEnabled = function () {
    return graph.graphHandler.guidesEnabled
  }

  ds.createDragElement = mxDragSource.prototype.createDragElement
}
