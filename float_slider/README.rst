Overview
========

The wxPython slider widget handles only integers.  To handle floats one must
convert external float values to widget internal integer values and vice versa.

The general way to handle this is to make the custom **FloatSlider** widget look
as much like a normal slider as possible.  We need the user to supply functions
to convert between user units (floats) and the integer internal units.

The file **floatslider.py** shows one way to do this.  It bundles a Slider and
TextCtrl widget into the FloatSlider widget which is possibly more than you
need, but that's what I required at the time.

Example Usage
-------------

Just doing:

::

    python floatslider.py

should run a very simple test of the widget.

Dependencies
------------

Just wxPython.

Improvements
------------

I just threw this together while working on a project one day.  There's probably
better ways to do this.  Constructive criticism welcome!
