Single-Linked List
==================

This tutorial designs and tests python code that iplements a *singly-linked
list* data structure (SLL).  An SLL is usually drawn like this in the typical
'box and arrow' form:

.. image:: ssl.png
    :alt: A singly-linked list

This example shows a list that is referred by a variable *my_list*.  The
first element of the list consists of two parts: the value ('A' in this case)
and a reference to the *next* element in the list.  This continues to the right
until the last element which contains a 'null' reference which is just a special
value that cannot be a pointer or reference to another element.  In python we
use the *None* value.  When drawing this special reference on a whiteboard or
in a picture we often use the electical earth symbol, but sometimes you may see
it drawn like this:

.. image:: end_of_list.png
    :alt: An alternate way of drawing the 'null' reference

Of course, we *could* implenent an SSL simple as a python list, but that
defeats the purpose of this tutorial, which is to show one or more ways to
actually implement a singly-linked list.

Implementation
==============

So, how are we going to do this in python?

One obvious way is to define a class *SSL* that contains a *value* and *next*
reference:

::

    class SSL(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

And we would create the linked list above in this way:

::

    my_list = SSL('A',
                  SSL(20,
                      SSL('q',
                          SSL('M'))))

We could have done it this way, which may (or may not) be easier to read:

::

    my_list = SSL('M')
    my_list = SSL('q', my_list)
    my_list = SSL(20, my_list)
    my_list = SSL('A', my_list)

List Operations
===============

Once we have a list, we want to perform certain operations on it.  Things like:

* get the length of a list
* find an element in a list
* remove a found element in a list
* add a new element after a found element
* remove the first element in the list
* remove the last element in the list

and many others.

List Length
-----------

We create a function that returns the count of elements in a given list:

::

    def ssl_len(ssl):
        """Return the count of elements in list 'ssl'."""

        count = 0
        while ssl is not None:
            count += 1
            ssl = ssl.next
        return count

This code is in file *ssl.py*.

Once we write something like this the immediate thought that should occur to
you is "how do I test this?".  We use the python *unittest* module:

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

