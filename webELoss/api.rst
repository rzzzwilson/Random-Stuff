webEloss API
============

This is the design document for the API to use the webELoss widget.

The widget is designed to fit into any web page you want.  Once the 
widget code is running the user will interact with the graph and other widgets
on the page.

Instantiation
-------------

To get an instance of a webELoss widget in your web page, you need
to:

* create a <div> that will contain the widget
* instantiate the widget

The <div> you create to contain the widget doesn't have to be empty,
but if it isn't you run the risk of the widget code fiddling with your
objects within the <div>.

A simple example that doesn't do much:

::

    <!DOCTYPE html>
    <html xml:lang="en" lang="en">
        <head>
            <link rel="stylesheet" type="text/css" href="webeloss.css">
            <script src="webeloss.js"></script>
            <script type="text/javascript">
                function run_js()
                {
                    graph = new Graph("graph");     // pass the name of the container <div>
                }
            </script>
        </head>
        <body onload="run_js();">
            <div id="graph" class="graph" />
        </body>
    </html>

Note that you need to link to the widget javascript and CSS files.  Also note
the "run_js();" in the <body> "onload".

Configuration
-------------

There are many methods that the user may use to change the widget configuration.
Before we talk about them we need to define names for various parts of the
widget display.

.. image:: webeloss_1.png

The **graph** proper is the white rectangular area with a grey grid.  The darker
surround is the **margin**.  In the top margin we see the **maintitle** and
**subtitle**.  The left margin contains the **y axis label** and the bottom
margin contains the **x axis label**.

Titles
------

The maintitle and subtitle texts are changed this way:

::

    function run_js()
    {
        graph = new Graph("graph");
        graph.setTitle("New main title", "New sub title");
    }

If the subtitle parameter is omitted the graph will have no subtitle.  If *both*
title parameters are missing then the graph will have no titles at all.

The width of the top margin will vary depending on the presence or absence
of titles.

X Axis
------

The X axis has a label and a range.  In the example above the label is
"Depth (m)" and the range is -1 to +7.

::

    function run_js()
    {
        graph = new Graph("graph");
        graph.setX("New X axis label", min_x, max_x, step_x);
    }

The **min_x** and **max_x** parameters set the range limits and the
**step_x** parameter sets the step between X axis ticks.

If the **step_x** parameter is not supplied it is assumed to be **1**.

Y Axis
------

The Y axis has a label and a range.  In the example above the label is
"Damage (%)" and the range is 0 to 100.

::

    function run_js()
    {
        graph = new Graph("graph");
        graph.setY("New Y axis label", min_y, max_y, step_y);
    }

The **min_y** and **max_y** parameters set the range limits and the
**step_y** parameter sets the step between Y axis ticks.

If the **step_y** parameter is not supplied it is assumed to be **1**.

Miscellaneous
-------------

Various other things - colours, margins, etc.

Adding Data
===========

How to add data to the graph:

* damage curves
* depth markers
* reference curves

We add the various bits of data to the widget by supplying a single
javascript data structure:

::

    function run_js()
    {
        graph = new Graph("graph");
        graph.setData(data);
    }

The data structure ...

Retrieving Data
===============

Once the widget is configured the user may interact with it and change the
data given to it.  If we want to save the state of the widget and continue
another day we need to retrieve the modified data:

::

    function run_js()
    {
        graph = new Graph("graph");
    }
    
    // somewhere else in javascript
    data = graph.getData();

The ``getData()`` method returns a data structure describing the current state
of the widget.
