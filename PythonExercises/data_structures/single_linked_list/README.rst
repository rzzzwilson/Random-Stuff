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
special value that cannot be a reference to another element.  In
python we use the *None* value.  When drawing this special reference on a
whiteboard or in a picture we often just draw a large 'X' as shown above.
Sometimes we might only draw one line of the 'X' or even use the electrical
'earth' symbol:

.. image:: end_of_list.png
    :alt: Examples of different styles for end-of-list

SSL Operations
==============

Once we have an SSL there are many things we might do with it:

* get the length of the list
* add a new element at the front
* add a new element at the end
* find an element in the list
* add a new element after a found element
* remove an element in the list
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

And we would create the example linked list above in this way:

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

Following on from the SSL approach above, we could have written this as:

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

Element Implementation
======================

We now write the python code to implement the *element* approach.  All this
code is in the **ssl_element.py** file.  We will put the test code into
**test_ssl_element.py**.  Later, **test_ssl.py** will test all three
implementations.

len = length(ssl)
-----------------

The *length()* function is quite simple and straightforward:

::

    def length(ssl):
        """Return the count of elements in 'ssl'."""
     
        count = 0
     
        while ssl is not None:
            count += 1
            ssl = ssl.next
     
        return count

Of course, after we implement each function we write test cases in
**test_ssl.py**.  For the *length()* function we have:

::

    def test_length(self):
        """Check that length() works."""
    
        my_ssl = ssl.SSL('M')
        my_ssl = ssl.SSL('q', my_ssl)
        my_ssl = ssl.SSL(20, my_ssl)
        my_ssl = ssl.SSL('A', my_ssl)
        expected_len = 4
    
        self.assertEqual(ssl.length(my_ssl), expected_len)
    
    def test_length2(self):
        """Check that len() works on an empty list."""
    
        my_ssl = None
        expected_len = 0
    
        self.assertEqual(ssl.length(my_ssl), expected_len)
    
    def test_length3(self):
        """Check that length() works."""
    
        my_ssl = ssl.SSL('M')
        expected_len = 1
    
        self.assertEqual(ssl.length(my_ssl), expected_len)

We won't show any further testing code until we implement the *tuple*
approach unless there is some interesting point.

ssl = add_front(ssl, value)
---------------------------

This function adds a new element containing *value* at the front of an SSL.
The implementation code shows us how simple this is:

::

    def add_front(ssl, value):
        """Add a new element containing 'value' at the front of an SSL.
     
        Returns a reference to the new head of the SSL.
        """
    
        new_ssl = SSL(value, ssl)
        return new_ssl

ssl = add_end(ssl, value)
-------------------------

This function looks to be as easy to implement as the *add_front()* function,
but here we see the complications that arise even in a simple SSL:

::

    def add_end(ssl, value):
        """Add a new element containing 'value' at the end of an SSL.
    
        Returns a reference to the head of the SSL.
        Just to be the same as add_front().
        """
    
        # find last element of the SSL
        last = _find_last(ssl)
        if last is None:
            # SSL is empty
            return SSL(value)
    
        # add new element to end
        last.next = SSL(value)
        return ssl

We must handle the special case of an empty SSL.

Note that we use a special helper function here: *_find_last(ssl)*.  Since we
know there will be other times when we need to find the last element in a list
we define a special function for this operation.

The implementation complications are echoed in the testing code, as we must
test for both cases:

* an empty SSL
* a non-empty SSL

ssl = find(ssl, value)
----------------------

The function is used to find the first element in an SSL with the given value.
The function returns a reference to the found element.  This is basically a
reference to the entire sub-SSL starting at the found value.  Again we have to
handle the *empty* special case:

::

    def find(ssl, val):
        """Find element value 'val' in an SSL.
    
        ssl   the SSL to search in
        val   the element value to find
        
        Returns a reference to the element containing 'val'.  Return None if
        not found.
    
        The SSL is not assumed to be sorted.
        """
    
        while ssl is not None:
            if ssl.value == val:
                return ssl
            ssl = ssl.next
        
        return None

ssl = add_after(ssl, find_value, value)
---------------------------------------

The *add_after()* function adds a new element containing *value* immediately
after a found element containing *find_value*.

::

    def add_after(ssl, find_value, value):
        """Add an element containing 'value' after the element containing 'find_value'.
          
        Return a reference to the found element.
        If the element containing 'find_value' is not found, return None.

        Adds after the first element found, not any subsequent elements with the
        same value.
        """

        f = find(ssl, find_value)
        if f is not None:
            f.next = SSL(value, f.next)
            return f
        return None

The code is simple.  We use the previously defined function *find()* to look
for the *value* value.

ssl = remove(ssl, find_value)
-----------------------------

The *remove()* function removes the first element in an SSL that contains the
given value.  If no such element is found the SSL remains unchanged:

::

    def remove(ssl, find_value):
        """Find and remove element with value 'find_value' in an SSL.
    
        ssl         the SSL to search in
        find_value  the element value to find and remove
    
        Returns a reference to the possibly modified SSL.  This may be different
        from the original 'ssl' reference as the first element may be removed.
        """
    
        # a reference to the previous element before the 'ssl' element
        last = None
        scan = ssl
    
        while scan is not None:
            if scan.value == find_value:
                if last is None:
                    # found at the first element
                    return scan.next
                # found within SSL, remove & return original 'ssl'
                last.next = scan.next
                return ssl
            last = scan
            scan = scan.next
    
        return ssl

Here we see the *empty* complication cropping up again, bit it's not too bad.

We also see another thing that touches on the API design of our implementation.
We should ask ourselves "what does each function return?".  The design decision
taken was to always return a reference to the SSL where it made sense.

In the *remove()* function it is something we **must do**, as the function may
remove the first element of the SSL and we must tell the calling code what the
new SSL head reference is.

In the *find()* function we saw previously, we must tell the calling code
whether we found the value or not.  We could just return *True* or *false*,
but we decided to return the reference to the found element or *None* if
we didn't find the value.  This way, the calling code gets the binary result
of found or not as well as a reference to the found element so the code can
perhaps manipulate the found part of the SSL.

ssl = remove_first(ssl)
-----------------------

The *remove_first()* function removes the first element of the given list:

::

    def remove_first(ssl):
        """Remove the first element of an SSL.
    
        Return the new SSL head reference.
        """
    
        # if SSL is empty, do nothing
        if ssl is None:
            return None
    
        # return reference to second element
        return ssl.next

Again we see the special handling of the *empty* case.

Note that we don't do anything to delete the removed element.  Python will
garbage-collect it eventually.

ssl = remove_last(ssl)
----------------------

This function removes the last element in an SSL, if any:

::

    def remove_last(ssl):
        """Remove the last element of an SSL.
    
        Returns a reference to the modified SSL.  Note that SSL may only
        contain one element to begin with.
        """
    
        # find last and second-last elements in SSL
        prev = None
        scan = ssl
    
        while scan is not None:
            if scan.next is None:
                if prev is None:
                    # only one element in SSL
                    return None
                # remove last element & return original 'ssl'
                prev.next = None
                return ssl
            prev = scan
            scan = scan.next

string = __ssl__(ssl)
---------------------

As we were writing the test cases we found we needed to compare two SSLs.
This could be done in a generalized computer science way but we decided to
simply take a leaf from the python book and create a function that behaves
like the object *__str__()* method.

The *element* implement function *__str__()* converts an SSL into a simple
python list and then return the string produced by the *str()* function:

::

    def __str__(ssl):
        """Convert an SSL into a 'list' string representation."""
    
        result = []
    
        while ssl is not None:
            result.append(ssl.value)
            ssl = ssl.next
    
        return str(result)

This allows a simple comparison of two SSLs that is good enough for testing.
We can see this function in operation in this sample of testing code:

::

    def test_add_front(self):
        """Check that add_front() works for empty SSL."""
        
        old_ssl = None
        new_ssl = ssl.add_front(old_ssl, 'A')
        expected = ['A']
        
        self.assertEqual(ssl.__str__(new_ssl), str(expected))
        
    def test_add_front2(self):
        """Check that add_front() works on SSL with one element."""
        
        old_ssl = ssl.SSL(20)
        new_ssl = ssl.add_front(old_ssl, 'M')
        expected = ['M', 20]
        
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

At this point our implementation of the *element* code is complete and tested.
The implementation code is in the **ssl_element.py** file and the test code is
in **test_ssl_element.py**.

Tuple Implementation
====================

We now implement and test the *tuple* SSL idea.

The testing code will 




Testing Implementations
=======================

Being good little programmers, we start thinking about testing our code, of
course!  Here we will use the python *unittest* module.

Our test code, like all test code, should really test the implementation of an
abstract singly-linked list.  Exactly how the SSL is implemented is of no
concern.  The test code could be written by someone other than the SSL
implementor.  This means that if we are clever enough, the same test code should
be able to test all three implementations.

One thing we want to do in testing is to ensure that an SSL we create has the
form we expect.  We could step through the list, but that requires knowledge
of how the list is implemented.  Another approach is to implement a method or
function that converts an SSL to a textual form.  This is what we will do.  In
a nod to the *python-way*, we implement a method or function *__str__()* which
returns a string indicating the structure of the SSL expressed as a python list.
This method/function is part of the implementation of each type of SSL and hides
the implementation details.

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


