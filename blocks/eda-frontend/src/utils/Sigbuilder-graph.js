import mxGraphFactory from 'mxgraph'
import Highcharts from 'highcharts'
import { getmethod, showModalWindow } from './dependencies'

const {
    mxEvent
} = new mxGraphFactory()

export let graph_sigbuilder = "";
export let sigbuilderGraph = "";

let wind = "";

// Function to create a chart with responsive points for Sigbuilder
function createDraggablePointsChartSigbuilder (graphParameters, pointsHistory, xmin, xmax, ymin, ymax, chart_type, points, method, xmaxtitle, step, stepname) {
    graphParameters.mtd = method;
    const subtitle = updateSubtitleForSigbuilderGraph(points, graphParameters.mtd, xmaxtitle, graphParameters.PeriodicOption);
    pointsHistory.push(graphParameters.graphPoints.slice());

    let sigbuilderGraph = Highcharts.chart('drag_sig_chart', {
        chart: {
            type: chart_type,
            animation: false,
            events: {
                click: function (e) {
                    const xValue = e.xAxis[0].value;
                    const yValue = e.yAxis[0].value;
                    addPointsOnChart(sigbuilderGraph, graphParameters, pointsHistory, xValue, yValue);
                }
            }
        },
        tooltip: {
            enabled: false
        },
        title: {
            text: ""
        },
        subtitle: {
            text: subtitle
        },

        yAxis: {
            title: {
                text: 'Output'
            },
            min: parseFloat(ymin),
            max: parseFloat(ymax),
            gridLineWidth: 1,
            gridLineDashStyle: 'dash'
        },

        xAxis: {
            title: {
                text: 'time'
            },
            min: parseFloat(xmin),
            max: parseFloat(xmax),
            gridLineWidth: 1,
            gridLineDashStyle: 'dash'
        },

        plotOptions: {
            series: {
                point: {
                    events: {
                        drag: function (e) {
                            if (e.y >= ymax) {
                                this.y = ymax;
                                return false;
                            }
                            if (e.y <= ymin) {
                                this.y = ymin;
                                return false;
                            }
                            if (e.x >= xmax) {
                                this.x = xmax;
                                return false;
                            }
                            if (e.x <= xmin) {
                                this.x = xmin;
                                return false;
                            }
                        },
                        drop: function (e) {
                            pointsHistory.push(graphParameters.graphPoints.slice());
                        },
                        dblclick: function (e) {
                            const graphObject = e;
                            editPointsValue(graphObject, graph_sigbuilder, sigbuilderGraph, graphParameters, pointsHistory);
                        },
                        contextmenu: function (e) {
                            const graphObject = e;
                            removePointsFromChart(graphObject, sigbuilderGraph, graphParameters, pointsHistory);
                        }
                    },
                    stickyTracking: false
                },
                column: {
                    stacking: 'normal'
                },
                marker: {
                    enabled: true,
                    symbol: 'url(../images/plus-icon.png)'
                }
            }
        },
        series: [{
            draggableX: true,
            draggableY: true,
            showInLegend: false,
            data: graphParameters.graphPoints,
            step: step,
            name: stepname
        }]
    });
    return sigbuilderGraph;
};

export function updateSubtitleForSigbuilderGraph (points, method, xmaxtitle, periodicFlag) {

    let subTitle = "";
    if (periodicFlag == "y") {
        subTitle = "<b>" + points + " points, Method: " + getmethod(method) + ", periodic, T = " + xmaxtitle + "</b>";
    } else {
        subTitle = "<b>" + points + " points, Method: " + getmethod(method) + ", aperiodic</b>";
    }
    return subTitle;
}

function autoscaleFunctionalityForGraph (sigbuilderGraph, graphParameters, pointsHistory) {
    //Added for postive/maximum value autoscale functionality
        const maxXValueNew = sigbuilderGraph.xAxis[0].getExtremes().dataMax; //get max x point's value
        const minXValueNew = sigbuilderGraph.xAxis[0].getExtremes().dataMin; //get min x point's value
        const maxYValueNew = sigbuilderGraph.yAxis[0].getExtremes().dataMax; //get max y point's value
        const minYValueNew = sigbuilderGraph.yAxis[0].getExtremes().dataMin; //get min y point's value
        const diffX = ((Math.abs(maxXValueNew - minXValueNew)) / 100) * 10;
        const diffY = ((Math.abs(maxYValueNew - minYValueNew)) / 100) * 10;
        graphParameters.xmin = 0; //set min x axis value
        graphParameters.xmax = maxXValueNew + diffX; //set max x axis value
        if (minYValueNew > 0) {
            minYValueNew = 0;
        }
        graphParameters.ymin = minYValueNew - diffY; //set min y axis value
        graphParameters.ymax = maxYValueNew + diffY; //set max y axis value
        graphParameters.points = graphParameters.graphPoints.length;
        sigbuilderGraph = createDraggablePointsChartSigbuilder(graphParameters, pointsHistory, graphParameters.xmin, graphParameters.xmax, graphParameters.ymin, graphParameters.ymax, graphParameters.chartType, graphParameters.points, graphParameters.mtd, graphParameters.xmaxTitle, graphParameters.step, graphParameters.stepname);
}

export function editPointsValue (graphObject, graph, sigbuilderGraph, graphParameters, pointsHistory) {

    document.getElementById("messageLabel").innerHTML = "";
    //Making graph window inaccessible
    const graphWind = document.getElementById("graphcontentwind");
    graphWind.style.pointerEvents = "none";
    // Create basic structure for the form
    const content = document.createElement('div');
    content.setAttribute("id", "editCoordinates");

    // Add Form
    const myform = document.createElement("form");
    myform.method = "post";
    myform.id = "formEditCoordinate";
    myform.style.padding = "10px";

    const titlelabel = document.createElement('span');
    titlelabel.innerHTML = "Enter new x and y";
    myform.appendChild(titlelabel);
    // Line break
    const linebreak = document.createElement('br');
    myform.appendChild(linebreak);
    myform.appendChild(linebreak);

    const keys = Object.keys(graphObject.point.options);
    const len = keys.length;
    for (let i = 0; i < len; i++) {
        // Input Title
        const namelabel = document.createElement('label');
        namelabel.innerHTML = keys[i].toString();
        namelabel.style.marginLeft = "30px";
        myform.appendChild(namelabel);

        let value = 0;
        if (((graphObject.point.options[keys[i]]).toString()).includes(".")) {
            value = (graphObject.point.options[keys[i]]).toFixed(6);
        } else {
            value = (graphObject.point.options[keys[i]]);
        }
        // Input
        const input = document.createElement("input");
        input.name = "edit_" + keys[i];
        input.value = value;
        input.setAttribute("id", "edit_" + keys[i]);
        input.setAttribute("class", "fieldInput");
        myform.appendChild(input);

        myform.appendChild(linebreak);
        myform.appendChild(linebreak);

    }

    myform.appendChild(linebreak);

    // Button - Cancel
    const cancelBtn = document.createElement("button");
    cancelBtn.style.cssFloat = "right";
    cancelBtn.innerHTML = 'Cancel';
    cancelBtn.type = "button";
    cancelBtn.name = "Cancel";
    myform.appendChild(cancelBtn);

    // Button - OK
    const okBtn = document.createElement("button");
    okBtn.style.cssFloat = "right";
    okBtn.style.marginRight = "20px";
    okBtn.innerHTML = 'OK';
    okBtn.type = "button";
    okBtn.name = "OK";

    myform.appendChild(okBtn);
    content.appendChild(myform);
    const height = 150;
    wind = showModalWindow(graph, 'Scilab Multiple Values Request', content, 200, height);
    wind.addListener(mxEvent.DESTROY, function (evt) {
        graphWind.style.pointerEvents = "auto";
    });
    // Executes when button 'cancelBtn' is clicked
    cancelBtn.onclick = function () {
        document.getElementById("messageLabel").innerHTML = "";
        graphWind.style.pointerEvents = "auto";
        wind.destroy();
    };
    // Executes when button 'okBtn' is clicked
    okBtn.onclick = function () {
        let xValue = parseFloat(document.getElementById("edit_x").value);
        if (xValue < 0) {
            xValue = 0;
        }
        let yValue = parseFloat(document.getElementById("edit_y").value);
        const points = graphParameters.graphPoints;
        const xArry = [];
        for (let i = 0; i < points.length; i++) {
            xArry[i] = points[i][0];
        }
        xArry[points.length] = xValue;
        const result = checkDuplicateXValues(xArry);
        const mtdCheck = [0, 1, 2].includes(graphParameters.mtd);
        if (result) {
            removePointsFromChart(graphObject, sigbuilderGraph, graphParameters, pointsHistory);
            addPointsOnChart(sigbuilderGraph, graphParameters, pointsHistory, xValue, yValue);
            autoscaleFunctionalityForGraph(sigbuilderGraph, graphParameters, pointsHistory);
            document.getElementById("messageLabel").innerHTML = "";
            graphWind.style.pointerEvents = "auto";
            wind.destroy();
        } else {
            if (mtdCheck) {
                removePointsFromChart(graphObject, sigbuilderGraph, graphParameters, pointsHistory);
                addPointsOnChart(sigbuilderGraph, graphParameters, pointsHistory, xValue, yValue);
                autoscaleFunctionalityForGraph(sigbuilderGraph, graphParameters, pointsHistory);
                document.getElementById("messageLabel").innerHTML = "";
                graphWind.style.pointerEvents = "auto";
                wind.destroy();
            } else {
                document.getElementById("messageLabel").innerHTML = "ERROR IN SPLINE : " + getmethod(graphParameters.mtd);
                wind.destroy();
                graphWind.style.pointerEvents = "auto";
                throw "incorrect";
            }
        }
    };
}

export function removePointsFromChart (graphObject, sigbuilderGraph, graphParameters, pointsHistory) {
    const counter = graphObject.point.index;
    sigbuilderGraph.series[0].data[counter].remove();
    pointsHistory.push(graphParameters.graphPoints.slice());
    graphParameters.points = sigbuilderGraph.series[0].data.length;
    graphParameters.xmaxTitle = sigbuilderGraph.xAxis[0].getExtremes().dataMax.toFixed(6);
    sigbuilderGraph.setTitle(null, { text: updateSubtitleForSigbuilderGraph(graphParameters.points, graphParameters.mtd, graphParameters.xmaxTitle, graphParameters.PeriodicOption)});
}

export function addPointsOnChart (sigbuilderGraph, graphParameters, pointsHistory, xValue, yValue) {
    document.getElementById("messageLabel").innerHTML = "";
    if (xValue == 0 && yValue == 0) {
        graphParameters.flag_for_zeros = true;
    }
    const points = graphParameters.graphPoints;
    const xArry = [];
    for (let i = 0; i < points.length; i++) {
        xArry[i] = points[i][0];
    }
    xArry[points.length] = xValue;
    const result = checkDuplicateXValues(xArry);
    const mtdCheck = [0, 1, 2].includes(graphParameters.mtd);
    if (result) {
        sigbuilderGraph.series[0].addPoint([xValue, yValue]);
        pointsHistory.push(graphParameters.graphPoints.slice());
        graphParameters.points = sigbuilderGraph.series[0].data.length;
        graphParameters.xmaxTitle = sigbuilderGraph.xAxis[0].getExtremes().dataMax.toFixed(6);
        sigbuilderGraph.setTitle(null, { text: updateSubtitleForSigbuilderGraph(graphParameters.points, graphParameters.mtd,   graphParameters.xmaxTitle, graphParameters.PeriodicOption)});
    } else {
        if (mtdCheck) {
            sigbuilderGraph.series[0].addPoint([xValue, yValue]);
            pointsHistory.push(graphParameters.graphPoints.slice());
            graphParameters.points = sigbuilderGraph.series[0].data.length;
            graphParameters.xmaxTitle = sigbuilderGraph.xAxis[0].getExtremes().dataMax.toFixed(6);
            sigbuilderGraph.setTitle(null, { text: updateSubtitleForSigbuilderGraph(graphParameters.points, graphParameters.mtd,   graphParameters.xmaxTitle, graphParameters.PeriodicOption)});
        } else {
            document.getElementById("messageLabel").innerHTML = "ERROR IN SPLINE : " + getmethod(graphParameters.mtd);
            throw "incorrect";
        }
    }
}

function checkDuplicateXValues (xxArry) {
    const arrayForCompare = [];
    const result = xxArry.slice(0).every(function (item, index, array) {
        if (arrayForCompare.indexOf(item) > -1) {
            array.length = 0;
            return false;
        } else {
            arrayForCompare.push(item);
            return true;
        }
    });
    return result;
}
