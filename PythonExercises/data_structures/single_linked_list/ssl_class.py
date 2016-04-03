#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Class implementation of a singly-linked list.
"""


class SSL(object):

    class element(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, value, next=None):
        self.ssl = None

    def length(self):
        """Return the count of elements in this SSL."""

        count = 0

        while self is not None:
            count += 1
            self = self.next

        return count

    def add_prefix(self, value):
        """Add an element containing 'value' to the front of the SSL."""

        self.ssl = element(value, self.ssl)

    def add_suffix(self, value):
        """Add an element containing 'value' to the end of the SSL."""

        if self.ssl is None:
            # list is empty, add at fron
            self.ssl = element(value)
        else:
            scan = self.ssl
            while scan.next is not None:
                scan = scan.next
            scan.next = element(value)

    def find(self, find):
        """Find element value 'find' in this SSL.

        find  the element value to find

        Returns a reference to the element containing 'find'.  Return None if
        not found.
        """

        while self is not None:
            if self.value == find:
                return self
            self = self.next

        return None

    def ssl_remove(self, find):
        """Find and remove element with value 'find' in this SSL.

        find  the element value to find and remove

        Returns a reference to the removed element containing 'find'.  Returns None
        if not found.
        """

        # a reference to the previous element before the current element
        last = None

        while self is not None:
            if self.value == find:
                if last is not None:
                    last.next = self
                else:

                return
            last = self
            self = self.next

        return None

    def __str__(self):
        """Convert this SSL into a 'list' string."""

        result = []

        while self is not None:
            result.append(self.value)
            self = self.next
        result.reverse()

        return str(result)
