Why do python programmers use 'self'?
=====================================

Occasionally we see questions on `/r/learnpython`__ and elsewhere:

::

    Why the heck does everybody use 'self' so much?

.. __: https://www.reddit.com/r/learnpython/

The answer is: **TRADITION!**
(cue the song from *Fiddler on the Roof*).

Object Oriented Python
----------------------

The real answer is due to the way Python's Object system works.

Suppose we have a very simple class:

::

    class Test(object):

        def __init__(self):
            """Set instance .number to 0."""

            self.number = 0

        def bump_print(self, bump):
            """Bump the .number and then print it."""

            self.number += bump
            print('.number=%d' % self.number)

(The above code will run in python 2.x and in 3.x.)

Note the ``self`` variables above.  They appear in the parameter list to the
``__init__()`` and ``bump_print()`` methods of the class ``Test``.

If we then execute this code:

::

    a = Test()
    a.bump_print(2)
    a.bump_print(3)

we would see the output:

::

    .number=2
    .number=5

When the class definition above is compiled there are no existing instances of
class ``Test``, but an instance method **must operate on a class instance**.
So when we call an instance method at runtime we must tell the method which
instance we are operating on.  The first parameter in the call to an instance
method is always a reference to the instance the method is operating on.

For example, in the above code:

::

    a.bump_print(2)

can be thought of as a call to a method of a class with the object reference
being passed as the first parameter:

::

    <CLASS>.bump_print(a, 2)

This instance reference (the first parameter) can have any valid name in the
method implementation, but ``self`` is traditional, to the extent that any other
name is now considered odd or suspicious.  User-supplied parameters, if any,
are after the ``self`` parameter.

Note that other languages hide this reference passing to some extent.  Java, for
instance, doesn't explicitly pass its ``this`` parameter in the method parameter
list, it just magically appears in the environment of the method code.

Whether the python ``self`` should be explicit or not has been discussed in the
past, but the BDFL has decided that the "explicit self" is `here to stay`__.

.. __: http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html

Note
----

Some people think of the ``__init__()`` method of a class as the **constructor**
and then get hung up on why the constructor is passed a reference to the new
instance.  The ``__init__()`` method is really an **initializer** and the
constructor itself is hidden away in the python runtime code.  The constructor
calls the initializer and must pass a reference to the newly constructed instance.
