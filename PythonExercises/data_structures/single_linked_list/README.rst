Single-Linked List
==================

This tutorial designs and tests python code that implements a *singly-linked
list* data structure (SLL).  An SSL is a special case of a generalized
`Linked List <https://en.wikipedia.org/wiki/Linked_list>`_.

Of course, we *could* implenent an SSL simply as a python list, but that
defeats the purpose of this tutorial, which is to show one or more ways to
actually implement a singly-linked list.  Doing this shows the student just
*why* some list operations are expensive and why some are cheap.

An SLL is usually drawn like this in the typical 'box and arrow' form:

.. image:: ssl.png
    :alt: A singly-linked list

We keep a reference to the first element of the list in some variable.  The
first element of the list consists of two parts: the value (12 in this case)
and a reference to the *next* element in the list.  This continues to the right
until the last element which contains a 'null' *next* reference which is just a
special value that cannot be a pointer or reference to another element.  In
python we use the *None* value.  When drawing this special reference on a
whiteboard or in a picture we often just draw a large 'X' as shown above.
Sometimes we might only draw one line of the 'X' or even use the electrical
'earth' symbol:

.. image:: end_of_list.png
    :alt: Examples of different styles for end-of-list

SSL Operations
==============

Once we have an SSL there are lots of things we want to do with it:

* get the length of the list
* add a new element at the front
* add a new element at the end
* find an element in the list
* remove a found element in the list
* add a new element after a found element
* remove the first element in the list
* remove the last element in the list

Implementation
==============

So, how are we going to do this in python?  Here are a few ways.

Use a class as a list element
-----------------------------

One obvious way is to define a class *SSL* that contains a *value* and *next*
reference:

::

    class SSL(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

And we would create the linked list above in this way:

::

    my_list = SSL(12, SSL(99, SSL(37))))

Or we could have done it this way, which may (or may not) be easier to read:

::

    my_list = SSL(12)
    my_list = SSL(99, my_list)
    my_list = SSL(37, my_list)

Use a tuple as a list element
-----------------------------

Another way would be to just use a 2-tuple:

::

    my_list = (37, None)
    my_list = (99, my_list)
    my_list = (12, my_list)

Foolowing on from the SSL approach above, we could have written this as:

::

    my_list = (12, (99, (37, None)))

which is shorter and brings some joy to the hearts of old Lisp programmers!

Define a List class
-------------------

We could also go full OOP and define an SSL class that has lots of state
and methods.  Everything is hidden away in the class:

::

    class SSL(object):
    
        class elem(object(object)):
            def __init__(self, value, next=None):
                self.value = value
                self.next = next
    
        def __init__(self):
            # some sort of initialization
            self.ssl = None
    
        def add_at front(self, value):
            self.ssl = elem(value, self.ssl)
    
        # etc
    
    my_list = SSL()
    my_list.add_at_end(12)
    my_list.add_at_end(99)
    my_list.add_at_end(37)

There are many other ways of implementing an SSL.  We will only examine the
three above.

All the *element* code is in the file **ssl_element.py**.  The *tuple* code
is in **ssl_tuple.py**, and the *class* code is in **ssl_class.py**.

List Length
-----------

For the *element* approach we create a function that returns the count of
elements in a given list:

::

    def length(ssl):
        """Return the count of elements in list 'ssl'."""
    
        count = 0
        while ssl is not None:
            count += 1
            ssl = ssl.next
        return count

The *tuple* approach requires slightly different code:

::

    def length(ssl):
        """Return the count of elements in list 'ssl'."""

        count = 0
        while ssl is not None:
            count += 1
            ssl = ssl[1]
        return count

The *class* approach does look simpler:

::

    my_list.length()

but we need to implement the *len()* method in the class:

::

    def length(self):
        """Return the count of elements in this list."""

        count = 0
        ssl = self.ssl
        while ssl is not None:
            count += 1
            ssl = ssl.next
        return count






Which implementation should I use?
==================================

In python you wouldn't use *any* of the above approaches.  Python has good data
structures which already includes a *list* you can use.  But if your language
doesn't provide nice data structures and you need to implement an SSL (C, for
example) then you need to choose.

We choose the implementation method depending on the relative costs in:

* time, and
* space




























::

    import ssl
    import unittest


    class TestSSL(unittest.TestCase):

        def test_ssl_create(self):
            """Check a simple SSL creation."""

             my_list = ssl.SSL('M')
             my_list = ssl.SSL('q', my_list)
             my_list = ssl.SSL(20, my_list)
             my_list = ssl.SSL('A', my_list)

             my_list2 = ssl.SSL('A',
                                ssl.SSL(20,
                                        ssl.SSL('q',
                                                ssl.SSL('M'))))

             self.assertEqual(my_list, my_list2)

    if __name__ == '__main__':
        suite = unittest.makeSuite(TestSSL,'test')
        runner = unittest.TextTestRunner()
        runner.run(suite)

The test code is in *test_ssl.py*.

The idea may be right, but when we run this we get:

::

    F
    ======================================================================
    FAIL: test_ssl_create (__main__.TestSSL)
    Check a simple SSL creation.
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "test_ssl.py", line 27, in test_ssl_create
        self.assertEqual(my_list, my_list2)
    AssertionError: <ssl.SSL object at 0x7f4dd03a7690> != <ssl.SSL object at 0x7f4dd03a7790>

We forgot that comparing objects doesn't work as we only compare the objects at
the head of each SSL.  We need some method of comparing SSLs.  One way is to
write another function that converts an SSL into a python list:

::

    def ssl2list(ssl):
        """Convert an SSL into a list."""

        result = []
        while ssl is not None:
            result.append(ssl.value)
            ssl = ssl.next
        result.reverse()
        return result

Now our test code can convert a constructed SSL into a list for the purposes of
comparison.  Of course, our test code also needs to test the *ssl2list()*
function:

::

    def test_ssl2list(self):
        """Check that ssl2list() works."""

        my_list = ssl.SSL('M')
        my_list = ssl.SSL('q', my_list)
        my_list = ssl.SSL(20, my_list)
        my_list = ssl.SSL('A', my_list)
        expected = ['M', 'q', 20, 'A']

        self.assertEqual(ssl.ssl2list(my_list), expected)

    def test_ssl_create(self):
        """Check a simple SSL creation."""

        my_list = ssl.SSL('M')
        my_list = ssl.SSL('q', my_list)
        my_list = ssl.SSL(20, my_list)
        my_list = ssl.SSL('A', my_list)

        my_list2 = ssl.SSL('A',
                           ssl.SSL(20,
                                   ssl.SSL('q',
                                           ssl.SSL('M'))))

        self.assertEqual(ssl.ssl2list(my_list), ssl.ssl2list(my_list2))

The above test code works perfectly.

Now we can test the *ssl_len()* function:

::

    def test_ssl_length(self):
        """Check that ssl2list() works."""

        my_list = ssl.SSL('M')
        my_list = ssl.SSL('q', my_list)
        my_list = ssl.SSL(20, my_list)
        my_list = ssl.SSL('A', my_list)
        expected_len = 4

        self.assertEqual(ssl.ssl_len(my_list), expected_len)

    def test_ssl_length2(self):
        """Check that ssl2list() works on an empty list."""

        my_list = None
        expected_len = 0

        self.assertEqual(ssl.ssl_len(my_list), expected_len)

And that all works fine.

You get the idea.  Look in the *test_ssl.py* file for all the test code.


