Tuple Implementation
====================

We now implement and test the *tuple* SLL idea.

The testing code will 




Testing Implementations
=======================

Being good little programmers, we start thinking about testing our code, of
course!  Here we will use the python *unittest* module.

Our test code, like all test code, should really test the implementation of an
abstract singly-linked list.  Exactly how the SLL is implemented is of no
concern.  The test code could be written by someone other than the SLL
implementor.  This means that if we are clever enough, the same test code should
be able to test all three implementations.

One thing we want to do in testing is to ensure that an SLL we create has the
form we expect.  We could step through the list, but that requires knowledge
of how the list is implemented.  Another approach is to implement a method or
function that converts an SLL to a textual form.  This is what we will do.  In
a nod to the *python-way*, we implement a method or function *__str__()* which
returns a string indicating the structure of the SLL expressed as a python list.
This method/function is part of the implementation of each type of SLL and hides
the implementation details.

Which implementation should I use?
==================================

In python you wouldn't use *any* of the above approaches.  Python has good data
structures which already includes a *list* you can use.  But if your language
doesn't provide nice data structures and you need to implement an SLL (C, for
example) then you need to choose.

We choose the implementation method depending on the relative costs in:

* time, and
* space




























::

    import sll
    import unittest


    class TestSLL(unittest.TestCase):

        def test_sll_create(self):
            """Check a simple SLL creation."""

             my_list = sll.SLL('M')
             my_list = sll.SLL('q', my_list)
             my_list = sll.SLL(20, my_list)
             my_list = sll.SLL('A', my_list)

             my_list2 = sll.SLL('A',
                                sll.SLL(20,
                                        sll.SLL('q',
                                                sll.SLL('M'))))

             self.assertEqual(my_list, my_list2)

    if __name__ == '__main__':
        suite = unittest.makeSuite(TestSLL,'test')
        runner = unittest.TextTestRunner()
        runner.run(suite)

The test code is in *test_sll.py*.

The idea may be right, but when we run this we get:

::

    F
    ======================================================================
    FAIL: test_sll_create (__main__.TestSLL)
    Check a simple SLL creation.
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "test_sll.py", line 27, in test_sll_create
        self.assertEqual(my_list, my_list2)
    AssertionError: <sll.SLL object at 0x7f4dd03a7690> != <sll.SLL object at 0x7f4dd03a7790>

We forgot that comparing objects doesn't work as we only compare the objects at
the head of each SLL.  We need some method of comparing SLL.  One way is to
write another function that converts an SLL into a python list:

::

    def sll2list(sll):
        """Convert an SLL into a list."""

        result = []
        while sll is not None:
            result.append(sll.value)
            sll = sll.next
        result.reverse()
        return result

Now our test code can convert a constructed SLL into a list for the purposes of
comparison.  Of course, our test code also needs to test the *sll2list()*
function:

::

    def test_sll2list(self):
        """Check that sll2list() works."""

        my_list = sll.SLL('M')
        my_list = sll.SLL('q', my_list)
        my_list = sll.SLL(20, my_list)
        my_list = sll.SLL('A', my_list)
        expected = ['M', 'q', 20, 'A']

        self.assertEqual(sll.sll2list(my_list), expected)

    def test_sll_create(self):
        """Check a simple SLL creation."""

        my_list = sll.SLL('M')
        my_list = sll.SLL('q', my_list)
        my_list = sll.SLL(20, my_list)
        my_list = sll.SLL('A', my_list)

        my_list2 = sll.SLL('A',
                           sll.SLL(20,
                                   sll.SLL('q',
                                           sll.SLL('M'))))

        self.assertEqual(sll.sll2list(my_list), sll.sll2list(my_list2))

The above test code works perfectly.

Now we can test the *sll_len()* function:

::

    def test_sll_length(self):
        """Check that sll2list() works."""

        my_list = sll.SLL('M')
        my_list = sll.SLL('q', my_list)
        my_list = sll.SLL(20, my_list)
        my_list = sll.SLL('A', my_list)
        expected_len = 4

        self.assertEqual(sll.sll_len(my_list), expected_len)

    def test_sll_length2(self):
        """Check that sll2list() works on an empty list."""

        my_list = None
        expected_len = 0

        self.assertEqual(sll.sll_len(my_list), expected_len)

And that all works fine.

You get the idea.  Look in the *test_sll.py* file for all the test code.


