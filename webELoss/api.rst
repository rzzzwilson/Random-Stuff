webEloss API
============

This is the design document for the API to use the webELoss widget.

The widget is designed to fit into any web page you want.  Once the 
widget code is running the user will interact with it

Instantiation
-------------

To get an instance of a webELoss widget in your web page, you need
to:

* create a <div> that will contain the widget
* instantiate the widget

The <div> you create to contain the widget doesn't have to be empty,
but if it isn't you run the risk of the widget code fiddling with your
objects within the <div>.

A simple example that doesn't do anything:

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

Note that you need to link to the widget javascript and CSS files.

Configuration
-------------

There are many methods that the user may use to change the widget configuration.
Before we talk about them we need to define names for various parts of the
widget display.

.. image:: webeloss_1.png

Titles
------

The main- and sub-titles are changed this way:

::

    graph = new Graph("graph");
    graph.setTitle("New main title", "New sub title");

If the subtitle parameter is omitted the graph will have no subtitle.  If *both*
title parameters are missing then the graph will have no titles at all.

X Axis
------

The X axis has a title and a range.  In the example above the title is
"Depth (m)" and the range is -1 to +7.

Y Axis
------

The Y axis has a title and a range.  In the example above the title is
"Damage (%)" and the range is 0 to 100.

Miscellaneous
-------------

Various other things - colours, margins, etc.



