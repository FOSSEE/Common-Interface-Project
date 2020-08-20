import React, {Component} from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import {
    mxGraph,
    mxParallelEdgeLayout,
    mxConstants,
    mxEdgeStyle,
    mxLayoutManager,
    mxCell,
    mxGeometry,
    mxRubberband,
    mxDragSource,
    mxKeyHandler,
    mxCodec,
    mxClient,
    mxConnectionHandler,
    mxUtils,
    mxToolbar,
    mxEvent,
    mxImage,
    mxFastOrganicLayout
} from "mxgraph";


export default class MxGraphGridAreaEditor extends Component {
    constructor(props) {
        super(props);
        this.state = {

        };
        this.LoadGraph = this
            .LoadGraph
            .bind(this);
    }


    LoadGraph(data) {
        var container = ReactDOM.findDOMNode(this.refs.divGraph);
        var zoomPanel = ReactDOM.findDOMNode(this.refs.divZoom);

        // Checks if the browser is supported
        if (!mxClient.isBrowserSupported()) {
            // Displays an error message if the browser is not supported.
            mxUtils.error("Browser is not supported!", 200, false);
        } else {
            // Disables the built-in context menu
            mxEvent.disableContextMenu(container);

            // Creates the graph inside the given container
            var graph = new mxGraph(container);

            // Enables rubberband selection
            new mxRubberband(graph);

            // Gets the default parent for inserting new cells. This is normally the first
            // child of the root (ie. layer 0).
            var parent = graph.getDefaultParent();
            // Enables tooltips, new connections and panning
            graph.setPanning(true);
            //graph.setTooltips(true); graph.setConnectable(true);
            graph.setEnabled(false);

            // Autosize labels on insert where autosize=1
            graph.autoSizeCellsOnAdd = true;

            // Allows moving of relative cells
            graph.isCellLocked = function (cell) {
                return this.isCellsLocked();
            };

            graph.isCellResizable = function (cell) {
                var geo = this
                    .model
                    .getGeometry(cell);

                return geo == null || !geo.relative;
            };

            // Truncates the label to the size of the vertex
            graph.getLabel = function (cell) {
                var label = this.labelsVisible
                    ? this.convertValueToString(cell)
                    : "";
                var geometry = this
                    .model
                    .getGeometry(cell);

                if (!this.model.isCollapsed(cell) && geometry != null && (geometry.offset == null || (geometry.offset.x == 0 && geometry.offset.y == 0)) && this.model.isVertex(cell) && geometry.width >= 2) {
                    var style = this.getCellStyle(cell);
                    var fontSize = style[mxConstants.STYLE_FONTSIZE] || mxConstants.DEFAULT_FONTSIZE;
                    var max = geometry.width / (fontSize * 0.625);

                    if (max < label.length) {
                        return label.substring(0, max) + "...";
                    }
                }

                return label;
            };

            // Enables wrapping for vertex labels
            graph.isWrapping = function (cell) {
                return this
                    .model
                    .isCollapsed(cell);
            };

            // Enables clipping of vertex labels if no offset is defined
            graph.isLabelClipped = function (cell) {
                var geometry = this
                    .model
                    .getGeometry(cell);

                return (geometry != null && !geometry.relative && (geometry.offset == null || (geometry.offset.x == 0 && geometry.offset.y == 0)));
            };
            var layout = new mxParallelEdgeLayout(graph);

            // Moves stuff wider apart than usual
            layout.forceConstant = 140;
            //// Adds cells to the model in a single step
            graph
                .getModel()
                .beginUpdate();
            try {

				//mxGrapg componnent
                var doc = mxUtils.createXmlDocument();
                var node = doc.createElement('YES')
                node.setAttribute('ComponentID', '[P01]');

                var vx = graph.insertVertex(graph.getDefaultParent(), null, node, 240, 40, 150, 30);

                var v1 = graph.insertVertex(parent, null, 'Example_Shape_01', 20, 120, 80, 30);
                var v2 = graph.insertVertex(parent, null, 'Example_Shape_02', 300, 120, 80, 30);
                var v3 = graph.insertVertex(parent, null, 'Example_Shape_03', 620, 180, 80, 30);
                var e1 = graph.insertEdge(parent, null, 'Example Edge name_01', v1, v2);
                var e2 = graph.insertEdge(parent, null, 'Example Edge name_02', v2, v3);
                var e3 = graph.insertEdge(parent, null, 'Example Edge name_02', v1, v3);


                // Gets the default parent for inserting new cells. This is normally the first
                // child of the root (ie. layer 0).
                var parent = graph.getDefaultParent();

                // Executes the layout
                layout.execute(parent);
                //data
            } finally {
                // Updates the display
                graph
                    .getModel()
                    .endUpdate();
            }

            // Automatically handle parallel edges
            var layout = new mxParallelEdgeLayout(graph);
            var layoutMgr = new mxLayoutManager(graph);

            // Enables rubberband (marquee) selection and a handler for basic keystrokes
            var rubberband = new mxRubberband(graph);
            var keyHandler = new mxKeyHandler(graph);
        }
    }

    render() {
        return (
                <div className="graph-container" ref="divGraph" id="divGraph"/>
                );
    }
}
