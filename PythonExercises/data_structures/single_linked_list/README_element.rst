Element Implementation
======================

We now write the python code to implement the *element* approach.  All this
code is in the **sll_element.py** file.  We will put the test code into
**test_sll_element.py**.

Initialization
--------------

As shown before, we implement the actual *element* as a small two attribute
object:

::

    class SLL(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

To create an element we must provide the value being stored and the 
reference to the *next* element:

::

    my_list = SLL(12)
    my_list = SLL(99, my_list)
    my_list = SLL(37, my_list)

Note that the supplied *next* reference is assumed to be *None* if not supplied.

len = length(sll)
-----------------

The *length()* function is quite simple and straightforward:

::

    def length(sll):
        """Return the count of elements in 'sll'."""
     
        count = 0
     
        while sll is not None:
            count += 1
            sll = sll.next
     
        return count

Of course, after we implement each function we write test cases in
**test_sll.py**.  For the *length()* function we have:

::

    def test_length(self):
        """Check that length() works."""
    
        my_sll = sll.SLL('M')
        my_sll = sll.SLL('q', my_sll)
        my_sll = sll.SLL(20, my_sll)
        my_sll = sll.SLL('A', my_sll)
        expected_len = 4
    
        self.assertEqual(sll.length(my_sll), expected_len)
    
    def test_length2(self):
        """Check that len() works on an empty list."""
    
        my_sll = None
        expected_len = 0
    
        self.assertEqual(sll.length(my_sll), expected_len)
    
    def test_length3(self):
        """Check that length() works."""
    
        my_sll = sll.SLL('M')
        expected_len = 1
    
        self.assertEqual(sll.length(my_sll), expected_len)

We won't show any further testing code until we implement the *tuple*
approach unless there is some interesting point.

sll = add_front(sll, value)
---------------------------

This function adds a new element containing *value* at the front of an SLL.
The implementation code shows us how simple this is:

::

    def add_front(sll, value):
        """Add a new element containing 'value' at the front of an SLL.
     
        Returns a reference to the new head of the SLL.
        """
    
        new_sll = SLL(value, sll)
        return new_sll

sll = add_end(sll, value)
-------------------------

This function looks to be as easy to implement as the *add_front()* function,
but here we see the complications that arise even in a simple SLL:

::

    def add_end(sll, value):
        """Add a new element containing 'value' at the end of an SLL.
    
        Returns a reference to the head of the SLL.
        Just to be the same as add_front().
        """
    
        # find last element of the SLL
        last = _find_last(sll)
        if last is None:
            # SLL is empty
            return SLL(value)
    
        # add new element to end
        last.next = SLL(value)
        return sll

We must handle the special case of an empty SLL.

Note that we use a special helper function here: *_find_last(sll)*.  Since we
know there will be other times when we need to find the last element in a list
we define a special function for this operation.

The implementation complications are echoed in the testing code, as we must
test for both cases:

* an empty SLL
* a non-empty SLL

sll = find(sll, value)
----------------------

The function is used to find the first element in an SLL with the given value.
The function returns a reference to the found element.  This is basically a
reference to the entire sub-SLL starting at the found value.  Again we have to
handle the *empty* special case:

::

    def find(sll, val):
        """Find element value 'val' in an SLL.
    
        sll   the SLL to search in
        val   the element value to find
        
        Returns a reference to the element containing 'val'.  Return None if
        not found.
    
        The SLL is not assumed to be sorted.
        """
    
        while sll is not None:
            if sll.value == val:
                return sll
            sll = sll.next
        
        return None

sll = add_after(sll, find_value, value)
---------------------------------------

The *add_after()* function adds a new element containing *value* immediately
after a found element containing *find_value*.

::

    def add_after(sll, find_value, value):
        """Add an element containing 'value' after the element containing 'find_value'.
          
        Return a reference to the found element.
        If the element containing 'find_value' is not found, return None.

        Adds after the first element found, not any subsequent elements with the
        same value.
        """

        f = find(sll, find_value)
        if f is not None:
            f.next = SLL(value, f.next)
            return f
        return None

The code is simple.  We use the previously defined function *find()* to look
for the *value* value.

sll = remove(sll, find_value)
-----------------------------

The *remove()* function removes the first element in an SLL that contains the
given value.  If no such element is found the SLL remains unchanged:

::

    def remove(sll, find_value):
        """Find and remove element with value 'find_value' in an SLL.
    
        sll         the SLL to search in
        find_value  the element value to find and remove
    
        Returns a reference to the possibly modified SLL.  This may be different
        from the original 'sll' reference as the first element may be removed.
        """
    
        # a reference to the previous element before the 'sll' element
        last = None
        scan = sll
    
        while scan is not None:
            if scan.value == find_value:
                if last is None:
                    # found at the first element
                    return scan.next
                # found within SLL, remove & return original 'sll'
                last.next = scan.next
                return sll
            last = scan
            scan = scan.next
    
        return sll

We can't use the *find()* function here.  While this will find the element
containing the required value, we also need a reference to the *preceding*
element so we change its *next* value.  So we have search code that uses
*last* and *scan* pointers.  Extra complicatiobs are foubd here, as we need to
handle the special case where the found element is the first in the SLL.

We must be sure to handle the case where the SLL is empty, but this is not too
bad.

We also see another thing that touches on the API design of our implementation.
We should ask ourselves "what does each function return?".  The design decision
taken was to always return a reference to the SLL where it made sense.

In the *remove()* function it is something we **must do**, as the function may
remove the first element of the SLL and we must tell the calling code what the
new SLL head reference is.

sll = remove_first(sll)
-----------------------

The *remove_first()* function removes the first element of the given list:

::

    def remove_first(sll):
        """Remove the first element of an SLL.
    
        Return the new SLL head reference.
        """
    
        # if SLL is empty, do nothing
        if sll is None:
            return None
    
        # return reference to second element
        return sll.next

Again we see the special handling of the *empty* case.

Note that we don't do anything to delete the removed element.  Python will
garbage-collect it eventually.

sll = remove_last(sll)
----------------------

This function removes the last element in an SLL, if any:

::

    def remove_last(sll):
        """Remove the last element of an SLL.
    
        Returns a reference to the modified SLL.  Note that SLL may only
        contain one element to begin with.
        """
    
        # find last and second-last elements in SLL
        prev = None
        scan = sll
    
        while scan is not None:
            if scan.next is None:
                if prev is None:
                    # only one element in SLL
                    return None
                # remove last element & return original 'sll'
                prev.next = None
                return sll
            prev = scan
            scan = scan.next

This code has similar requirements to the *remove()* function:  we must find
the second-last element which is the one we modify.

string = __str__(sll)
---------------------

As we were writing the test cases we found we needed to compare two SLLs.
This could be done in a generalized computer science way but we decided to
simply take a leaf from the python book and create a function that behaves
like the object *__str__()* method.

The *element* implement function *__str__()* converts an SLL into a simple
python list and then returns the string produced by the builtin *str()*
function:

::

    def __str__(sll):
        """Convert an SLL into a 'list' string representation."""
    
        result = []
    
        while sll is not None:
            result.append(sll.value)
            sll = sll.next
    
        return str(result)

This allows a simple comparison of two SLL that is good enough for testing.
We can see this function in operation in this sample of testing code:

::

    def test_add_front(self):
        """Check that add_front() works for empty SLL."""
        
        old_sll = None
        new_sll = sll.add_front(old_sll, 'A')
        expected = ['A']
        
        self.assertEqual(sll.__str__(new_sll), str(expected))
        
    def test_add_front2(self):
        """Check that add_front() works on SLL with one element."""
        
        old_sll = sll.SLL(20)
        new_sll = sll.add_front(old_sll, 'M')
        expected = ['M', 20]
        
        self.assertEqual(sll.__str__(new_sll), str(expected))

At this point our implementation of the *element* code is complete and tested.
Again, the implementation code is in the **sll_element.py** file and the test
code is in **test_sll_element.py**.
