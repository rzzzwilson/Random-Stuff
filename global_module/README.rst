A Global Module
===============

There has been talk over the years of a python Singleton object.  Possibly
the best known of these is the `Borg pattern`_ introduced by Alex Martelli.

.. _`Borg pattern`: https://github.com/rzzzwilson/morse/blob/master/morse/design.rst

Alex, and others I think, have pointed out that a plain python module also
behaves as a singleton.  You can define, access and modify any attributes of
a module you want.  The simplest example of this uses an **empty** module 'fred':

::

    import fred

    fred.tom = 'tom'
    fred.dick = 2
    fred.harry = (3.0, 'harry')

Other modules can import the 'fred' module and gain access to its attributes in
a global manner.  When the python code terminates the singleton data is lost.

A persistent global module
--------------------------

The code here is an experiment in providing persistance for the global module.
I initially hoped that the module ``__del__()`` method could be used to
automatically save the module state to disk, but testing showed that idea
doesn't work.

So to save/restore the global module state use:

::

    singleton.load(filename)
    singleton.save(filename)

where ``filename`` is optional and it not supplied the save filename is
``singleton.state``.

There is also a method used internally that may be useful to end users:

::

    payload = singleton.payload()

whiich returns a dictionary of all gloabl attributes and there values.

Testing
-------

A simple test of the singleton module is in ``test.py`` and ``test3.py``.

