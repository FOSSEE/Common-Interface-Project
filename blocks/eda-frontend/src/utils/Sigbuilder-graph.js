import mxGraphFactory from 'mxgraph'
import Highcharts from 'highcharts'
import { getmethod, showModalWindow } from './dependencies'

const {
    mxEvent
} = new mxGraphFactory()

export var graph_sigbuilder = "";
export var sigbuilder_Graph = "";

var wind = "";

// Function to create a chart with responsive points for Sigbuilder
var create_draggable_points_chart_sigbuilder = function(graphParameters, pointsHistory, xmin, xmax, ymin, ymax, chart_type, points, method, xmaxtitle,step,stepname) {
    graphParameters.mtd = method;
    var subtitle = updateSubtitleForSigbuilderGraph(points, graphParameters.mtd, xmaxtitle,graphParameters.PeriodicOption);
    pointsHistory.push(graphParameters.graphPoints.slice());

    let sigbuilder_Graph = Highcharts.chart('drag_sig_chart', {
        chart: {
            type: chart_type,
            animation: false,
            events: {
                click: function (e) {
                    var x_value = e.xAxis[0].value;
                    var y_value = e.yAxis[0].value;
                    addPointsOnChart(sigbuilder_Graph, graphParameters, pointsHistory, x_value, y_value);
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
                            var graphObject = e;
                            editPointsValue(graphObject, graph_sigbuilder, sigbuilder_Graph, graphParameters, pointsHistory);
                        },
                        contextmenu: function (e) {
                            var graphObject = e;
                            removePointsFromChart(graphObject, sigbuilder_Graph, graphParameters, pointsHistory);
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
    return sigbuilder_Graph;
};

export function updateSubtitleForSigbuilderGraph(points, method, xmaxtitle, periodicFlag){

    var subTitle = "";
    if(periodicFlag == "y"){
        subTitle = "<b>"+points+" points, Method: "+getmethod(method)+", periodic, T = "+xmaxtitle+"</b>";
    }else{
        subTitle = "<b>"+points+" points, Method: "+getmethod(method)+", aperiodic</b>";
    }
    return subTitle;
}

function autoscaleFunctionalityForGraph(sigbuilder_Graph, graphParameters, pointsHistory){
    //Added for postive/maximum value autoscale functionality
        var max_x_value_new = sigbuilder_Graph.xAxis[0].getExtremes().dataMax; //get max x point's value
        var min_x_value_new = sigbuilder_Graph.xAxis[0].getExtremes().dataMin; //get min x point's value
        var max_y_value_new = sigbuilder_Graph.yAxis[0].getExtremes().dataMax; //get max y point's value
        var min_y_value_new = sigbuilder_Graph.yAxis[0].getExtremes().dataMin; //get min y point's value
        var diff_x = ((Math.abs(max_x_value_new - min_x_value_new))/100)*10;
        var diff_y = ((Math.abs(max_y_value_new - min_y_value_new))/100)*10;
        graphParameters.xmin = 0; //set min x axis value
        graphParameters.xmax = max_x_value_new + diff_x; //set max x axis value
        if(min_y_value_new > 0){
            min_y_value_new = 0;
        }
        graphParameters.ymin = min_y_value_new - diff_y; //set min y axis value
        graphParameters.ymax = max_y_value_new + diff_y; //set max y axis value
        graphParameters.points = graphParameters.graphPoints.length;
        sigbuilder_Graph = create_draggable_points_chart_sigbuilder(graphParameters, pointsHistory, graphParameters.xmin, graphParameters.xmax, graphParameters.ymin, graphParameters.ymax, graphParameters.chartType, graphParameters.points, graphParameters.mtd, graphParameters.xmaxTitle, graphParameters.step, graphParameters.stepname);
}

export function editPointsValue(graphObject,graph,sigbuilder_Graph,graphParameters, pointsHistory){

    document.getElementById("messageLabel").innerHTML = "";
    //Making graph window inaccessible
    var graph_wind = document.getElementById("graphcontentwind");
    graph_wind.style.pointerEvents = "none";
    // Create basic structure for the form
    var content = document.createElement('div');
    content.setAttribute("id", "editCoordinates");

    // Add Form
    var myform = document.createElement("form");
    myform.method = "post";
    myform.id = "formEditCoordinate";
    myform.style.padding = "10px";

    var titlelabel = document.createElement('span');
    titlelabel.innerHTML = "Enter new x and y";
    myform.appendChild(titlelabel);
    // Line break
    var linebreak = document.createElement('br');
    myform.appendChild(linebreak);
    // Line break
    var linebreak = document.createElement('br');
    myform.appendChild(linebreak);

    var keys = Object.keys(graphObject.point.options);
    var len = keys.length;
    for(var i = 0; i < len; i++){
        // Input Title
        var namelabel = document.createElement('label');
        namelabel.innerHTML = keys[i].toString();
        namelabel.style.marginLeft = "30px";
        myform.appendChild(namelabel);

        var value = 0;
        if(((graphObject.point.options[keys[i]]).toString()).includes(".")){
            value = (graphObject.point.options[keys[i]]).toFixed(6);
        }else{
            value = (graphObject.point.options[keys[i]]);
        }
        // Input
        var input = document.createElement("input");
        input.name = "edit_"+keys[i];
        input.value = value;
        input.setAttribute("id", "edit_"+keys[i]);
        input.setAttribute("class", "fieldInput");
        myform.appendChild(input);

        // Line break
        var linebreak = document.createElement('br');
        myform.appendChild(linebreak);

        // Line break
        var linebreak = document.createElement('br');
        myform.appendChild(linebreak);

    }
    // Line break
    var linebreak = document.createElement('br');
    myform.appendChild(linebreak);

    // Button - Cancel
    var cancel_btn = document.createElement("button");
    cancel_btn.style.cssFloat = "right";
    cancel_btn.innerHTML = 'Cancel';
    cancel_btn.type = "button";
    cancel_btn.name = "Cancel";
    myform.appendChild(cancel_btn);

    // Button - OK
    var ok_btn = document.createElement("button");
    ok_btn.style.cssFloat = "right";
    ok_btn.style.marginRight = "20px";
    ok_btn.innerHTML = 'OK';
    ok_btn.type = "button";
    ok_btn.name = "OK";

    myform.appendChild(ok_btn);
    content.appendChild(myform);
    var height = 150;
    wind = showModalWindow(graph, 'Scilab Multiple Values Request', content, 200, height);
    wind.addListener(mxEvent.DESTROY, function(evt) {
        graph_wind.style.pointerEvents = "auto";
    });
    // Executes when button 'cancel_btn' is clicked
    cancel_btn.onclick = function() {
        document.getElementById("messageLabel").innerHTML = "";
        graph_wind.style.pointerEvents = "auto";
        wind.destroy();
    };
    // Executes when button 'ok_btn' is clicked
    ok_btn.onclick = function() {
        var x_value = parseFloat(document.getElementById("edit_x").value);
        if(x_value < 0){
            x_value = 0;
        }
        var y_value = parseFloat(document.getElementById("edit_y").value);
        var points = graphParameters.graphPoints;
        var x_arry = [];
        for(var i = 0;i < points.length;i++){
            x_arry[i] = points[i][0];
        }
        x_arry[points.length] = x_value;
        var result = checkDuplicate_X_values(x_arry);
        var mtd_check = [0, 1, 2].includes(graphParameters.mtd);
        if(result){
            removePointsFromChart(graphObject,sigbuilder_Graph,graphParameters, pointsHistory);
            addPointsOnChart(sigbuilder_Graph,graphParameters, pointsHistory,x_value,y_value);
            autoscaleFunctionalityForGraph(sigbuilder_Graph, graphParameters, pointsHistory);
            document.getElementById("messageLabel").innerHTML = "";
            graph_wind.style.pointerEvents = "auto";
            wind.destroy();
        }else{
            if(mtd_check){
                removePointsFromChart(graphObject,sigbuilder_Graph,graphParameters, pointsHistory);
                addPointsOnChart(sigbuilder_Graph,graphParameters, pointsHistory,x_value,y_value);
                autoscaleFunctionalityForGraph(sigbuilder_Graph, graphParameters, pointsHistory);
                document.getElementById("messageLabel").innerHTML = "";
                graph_wind.style.pointerEvents = "auto";
                wind.destroy();
            }else{
                document.getElementById("messageLabel").innerHTML = "ERROR IN SPLINE : "+getmethod(graphParameters.mtd);
                wind.destroy();
                graph_wind.style.pointerEvents = "auto";
                throw "incorrect";
            }
        }
    };
}

export function removePointsFromChart(graphObject, sigbuilder_Graph, graphParameters, pointsHistory){
    var counter = graphObject.point.index;
    sigbuilder_Graph.series[0].data[counter].remove();
    pointsHistory.push(graphParameters.graphPoints.slice());
    graphParameters.points = sigbuilder_Graph.series[0].data.length;
    graphParameters.mtd = graphParameters.mtd;
    graphParameters.xmaxTitle = sigbuilder_Graph.xAxis[0].getExtremes().dataMax.toFixed(6);
    sigbuilder_Graph.setTitle(null, { text: updateSubtitleForSigbuilderGraph(graphParameters.points, graphParameters.mtd, graphParameters.xmaxTitle, graphParameters.PeriodicOption)});
}

export function addPointsOnChart(sigbuilder_Graph, graphParameters, pointsHistory, x_value, y_value){
    document.getElementById("messageLabel").innerHTML = "";
    if(x_value == 0 && y_value == 0){
        graphParameters.flag_for_zeros = true;
    }
    var points = graphParameters.graphPoints;
    var x_arry = [];
    for(var i = 0;i < points.length;i++){
        x_arry[i] = points[i][0];
    }
    x_arry[points.length] = x_value;
    var result = checkDuplicate_X_values(x_arry);
    var mtd_check = [0, 1, 2].includes(graphParameters.mtd);
    if(result){
        sigbuilder_Graph.series[0].addPoint([x_value, y_value]);
        pointsHistory.push(graphParameters.graphPoints.slice());
        graphParameters.points = sigbuilder_Graph.series[0].data.length;
        graphParameters.mtd = graphParameters.mtd;
        graphParameters.xmaxTitle = sigbuilder_Graph.xAxis[0].getExtremes().dataMax.toFixed(6);
        sigbuilder_Graph.setTitle(null, { text: updateSubtitleForSigbuilderGraph(graphParameters.points, graphParameters.mtd,   graphParameters.xmaxTitle, graphParameters.PeriodicOption)});
    }else{
        if(mtd_check){
            sigbuilder_Graph.series[0].addPoint([x_value, y_value]);
            pointsHistory.push(graphParameters.graphPoints.slice());
            graphParameters.points = sigbuilder_Graph.series[0].data.length;
            graphParameters.mtd = graphParameters.mtd;
            graphParameters.xmaxTitle = sigbuilder_Graph.xAxis[0].getExtremes().dataMax.toFixed(6);
            sigbuilder_Graph.setTitle(null, { text: updateSubtitleForSigbuilderGraph(graphParameters.points, graphParameters.mtd,   graphParameters.xmaxTitle, graphParameters.PeriodicOption)});
        }else{
            document.getElementById("messageLabel").innerHTML = "ERROR IN SPLINE : "+getmethod(graphParameters.mtd);
            throw "incorrect";
        }
    }
}

function checkDuplicate_X_values(xx_arry){
    var array_for_compare = [];
    var result = xx_arry.slice(0).every(function(item, index, array){
        if(array_for_compare.indexOf(item) > -1){
            array.length = 0;
            return false;
        }else{
            array_for_compare.push(item);
            return true;
        }
    });
    return result;
}
