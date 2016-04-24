Single-Linked List
==================

This tutorial designs and tests python code that implements a *singly-linked
list* data structure (SLL).  An SLL is a special case of a generalized
`Linked List <https://en.wikipedia.org/wiki/Linked_list>`_.

Of course, we *could* implement an SLL simply as a python list, but that
defeats the purpose of this tutorial, which is to show one or more ways to
actually implement a singly-linked list.  Doing this shows the student just
*why* some list operations are expensive and why some are cheap.

An SLL is usually drawn like this in the typical 'box and arrow' form:

.. image:: sll.png
    :alt: A singly-linked list

We keep a reference to the first element of the list in some variable.  The
first element of the list consists of two parts: the value (12 in this case)
and a reference to the *next* element in the list.  This continues to the right
until the last element which contains a 'null' *next* reference, which is just a
special value that cannot be a reference to another element.  In
python we use the *None* value.  When drawing this special reference on a
whiteboard or in a picture we often just draw a large 'X' as shown above.
Sometimes you might see only one line of the 'X' or even the electrical
'earth' symbol:

.. image:: end_of_list.png
    :alt: Examples of different styles for end-of-list

SLL Operations
==============

Once we have an SLL there are many things we might do with it:

* get the length of the list
* add a new element at the front
* add a new element at the end
* remove the first element in the list
* remove the last element in the list
* find an element in the list
* add a new element after a found element
* remove a found element in the list
* do something with each value in order

Implementation
==============

So, how are we going to do this in python?  Here are a few ways.

Use a class as a list element
-----------------------------

One obvious way is to define a class *SLL* that contains a *value* and *next*
reference:

::

    class SLL(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

And we would create the example linked list above in this way:

::

    my_list = SLL(12, SLL(99, SLL(37))))

Or we could have done it this way, which may (or may not) be easier to read:

::

    my_list = SLL(12)
    my_list = SLL(99, my_list)
    my_list = SLL(37, my_list)

Use a tuple as a list element
-----------------------------

Another way would be to just use a 2-tuple:

::

    my_list = (37, None)
    my_list = (99, my_list)
    my_list = (12, my_list)

Following on from the SLL approach above, we could have written this as:

::

    my_list = (12, (99, (37, None)))

which is shorter and brings some joy to the hearts of old Lisp programmers!

Of course, tuples are *immutable*, so we have some trouble changing an SSL.
We actually implement the 'tuple' code with two element *lists*.

Define a List class
-------------------

We could also go full
`OOP <https://en.wikipedia.org/wiki/Object-oriented_programming>`_
and define an SLL class that has lots of state and methods.  Everything is
hidden away in the class:

::

    class SLL(object):
    
        class elem(object(object)):
            def __init__(self, value, next=None):
                self.value = value
                self.next = next
    
        def __init__(self):
            # some sort of initialization
            self.sll = None
    
        def add_at front(self, value):
            self.sll = elem(value, self.sll)
    
        # etc
    
    my_list = SLL()
    my_list.add_at_end(12)
    my_list.add_at_end(99)
    my_list.add_at_end(37)

Element Implementation
======================

There are many other ways of implementing an SLL.  We will only examine the
three above.  We discuss each implementation here:

* `element implementation <README_element.rst>`_
* `tuple implementation <README_tuple.rst>`_
* `class implementation <README_class.rst>`_
