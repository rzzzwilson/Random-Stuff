// Javascript code for the webELoss flood graph widget.

"use strict";

// configuration and default values for the widget object

// names of the dynamically created objects
var graphCanvasName = "graph";              // the graph <canvas> name
var graphAnnoName = "annotation";           // the graph annotation <canvas> name
var graphPopupMenuName = "menu";            // the normal popup menu <div> name
var graphPopupPointMenuName = "pointmenu";  // the point popup menu <div> name

// colours for various parts of the graph, etc
var graphCanvasColour = "white";    // background of graph proper
var graphBorderColour = "silver";   // border colour
var graphAxisColour = "black";      // axis lines and ticks
var graphGridColour = "Gainsboro";
var graphDMColour = "red";          // depth marker line and hotspot

var graphTitleColour = "black";
var graphTitle1Font = "28pt Arial";
var graphTitle1 = "Main title";
var graphTitle2Font = "18pt Arial";
var graphTitle2 = "Subtitle";

var graphGridWidth = 0.5;           // width of grid lines
var graphXAxisLabel = "Depth (m)";
var graphYAxisLabel = "Damage (%)";
var graphAxisLabelFont = "20pt Arial";
var graphAxisFont = "10pt Arial";

//FIXME  should be dynamic
var graphAnnotateWidth = 200;        // width of annotation box (pixels)

var graphDefaultDamage = 10.0;        // default percentage damage error

// turn graph grid on if true
var graphGrid = true;

// graph border margin widths
var leftMargin = 100;
var rightMargin = 25;
var topMargin = 100;
var bottomMargin = 80;

// width of axes and tick marks
var axisLineWidth = 3;              // width of axis lines (four sides)
var axisTickWidth = 1;              // tick width
var axisTickLength = 8;             // tick length

// X axis range and step
var minXAxis = -1;
var maxXAxis = 7;
var stepXAxis = 1;

// Y axis range and step
var minYAxis = 0;
var maxYAxis = 100;
var stepYAxis = 10;

// Damage Curve stuff
var graphDCWidth = 4;               // DC line width in pixels
var graphDCDepthGranule = 0.05;     // DC granularity (in metres)
var graphDCDamageGranule = 1.0;     // DC granularity (in percentage points)
var graphDCHSRadius = 8;            // radius in pixels of HS semicircle
var graphDCNewHSColour = "#808080"; // colour of DC "new" HS

// Reference Curve stuff
var graphRCWidth = 1;               // RC line width in pixels
var graphRCHSRadius = 8;            // radius in pixels of HS semicircle
var graphRCColour = "#000000";      // if defined, colour of HS
                                    // if not, use RC colour

// ErrorBar stuff for the Damage Curve
var graphEBLineWidth = 0.5;        // width of errorbar lines in pixels
var graphEBCapWidth = 3;           // halfwidth of capbar in pixels
var graphEBColour = "#000000";     // if defined, colour of errorbars
                                   // if not, use DC colour
// Depth Marker stuff
var graphDMWidth = 0.5;            // line width in pixels
var graphDMHSRadius = 8;           // radius in pixels of HS semicircle
var graphDMGranule = 0.05;         // DM granularity (in metres)

//*****************************************************************************
// Initial attempt at a 'graph' object usable by webELoss.
//*****************************************************************************

//////////////////////////////
// Setup the graph in a canvas
//     canvas_div_name  name of the user <div> to work within
//     canvas_obj_name  name of the <canvas> object in the <div>

function Graph(widget_div_name)
{
    // set some internal state from the defaults
    this.graphTitle1 = graphTitle1;
    this.graphTitle2 = graphTitle2;

    // save the container <div> name and <div> object reference
    this.graphDivName = widget_div_name;
    this.graphDiv = document.getElementById(widget_div_name);

    // check the given <div> doesn't 
    
    // create graph widget object in the given container <div>
    var graph_canvas = document.createElement('canvas');
    this.graphCanvas = graph_canvas;
    this.graphCanvasName = graphCanvasName;
    graph_canvas.id = this.graphCanvasName;
    graph_canvas.style.position = "absolute";
    this.graphDiv.appendChild(graph_canvas);
    console.log('Created graph canvas: ' + this.graphCanvas);
    
    // create annotation <div> in the given container <div>
    var anno_div = document.createElement('div');
    this.graphAnnoDiv = anno_div;
    this.graphAnnoName = graphAnnoName;
    anno_div.id = this.graphAnnoName;
    anno_div.className = this.graphAnnoName;
    anno_div.style.position = "absolute";
    anno_div.style.visibility="hidden";
    this.graphDiv.appendChild(anno_div);
    console.log('Created annotation <div>: ' + this.graphAnnoDiv);
    
    // create the popup menu <div>s

    // mouse screen coordinates
    this.xScreenCoord = null;
    this.yScreenCoord = null;

    // mouse graph coordinates (in graph units)
    this.xGraphCoord = null;
    this.yGraphCoord = null;

    // flag to tell us if dragging with left button down
    this.leftButtonDown = false;

    // the list holding Depth Marker data
     this.DepthMarkerArray = [];
    // could combine these two
    this.DMHSIndex = null;          // index into DepthMarkerArray of HS DM
    this.DMHotspotShowing = false;  // true if DM hotspot is showing
    this.DMHSx = null;        // if showing, X canvas coord
    this.DMHSy = null;        // if showing, Y canvas coord
    this.draggingDM = false;    // true if dragging DM HS

    // object holding the Damage Curve data
    // object is: {colour: "#ff0000", points:[{depth:x, damage:y, error: 10}, ...]}
    this.DamageCurve = null;

    // hotspot (HS) stuff for DC
    this.DCHSIndex = null;          // index into DamageCurve.points of HS DC
    this.DCHotspotShowing = false;  // true if DC hotspot is showing
    this.DCHSx = null;        // if showing, X canvas coord
    this.DCHSy = null;        // if showing, Y canvas coord
    this.draggingDC = false;    // true if dragging DC HS

    // array holding the Damage Curve "new points" data
    // array object is: {depth:x, damage:y}
    this.DCNewPoints = [{depth:(minXAxis+maxXAxis)/2.0, damage:minYAxis}];
    this.DCNewHSIndex = null;        // index into this.DCNewPoints of HS
    this.DCNewHotspotShowing = false;    // true if new DC hotspot is showing
    this.DCNewHSx = null;            // if showing, X canvas coord
    this.DCNewHSy = null;            // if showing, Y canvas coord

    // array holding the Reference Curve data
    // object is: {colour: "#ff0000", points:[{depth:x, damage:y}, ...]}
    this.ReferenceCurves = [];
    this.RCHS = [];                 // hotspot positions for RC

    // hotspot (HS) stuff for RC
    this.RCHSIndex = null;          // index into this.RCHS of RC HS
    this.RCHotspotShowing = false;  // true if RC hotspot is showing
    this.RCHSx = null;        // if showing, X canvas coord
    this.RCHSy = null;        // if showing, Y canvas coord

    // lengths of (dynamic) graph axes
    this.graphXLength = null;       // X pixel length of graph data view
    this.graphYLength = null;       // Y pixel length of graph data view

    this.annotateShowing = false;   // true if annotation is showing

    this.bindThis();
    this.refresh();
}

//////////////////////////////
// Set the Depth Markers
//     dms  the new depth marker data
Graph.prototype.setDepthMarkers = function(dms)
{
    this.DepthMarkerArray = dms;
}

//////////////////////////////
// Set the Damage Curve
//     dc  the new damage curve data
Graph.prototype.setDamageCurve = function(dc)
{
    this.DamageCurve = dc;
    this.makeDCNewPoints();
}

//////////////////////////////
// create a set of "DC new points" from the current DC points
Graph.prototype.makeDCNewPoints = function()
{
    var last_depth = minXAxis;
    var last_damage = minYAxis;

    this.DCNewPoints = [];

    for (var i in this.DamageCurve.points)
    {
        var point = this.DamageCurve.points[i];
        var next_depth = point.depth;
        var next_damage = point.damage;

        var new_depth = (last_depth + next_depth) / 2.0;
        var new_damage = (last_damage + next_damage) / 2.0;
        this.DCNewPoints.push({depth:new_depth, damage:new_damage});

        last_depth = next_depth;
        last_damage = next_damage;
    }

    // add last point
    new_depth = (last_depth + maxXAxis) / 2.0;
    new_damage = last_damage;
    this.DCNewPoints.push({depth:new_depth, damage:new_damage});
}

//////////////////////////////
// Set the Reference Curves data
//      rc  the new reference curve data
Graph.prototype.setReferenceCurves = function(rc)
{
    this.ReferenceCurves = rc;
    this.makeRCHotspots();
}

//////////////////////////////
// Create the RC hotspot data, just array of last damage values for each RC curve
Graph.prototype.makeRCHotspots = function()
{
    this.RCHS = []
    for (var i in this.ReferenceCurves)
    {
        var curve = this.ReferenceCurves[i];
        var last = curve.points[curve.points.length - 1];

        this.RCHS.push(last.damage);
    }
}

//////////////////////////////
// Called on display refresh - draw the graph
Graph.prototype.refresh = function(event)
{
    var canvas_ctx = this.graphCanvas.getContext("2d");

    // get viewport width+height and then calculate X and Y axis length in pixels
    var canvasWidth = window.innerWidth;
    var canvasHeight = window.innerHeight;
    this.graphXLength = canvasWidth - leftMargin - rightMargin;
    this.graphYLength = canvasHeight - topMargin - bottomMargin;
    this.maxGraphHeight = topMargin;

    // fix the canvas in the viewport, full size
    this.graphCanvas.style.position = "fixed";
    this.graphCanvas.setAttribute("width", canvasWidth);
    this.graphCanvas.setAttribute("height", canvasHeight);
    this.graphCanvas.style.top = 0;
    this.graphCanvas.style.left = 0;
    canvas_ctx.lineJoin = "round";

    // draw the graph
    // clear canvas to the border colour
    canvas_ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    canvas_ctx.fillStyle = graphBorderColour;
    canvas_ctx.beginPath();
    canvas_ctx.moveTo(0, 0);
    canvas_ctx.lineTo(0, canvasHeight);
    canvas_ctx.lineTo(canvasWidth, canvasHeight);
    canvas_ctx.lineTo(canvasWidth, 0);
    canvas_ctx.closePath();
    canvas_ctx.fill();

    // then draw the graph area in the middle
    canvas_ctx.fillStyle = graphCanvasColour;
    canvas_ctx.beginPath();
    canvas_ctx.moveTo(leftMargin, topMargin);
    canvas_ctx.lineTo(leftMargin, canvasHeight-bottomMargin);
    canvas_ctx.lineTo(canvasWidth-rightMargin, canvasHeight-bottomMargin);
    canvas_ctx.lineTo(canvasWidth-rightMargin, topMargin);
    canvas_ctx.closePath();
    canvas_ctx.fill();

    // outline the graph with the axes
    canvas_ctx.strokeStyle = graphAxisColour;
    canvas_ctx.lineWidth = axisLineWidth;
    canvas_ctx.beginPath();
    canvas_ctx.moveTo(leftMargin, topMargin);
    canvas_ctx.lineTo(leftMargin, canvasHeight-bottomMargin);
    canvas_ctx.lineTo(canvasWidth-rightMargin, canvasHeight-bottomMargin);
    canvas_ctx.lineTo(canvasWidth-rightMargin, topMargin);
    canvas_ctx.closePath();
    canvas_ctx.stroke();

    // if required, draw a subtle grid
    if (graphGrid)
    {
        canvas_ctx.strokeStyle = graphGridColour;
        canvas_ctx.lineWidth = graphGridWidth;

        // vertical grid lines
        var step = (maxXAxis - minXAxis) / stepXAxis;
        var stepLength = this.graphXLength / step;

        for (step = 0; step <= this.graphXLength; step += stepLength)
        {
            canvas_ctx.beginPath();
            canvas_ctx.moveTo(leftMargin+step, topMargin);
            canvas_ctx.lineTo(leftMargin+step, canvasHeight-bottomMargin);
            canvas_ctx.stroke();
        }

        // horizontal grid lines
        var step = (maxYAxis - minYAxis) / stepYAxis;
        var stepLength = this.graphYLength / step;

        for (step = 0; step <= this.graphYLength; step += stepLength)
        {
            canvas_ctx.beginPath();
            canvas_ctx.moveTo(leftMargin, topMargin+step);
            canvas_ctx.lineTo(canvasWidth-rightMargin, topMargin+step);
            canvas_ctx.stroke();
        }
    }

    // draw X axis ticks and labels
    canvas_ctx.strokeStyle = graphAxisColour;
    canvas_ctx.font = graphAxisFont;
    canvas_ctx.fillStyle = graphAxisColour;
    canvas_ctx.textBaseline = "top";
    canvas_ctx.lineWidth = axisTickWidth;
    var step = (maxXAxis - minXAxis) / stepXAxis;
    var stepLength = this.graphXLength / step;
    var yPosn = topMargin+this.graphYLength;
    var depth = minXAxis;
    for (step = 0; step <= this.graphXLength+stepXAxis-1; step += stepLength)
    {
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(leftMargin+step, yPosn);
        canvas_ctx.lineTo(leftMargin+step, yPosn+axisTickLength);
        canvas_ctx.stroke();

        var width = canvas_ctx.measureText(depth).width;
        canvas_ctx.fillText(depth, leftMargin+step-width/2, yPosn+axisTickLength+2);

        depth += stepXAxis;
    }
    canvas_ctx.font = graphAxisLabelFont;
    canvas_ctx.save();
    canvas_ctx.translate(leftMargin+this.graphXLength/2, yPosn+axisTickLength+25);
    canvas_ctx.textAlign = "center";
    canvas_ctx.fillText(graphXAxisLabel, 0, 0);
    canvas_ctx.restore();

    // draw Y axis ticks and labels
    canvas_ctx.strokeStyle = graphAxisColour;
    canvas_ctx.font = graphAxisFont;
    canvas_ctx.fillStyle = graphAxisColour;
    canvas_ctx.textBaseline = "middle";
    canvas_ctx.lineWidth = axisTickWidth;
    step = (maxYAxis - minYAxis) / stepYAxis;
    stepLength = this.graphYLength / step;
    var damage = maxYAxis;
    for (step = 0; step <= this.graphYLength+stepYAxis-1; step += stepLength)
    {
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(leftMargin, topMargin+step);
        canvas_ctx.lineTo(leftMargin-axisTickLength, topMargin+step);
        canvas_ctx.stroke();

        var width = canvas_ctx.measureText(damage).width;
        canvas_ctx.fillText(damage, leftMargin-axisTickLength-width-3, topMargin+step);

        damage -= stepYAxis;
    }
    canvas_ctx.font = graphAxisLabelFont;
    canvas_ctx.save();
    canvas_ctx.translate(40, topMargin+this.graphYLength/2);
    canvas_ctx.rotate(-Math.PI/2);
    canvas_ctx.textAlign = "center";
    canvas_ctx.fillText(graphYAxisLabel, 0, 0);
    canvas_ctx.restore();

    // now draw the actual graph itself from the data
    // draw depth markers
    canvas_ctx.strokeStyle = graphDMColour;
    canvas_ctx.lineWidth = graphDMWidth;
    canvas_ctx.fillStyle = graphDMColour;
    for (var i in this.DepthMarkerArray)
    {
        var dm_depth = this.DepthMarkerArray[i].depth;
        var xoffset = leftMargin + this.graphXLength*(dm_depth-minXAxis)/(maxXAxis - minXAxis);

        canvas_ctx.beginPath();
        canvas_ctx.moveTo(xoffset, topMargin);
        canvas_ctx.lineTo(xoffset, canvasHeight-bottomMargin);
        canvas_ctx.stroke();
    }

    // draw DM HS half-circle if we are showing it
    if (this.DMHotspotShowing)
    {
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(this.DMHSx, topMargin);
        canvas_ctx.arc(this.DMHSx, this.DMHSy, graphDMHSRadius, 0, Math.PI, false);
        canvas_ctx.fill();
    }
    // draw reference curves
    for (var i in this.ReferenceCurves)
    {
            var curve = this.ReferenceCurves[i];
        var currentY = 0.0;    // Y coord of last point drawn

        canvas_ctx.strokeStyle = curve.colour;
        canvas_ctx.fillStyle = curve.colour;
            canvas_ctx.lineWidth = graphRCWidth;
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(leftMargin, topMargin+this.graphYLength);

        // lineTo() each point
        for (var j in curve.points)
        {
            var point = curve.points[j];
            var x = this.convertXGraph2Screen(point.depth);
            var y = this.convertYGraph2Screen(point.damage);
    
            canvas_ctx.lineTo(x, y);
            currentY = y
        }

       canvas_ctx.lineTo(leftMargin+this.graphXLength, currentY);
       canvas_ctx.stroke();
    }

    // draw the RC hotspot, if showing
    if (this.RCHotspotShowing)
    {
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(this.RCHSx, this.RCHSy);
        canvas_ctx.arc(this.DMHSx, this.DMHSy, graphRCHSRadius, Math.PI/2, Math.PI/2+Math.PI, false);
        canvas_ctx.fill();
    }

    // draw the error bars at each point on the damage curve
    if (this.DamageCurve != null)
    {
        for (var i in this.DamageCurve.points)
        {
            var point = this.DamageCurve.points[i];
            var screen_x = this.convertXGraph2Screen(point.depth);
            var screen_y = this.convertYGraph2Screen(point.damage);
            var graph_delta = point.damage*point.error/100;
            var screen_delta = this.convertYGraph2Screen(graph_delta)-this.graphYLength-topMargin;

            //graph.drawErrorbars(x, y, error, colour);
            if (typeof graphEBColour=="undefined")
                canvas_ctx.strokeStyle = this.DamageCurve.colour;
            else
                canvas_ctx.strokeStyle = graphEBColour;

            // limit top of error bar to top of graph proper
            var y_plus_delta = screen_y+screen_delta;
            if (y_plus_delta < topMargin)
                y_plus_delta = topMargin;

            canvas_ctx.lineWidth = graphEBLineWidth;
            canvas_ctx.beginPath();
            canvas_ctx.moveTo(screen_x, y_plus_delta);
            canvas_ctx.lineTo(screen_x, screen_y-screen_delta);
            canvas_ctx.moveTo(screen_x-graphEBCapWidth, y_plus_delta);
            canvas_ctx.lineTo(screen_x+graphEBCapWidth, y_plus_delta);
            canvas_ctx.moveTo(screen_x-graphEBCapWidth, screen_y-screen_delta);
            canvas_ctx.lineTo(screen_x+graphEBCapWidth, screen_y-screen_delta);
            canvas_ctx.stroke();
        }
    }

    // draw new DC HS circle if we are showing it
    if (this.DCNewHotspotShowing)
    {
        canvas_ctx.strokeStyle = graphDCNewHSColour;
        canvas_ctx.fillStyle = graphDCNewHSColour;
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(this.DCNewHSx, this.DCNewHSy);
        canvas_ctx.arc(this.DCNewHSx, this.DCNewHSy, graphDCHSRadius, 0, 2*Math.PI, false);
        canvas_ctx.fill();
    }

    // draw DC HS circle if we are showing it
    if (this.DCHotspotShowing)
    {
        canvas_ctx.strokeStyle = this.DamageCurve.colour;
        canvas_ctx.fillStyle = this.DamageCurve.colour;
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(this.DCHSx, this.DCHSy);
        canvas_ctx.arc(this.DCHSx, this.DCHSy, graphDCHSRadius, 0, 2*Math.PI, false);
        canvas_ctx.fill();
    }

    // draw the damage curve itself
    if (this.DamageCurve != null)
    {
        var currentY = 0.0;    // Y coord of last point drawn

        canvas_ctx.strokeStyle = this.DamageCurve.colour;
        canvas_ctx.lineWidth = graphDCWidth;
        canvas_ctx.beginPath();
        canvas_ctx.moveTo(leftMargin, topMargin+this.graphYLength);

        // lineTo() each point
        for (var i in this.DamageCurve.points)
        {
            var point = this.DamageCurve.points[i];
            var x = this.convertXGraph2Screen(point.depth);
            var y = this.convertYGraph2Screen(point.damage);

            canvas_ctx.lineTo(x, y);
            currentY = y
        }

        canvas_ctx.lineTo(leftMargin+this.graphXLength, currentY);
        canvas_ctx.stroke();
    }

    // now display the graph main title
    canvas_ctx.strokeStyle = graphTitleColour;
    canvas_ctx.font = graphTitle1Font;
    canvas_ctx.fillStyle = graphTitleColour;
    canvas_ctx.textAlign = "center";
    canvas_ctx.textBaseline = "top";
    var title = this.graphTitle1;
    var xoffset = leftMargin+this.graphXLength/2;
    var yoffset = 15;
    canvas_ctx.fillText(title, xoffset, yoffset);
    // sub title
    canvas_ctx.font = graphTitle2Font;
    title = this.graphTitle2;
    var xoffset = leftMargin+this.graphXLength/2;
    var yoffset = 60;
    canvas_ctx.fillText(title, xoffset, yoffset);

    // recalculate the RC hotspots
    this.makeRCHotspots();
};

//////////////////////////////
// returns object with attributes for closest DM hotspot
// to mouse or null if none close enough.
//     result = {index: i, x: xoffset, y: yoffset}
// where i is index of closest DM in this.DepthMarkerArray
Graph.prototype.closestDMPoint = function(x, y, radius)
{
    var result = null;
    var close = 9999999999;

    if (this.yScreenCoord < topMargin)
        return null;

    for (var i in this.DepthMarkerArray)
    {
        var dm = this.DepthMarkerArray[i];
        var xoffset = leftMargin + this.graphXLength*(dm.depth-minXAxis)/(maxXAxis - minXAxis);
        var yoffset = topMargin;

        if (this.pointClose(xoffset, yoffset, this.xScreenCoord, this.yScreenCoord, radius))
        {
            var new_close = Math.abs(this.xScreenCoord-xoffset) + Math.abs(this.yScreenCoord-yoffset);
            if (new_close < close)
            {
                result = {index: i, x: xoffset, y: yoffset};
                close = new_close;
            }
        }
    }

    if (radius*radius < close*close)
        return null;

    return result;
};

//////////////////////////////
// Returns object with .x and .y coords of closest DC hotspot
// to mouse or null if none close enough.
//     x, y  mouse coordinates
//     radius  radius of circle around mouse position
// Returns:
//     result = {index: i, x: xoffset, y: yoffset};
// where i is index of closest DM in this.DamageCurve.points
Graph.prototype.closestDCPoint = function(x, y, radius)
{
    var result = null;
    var close = 9999999999;

    if (this.DamageCurve == null)
        return null;

    for (var i in this.DamageCurve.points)
    {
        var point = this.DamageCurve.points[i];
        var xoffset = leftMargin + this.graphXLength*(point.depth-minXAxis)/(maxXAxis - minXAxis);
        var yoffset = topMargin + this.graphYLength - this.graphYLength*(point.damage-minYAxis)/(maxYAxis - minYAxis);

        if (this.pointClose(xoffset, yoffset, this.xScreenCoord, this.yScreenCoord, radius))
        {
            var new_close = Math.abs(this.xScreenCoord-xoffset) + Math.abs(this.yScreenCoord-yoffset);
            if (new_close < close)
            {
                result = {index: i, x: xoffset, y: yoffset};
                close = new_close;
            }
        }
    }

    if (radius*radius < close*close)
        return null;

    return result;
};

//////////////////////////////
// Returns object with attributes for closest RC hotspot
// to mouse or null if none close enough.
//     result = {index: i, x: xoffset, y: yoffset}
// where i is index of closest DM in this.RCHS
Graph.prototype.closestRCPoint = function(points, x, y, radius)
{
    var result = null;
    var close = 9999999999;

    if (this.yScreenCoord > leftMargin+this.graphYLength+rightMargin)
        return null;

    for (var i in points)
    {
        var xoffset = leftMargin+this.graphXLength;
        var yoffset = points[i];

        if (this.pointClose(xoffset, yoffset, this.xScreenCoord, this.yScreenCoord, radius))
        {
            var new_close = Math.abs(this.xScreenCoord-xoffset) + Math.abs(this.yScreenCoord-yoffset);
            if (new_close < close)
            {
                result = {index: i, x: xoffset, y: yoffset};
                close = new_close;
            }
        }
    }

    if (radius*radius < close*close)
        return null;

    return result;
};

//////////////////////////////
// returns object with .x and .y coords of closest point in given list
// to mouse or null if none close enough.  list is in graph coords.
Graph.prototype.closestPoint = function(points, x, y, radius)
{
    var result = null;
    var close = 9999999999;

    for (var i in points)
    {
        var point = points[i];
        var xoffset = leftMargin + this.graphXLength*(point.depth-minXAxis)/(maxXAxis - minXAxis);
        var yoffset = topMargin + this.graphYLength - this.graphYLength*(point.damage-minYAxis)/(maxYAxis - minYAxis);

        if (this.pointClose(xoffset, yoffset, this.xScreenCoord, this.yScreenCoord, radius))
        {
            var new_close = Math.abs(this.xScreenCoord-xoffset) + Math.abs(this.yScreenCoord-yoffset);
            if (new_close < close)
            {
                result = {index: i, x: xoffset, y: yoffset};
                close = new_close;
            }
        }
    }

    if (radius*radius < close*close)
        return null;

    return result;
};

//////////////////////////////
// Returns true if p1 is no more than distance pixels away from p2
// in both X and Y directions.
Graph.prototype.pointClose = function(p1x, p1y, p2x, p2y, distance)
{
    return (Math.abs(p2x-p1x) <= distance) && (Math.abs(p2y-p1y) <= distance);
};

//////////////////////////////
// functions to convert screen coordinates to graph coordinates.
// return 'null' if not on graph proper.
Graph.prototype.convertXScreen2Graph = function(x)
{
    if ((x >= leftMargin) && (x <= (leftMargin+this.graphXLength)))
    {
        return (x-leftMargin)*(maxXAxis-minXAxis)/this.graphXLength + minXAxis;
    }

    return null;
};

Graph.prototype.convertYScreen2Graph = function(y)
{
    if ((y >= topMargin) && (y <= (topMargin+this.graphYLength)))
    {
        // must invert result as graph coords opposite to screen coords
        return maxYAxis - (y-topMargin)*(maxYAxis-minYAxis)/this.graphYLength + minYAxis;
    }

    return null;
};

//////////////////////////////
// functions to convert graph coordinates to screen coordinates.
Graph.prototype.convertXGraph2Screen = function(x)
{
    return leftMargin + ((x-minXAxis)*this.graphXLength)/(maxXAxis-minXAxis);
};

Graph.prototype.convertYGraph2Screen = function(y)
{
    return topMargin + this.graphYLength - ((y-minYAxis)*this.graphYLength)/(maxYAxis-minYAxis);
};

//////////////////////////////
// convert screen coords to graph coords (if on graph).
// if not on graph, return last X and Y 'on graph' values.
Graph.prototype.getGraphCoordString = function()
{
    // fill '*_coord_str' with previous values
    var x_coord_str = 'X='+this.xGraphCoord;
    var y_coord_str = 'Y='+this.yGraphCoord;
    var result = null;

    // get graph X coord, null if off graph
    result = this.convertXScreen2Graph(this.xScreenCoord);
    if (result != null)
    {
        this.xGraphCoord = result;
        x_coord_str = 'X='+result;
    }

    // get graph Y coord, null if off graph
    result = this.convertYScreen2Graph(this.yScreenCoord);
    if (result != null)
    {
        this.yGraphCoord = result;
        y_coord_str = 'Y='+result;
    }

    return x_coord_str+'\n'+y_coord_str;
};

//////////////////////////////
// Handle the "mouse move" event.
Graph.prototype.onMouseMove = function(e)
{
    var force_refresh = false;    // we may need to refresh the display

    // get mouse position on canvas
    if (e.pageX || e.pageY)
    {
        this.xScreenCoord = e.pageX;
        this.yScreenCoord = e.pageY;
    }
    else if (e.clientX || e.clientY)
    {
        this.xScreenCoord = e.clientX;
        this.yScreenCoord = e.clientY;
    }

    // update graph coords
    var result = this.convertXScreen2Graph(this.xScreenCoord);
    if (result != null)
            this.xGraphCoord = result;
    result = this.convertYScreen2Graph(this.yScreenCoord);
    if (result != null)
        this.yGraphCoord = result;

    if (this.draggingDM)
    {
        // quantize DM X coord to nearest allowed position
        var dm_x = Math.round(this.xGraphCoord/graphDMGranule) * graphDMGranule;

        // move indexed DM to new position
        var dm = this.DepthMarkerArray[this.DMHSIndex];
        var old_label = dm.label;
        this.DepthMarkerArray[this.DMHSIndex] = {label: old_label, depth: dm_x};
        // constrain HS to be on graph view
        this.DMHSx = Math.max(this.xScreenCoord, leftMargin);
        this.DMHSx = Math.min(this.DMHSx, (leftMargin+this.graphXLength));

        // update annotation text
        this.annotateReplace(this.nameOfTipsDIV, old_label + ": depth " + dm_x.toFixed(2) + "m");

        // move annotation if cursor close
        var graphPixCoord = this.xScreenCoord - leftMargin;

        if (graphPixCoord < this.graphXLength/4)
            this.annotateMove(this.nameOfTipsDIV, leftMargin+this.graphXLength-graphAnnotateWidth-20);
        else if (graphPixCoord > 3*this.graphXLength/4)
            this.annotateMove(this.nameOfTipsDIV, leftMargin+20);

        // force a redraw to show changed DM
        force_refresh = true;
    }
    else if (this.DepthMarkerArray.length > 0) // else check if close to a DM hotspot
    {
        var oldDMHotspotShowing = this.DMHotspotShowing;
        var closest = this.closestDMPoint(this.xScreenCoord, this.yScreenCoord, graphDMHSRadius);
        this.DMHotspotShowing = false;
        this.DMHSIndex = null;
        if (closest)
        {
            // there is a closest, take note
            this.DMHotspotShowing = true;
            this.DMHSIndex = closest.index;
            this.DMHSx = closest.x;
            this.DMHSy = closest.y;
        }

        // force a redraw if any HS status change
        if (oldDMHotspotShowing != this.DMHotspotShowing)
            force_refresh = true;
    }

    if (this.draggingDC)
    {
        // quantize DC X depth and damagecoord to nearest allowed position
        var dc_x = Math.round(this.xGraphCoord/graphDCDepthGranule) * graphDCDepthGranule;
        var dc_y = Math.round(this.yGraphCoord/graphDCDamageGranule) * graphDCDamageGranule;

        // move indexed DC point to new position
        var dc_point = this.DamageCurve.points[this.DCHSIndex];
        var old_error = dc_point.error;
        this.DamageCurve.points[this.DCHSIndex] = {depth: dc_x, damage: dc_y, error: old_error};

        // constrain HS to be on graph view
        this.DCHSx = Math.max(this.xScreenCoord, leftMargin);
        this.DCHSx = Math.min(this.DCHSx, (leftMargin+this.graphXLength));
        this.DCHSy = Math.max(this.yScreenCoord, topMargin);
        this.DCHSy = Math.min(this.DCHSy, (topMargin+this.graphYLength));

        // update annotation text
        this.annotateReplace(this.nameOfTipsDIV, "point: depth " + dc_x.toFixed(2) + "m");

        // move annotation if cursor close
        var graphPixCoord = this.xScreenCoord - leftMargin;

        if (graphPixCoord < this.graphXLength/4)
            this.annotateMove(this.nameOfTipsDIV, leftMargin+this.graphXLength-graphAnnotateWidth-20);
        else if (graphPixCoord > 3*this.graphXLength/4)
            this.annotateMove(this.nameOfTipsDIV, leftMargin+20);

        // force a redraw to show changed DC
        force_refresh = true;
    }
    else if (this.DepthMarkerArray.length > 0) // else check if close to a DC hotspot
    {
        var oldDCHotspotShowing = this.DCHotspotShowing;
        var closest = this.closestDCPoint(this.xScreenCoord, this.yScreenCoord, graphDCHSRadius);
        this.DCHotspotShowing = false;
        this.DCHSIndex = null;
        if (closest)
        {
            // there is a closest, take note
            this.DCHotspotShowing = true;
            this.DCHSIndex = closest.index;
            this.DCHSx = closest.x;
            this.DCHSy = closest.y;
        }

        // force a redraw if any HS status change
        if (oldDCHotspotShowing != this.DCHotspotShowing)
            force_refresh = true;
    }

    // check if close to a "new DC" hotspot
    // there is always a this.DCNewPoints list of at least one point
    {
        var oldDCNewHotspotShowing = this.DCNewHotspotShowing;
        var closest = this.closestPoint(this.DCNewPoints, this.xScreenCoord, this.yScreenCoord, graphDCHSRadius);
        this.DCNewHotspotShowing = false;
        this.DCNewHSIndex = null;
        if (closest)
        {
            // there is a closest, take note
            this.DCNewHotspotShowing = true;
            this.DCNewHSIndex = closest.index;
            this.DCNewHSx = closest.x;
            this.DCNewHSy = closest.y;
        }

        // force a redraw if any new DC HS status change
        if (oldDCNewHotspotShowing != this.DCNewHotspotShowing)
            force_refresh = true;
    }

    // check if close to an RC hotspot
    {
        var oldRCHotspotShowing = this.RCHotspotShowing;
        var closest = this.closestRCPoint(this.RCHS, this.xScreenCoord, this.yScreenCoord, graphRCHSRadius);
        this.RCHotspotShowing = false;
        this.RCHSIndex = null;
        if (closest)
        {
            // there is a closest, take note
            this.RCHotspotShowing = true;
            this.RCHSIndex = closest.index;
            this.RCHSx = closest.x;
            this.RCHSy = closest.y;
        }

        // force a redraw if any new RC HS status change
        if (oldRCHotspotShowing != this.RCHotspotShowing)
            force_refresh = true;
    }

    // if we did something above that requires a refresh, do it now
    if (force_refresh)
        this.refresh();
};

//////////////////////////////
// Handle the "mouse down" event.
Graph.prototype.onMouseDown = function(e)
{
    // hide any previous menu
    this.hideNormalMenu(e);
    this.hideAugmentedMenu(e);

    // remember which button was pressed (TODO: MAKE PORTABLE)
    this.leftButtonDown = (e.button == 0);
    this.rightButtonDown = (e.button == 2);

    // if left button and hotspot showing start dragging it
    this.draggingDM = (this.DMHotspotShowing && this.leftButtonDown);
    this.draggingDC = (this.DCHotspotShowing && this.leftButtonDown);

    // if on a 'new' DC hotspot, create new graph point, allow drag
    if (this.DCNewHotspotShowing && this.leftButtonDown)
    {
        // create new DC point
        var new_point = this.DCNewPoints[this.DCNewHSIndex];
        var new_depth = new_point.depth;
        var new_damage = new_point.damage;
        this.DamageCurve.points.splice(this.DCNewHSIndex, 0,
                           {depth:new_depth, damage:new_damage, error:graphDefaultDamage});
        this.DCHSIndex = this.DCNewHSIndex;
        this.DCNewHSIndex = null;
        this.DCNewHotspotShowing = false;
        this.makeDCNewPoints();

        // then allow drag of new point
        this.draggingDC = true;
    }

    // if we are dragging a DM
    if (this.draggingDM)
    {
        var dm = this.DepthMarkerArray[this.DMHSIndex];
        var x_posn = leftMargin + 20;

        this.annotateReplace(this.nameOfTipsDIV, dm.label + ": depth " + dm.depth.toFixed(2) + "m");
        if ((this.xScreenCoord - leftMargin) < this.graphXLength/2)
            x_posn = leftMargin+this.graphXLength-graphAnnotateWidth-20;
        this.annotate_show(x_posn, topMargin+20);
    }
    else if (this.draggingDC)        // if we are dragging a DC point
    {
        var point = this.DamageCurve.points[this.DCHSIndex];
        var x_posn = leftMargin + 20;

        this.annotateReplace(this.nameOfTipsDIV, "point: depth " + point.depth.toFixed(2) + "m");
        if ((this.xScreenCoord - leftMargin) < this.graphXLength/2)
            x_posn = leftMargin+this.graphXLength-graphAnnotateWidth-20;
        this.annotate_show(x_posn, topMargin+20);
    }
    else if (this.rightButtonDown)
    {
        // show required menu
        if (this.DCHotspotShowing)
        {
            this.showAugmentedMenu(e);
        }
        else
        {
            this.showNormalMenu(e);
        }
    }
};

//////////////////////////////
// Show a normal menu on right-button down.
//     e  the event object for right-button down
Graph.prototype.showNormalMenu = function(e)
{
    var menu = document.getElementById(graphPopupMenuName);

    //menu.style.left = e.layerX+'px';
    //menu.style.top = e.layerY+'px';

    menu.style.left = e.pageX+'px';
    menu.style.top = e.pageY+'px';
    menu.style.visibility="visible";
    menu.style.display = "";

    document.getElementById('menuDM').style.backgroundColor='#FFFFFF';
    document.getElementById('menuRC').style.backgroundColor='#FFFFFF';
    document.getElementById("menuDM").onclick = this.manageDM;

    return false;
};

//////////////////////////////
// Show an augmented menu on right-button down.
//     e  the event object for right-button down
Graph.prototype.showAugmentedMenu = function(e)
{
    var menu = document.getElementById(graphPopupPointMenuName);

    //menu.style.left = e.layerX+'px';
    //menu.style.top = e.layerY+'px';

    menu.style.left = e.pageX+'px';
    menu.style.top = e.pageY+'px';
    menu.style.visibility="visible";
    menu.style.display = "";

    document.getElementById('menuEdit').style.backgroundColor='#FFFFFF';
    document.getElementById('menuDelete').style.backgroundColor='#FFFFFF';
    document.getElementById('menuDM').style.backgroundColor='#FFFFFF';
    document.getElementById('menuRC').style.backgroundColor='#FFFFFF';

    return false;
};

//////////////////////////////
// Hide the menus.
Graph.prototype.hideNormalMenu = function(e)
{
    var menu = document.getElementById(graphPopupMenuName);

    menu.style.visibility="hidden";
}

Graph.prototype.hideAugmentedMenu = function(e)
{
    var menu = document.getElementById(graphPopupPointMenuName);

    menu.style.visibility="hidden";
}

//////////////////////////////
// Handle the "mouse up" event.
Graph.prototype.onMouseUp = function(e)
{
    // remove any annotation
    if (this.draggingDM || this.draggingDC)
    {
        this.annotate_hide(this.nameOfTipsDIV);
        // if we were dragging a DC point, create new list of "new points"
        if (this.draggingDC)
            this.makeDCNewPoints();
    }

    this.leftButtonDown = false;
    this.draggingDM = false;
    this.draggingDC = false;
};

//////////////////////////////
// Manage a DM.
Graph.prototype.manageDM = function()
{
    console.debug('manageDM');
};

////////////////////////////////////////////////////////////////

//
// Simple dynamic annotation
//

Graph.prototype.annotate_show = function(x, y)
{
    var style = this.graphAnnoDiv.style;
    var viz = style.visibility;

    style.left = x + "px";
    style.top = y + "px";
    style.width = graphAnnotateWidth + "px";
    style.visibility = "visible";
};

Graph.prototype.annotate_hide = function()
{
    var style = this.graphAnnoDiv.style;
    var viz = style.visibility;

    style.visibility = "hidden";
};

Graph.prototype.annotateReplace = function(new_text)
{
    this.graphAnnoDiv.innerHTML = new_text;
}

// move annotation box to new X position
Graph.prototype.annotateMove = function(new_x)
{
    var style = this.graphAnnoDiv.style;

    new_x += 'px';
    style.left = new_x;
}

//////////////////////////////
// Methods to configure the graph instance.

Graph.prototype.setTitle = function(title, subtitle)
{
    this.graphTitle1 = title;
    this.graphTitle2 = subtitle;
}

//////////////////////////////
// Bind the event handlers to the Graph instance 'this'

Graph.prototype.bindThis = function()
{
    this.refresh = this.refresh.bind(this);
    this.onmousemove = this.onMouseMove.bind(this);
    this.onmousedown = this.onMouseDown.bind(this);
    this.onmouseup = this.onMouseUp.bind(this);

    // plug our event handlers into the document
    document.onmousemove = this.onmousemove;
    document.onmousedown = this.onmousedown;
    document.onmouseup = this.onmouseup;
}

//if (document.captureEvents)
//{
//    document.captureEvents(Event.MOUSEMOVE);
//}

