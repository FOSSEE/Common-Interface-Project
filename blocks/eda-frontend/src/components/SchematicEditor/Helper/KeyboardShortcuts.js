/* eslint new-cap: ["error", {"newIsCapExceptionPattern": "^mx"}] */
import 'mxgraph/javascript/src/css/common.css'

import mxGraphFactory from 'mxgraph'
import { editorUndo, editorRedo, editorZoomIn, editorZoomOut, editorZoomAct } from './ToolbarTools'

const {
  mxKeyHandler,
  mxEvent,
  mxClient
} = new mxGraphFactory()

export default function keyboardShortcuts (graph) {
  const keyHandler = new mxKeyHandler(graph)

  keyHandler.getFunction = function (evt) {
    if (evt != null) {
      return (mxEvent.isControlDown(evt) || (mxClient.IS_MAC && evt.metaKey)) ? this.controlKeys[evt.keyCode] : this.normalKeys[evt.keyCode]
    }

    return null
  }

  // Delete - Del
  // keyHandler.bindKey(46, function (evt) {
  //   if (graph.isEnabled()) {
  //     graph.removeCells()
  //   }
  // })

  // Undo - Ctrl + Z
  keyHandler.bindControlKey(90, function (evt) {
    if (graph.isEnabled()) {
      editorUndo()
    }
  })

  // Redo - Ctrl + A
  keyHandler.bindControlKey(65, function (evt) {
    if (graph.isEnabled()) {
      editorRedo()
    }
  })

  // Zoom In - Ctrl + I
  keyHandler.bindControlKey(73, function (evt) {
    if (graph.isEnabled()) {
      editorZoomIn()
    }
  })

  // Zoom Out - Ctrl + O
  keyHandler.bindControlKey(79, function (evt) {
    if (graph.isEnabled()) {
      editorZoomOut()
    }
  })

  // Zoom Out - Ctrl + Y
  keyHandler.bindControlKey(89, function (evt) {
    if (graph.isEnabled()) {
      editorZoomAct()
    }
  })
}
