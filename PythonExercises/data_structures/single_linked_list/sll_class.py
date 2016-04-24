#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Class implementation of a singly-linked list.
"""

# global reference to the imported module
Module = None


class SLL(object):

    class element(object):
        """A private class to hold a value+next."""

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, values=None):
        """Initialize SLL with 'values'."""

        self.sll = None

        if hasattr(values, '__iter__'):
            for v in values[::-1]:
                self.sll = self.element(v, self.sll)
        elif values is not None:
            self.sll = self.element(values)

    def _find_last(self):
        """Internal function to find last element in an SLL.

        Returns a reference to the last element in the given SLL.
        Returns None if the SLL is empty.
        """

        scan = self.sll

        if scan is None:
            return None

        while scan.next is not None:
            scan = scan.next

        return scan

    def length(self):
        """Return the count of elements in this SLL."""

        count = 0
        scan = self.sll

        while scan is not None:
            count += 1
            scan = scan.next

        return count

    def add_front(self, value):
        """Add an element containing 'value' to the front of the SLL."""

        self.sll = self.element(value, self.sll)
        return self.sll

    def add_back(self, value):
        """Add an element containing 'value' to the end of the SLL."""

        # get last element of SLL
        last = self._find_last()

        if last is None:
            self.sll = self.element(value, self.sll)
        else:
            last.next = self.element(value)

        return self.sll

    def find(self, find):
        """Find element value 'find' in this SLL.

        find  the element value to find

        Returns the index of the found value, else None.
        """

        scan = self.sll
        count = 0
        while scan is not None:
            if scan.value == find:
                return count
            scan = scan.next
            count += 1

        return None

    def add_after(self, find_value, value):
        """Add an element containing 'value' after the element containing 'find_value'.

        Adds after the first element found, not any subsequent elements with the
        same value.
        """

        scan = self.sll
        while scan is not None:
            if scan.value == find_value:
                scan.next = self.element(value, scan.next)
                break
            scan = scan.next

    def remove(self, find):
        """Find and remove element with value 'find' in this SLL.

        find  the element value to find and remove

        Returns a reference to the possibly modified SLL.
        """

        # a reference to the previous element before the current element
        last = None
        scan = self.sll

        while scan is not None:
            if scan.value == find:
                if last is None:
                    # first element is found
                    self.sll = scan.next
                else:
                    # remove from body of SLL
                    last.next = scan.next
                break
            last = scan
            scan = scan.next

        return self.sll

    def remove_first(self):
        """Remove the first element of an SLL.

        Return the new SLL head reference.
        """

        # if SLL is empty, do nothing
        if self.sll is None:
            return None

        # self.ssl is now a reference to second element
        self.sll = self.sll.next

    def remove_last(self):
        """Remove the last element of an SLL.

        Returns a reference to the modified SLL.  Note that SLL may only
        contain one element to begin with.
        """

        # find last and second-last elements in SLL
        prev = None
        scan = self.sll

        while scan is not None:
            if scan.next is None:
                if prev is None:
                    # only one element in SLL
                    return None
                # remove last element & return original 'sll'
                prev.next = None
                return self.sll
            prev = scan
            scan = scan.next

        # get here if sll is None


    def map_fun(self, func, *args):
        """Apply func(*args) to each element value in the sll."""

        scan = self.sll

        while scan is not None:
            scan.value = func(scan.value, *args)
            scan = scan.next

    def str(self):
        """Convert this SLL into a 'list' string."""

        result = []

        scan = self.sll
        while scan is not None:
            result.append(scan.value)
            scan = scan.next

        return str(result)
