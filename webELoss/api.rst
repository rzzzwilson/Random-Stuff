webEloss API
============

This is the design document for the API to use the webELoss widget.

Instantiation
-------------

To get an instance of a webELoss widget in your web page, you need
to:

* create a *<div>* that will contain the widget
* instantiate the widget

The *<div>* you create to contain the widget doesn't have to be empty,
but if it isn't you run the risk of the widget code fiddling with your
objects within the <div>.

A simplistic example:

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
                    graph.setTitle("A new main title", "Short subtitle");
                    graph.refresh();
                }
            </script>
        </head>
        <body onload="run_js();">
            <div id="graph" class="graph" />
        </body>
    </html>

