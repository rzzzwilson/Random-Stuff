A Global Module
===============

There has been talk over the years of a python Singleton object.  Possibly
the best known of these is the `Borg pattern`_ introduced by Alex Martelli.
This is one of the great pattern names!

.. _`Borg pattern`: http://code.activestate.com/recipes/66531-singleton-we-dont-need-no-stinkin-singleton-the-bo/

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

Of course, if you value your sanity you would **NEVER** add or modify any
attributes with names starting with the '_' character!

A persistant global module
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
``singleton.state``.  These methods do not save/restore any module attributes
with names strting with '_'.

There is also a method used internally that may be useful to end users:

::

    payload = singleton.payload()

whiich returns a dictionary of all user global attributes and their values.

Testing
-------

A simple test of the singleton module is in ``test.py`` and ``test3.py``.

