#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Provide a data structure that manages Unique Identifier (UID)
integers and strings for a system that requires sequential IDs.

The aims:
. O(1) or O(logN) performance for pop() and push()
. pop() returns the lowest sequence number free
. push() will make a single UID reusable
. memory usage should be minimal
. a user-supplied prefix will be used with string PUIDs

Throws these exceptions:
    UIDNotAvailable  wanted UID is not available
    UIDNotInUse      tried to push UID not in use
    UIDBadPrefix     tried to push UID with unrecognized prefix
    UIDBadFormat     tried to push badly formatted UID
"""

import os
import sys


__version__ = '1.0'


class UIDNotAvailable(Exception):
    """Thrown if user wanted specific UID and it's not available."""

    def __init__(self, uid):
        self.message("Desired UID '%s' is not available" % str(uid))


class UIDNotInUse(Exception):
    """Thrown if user tries to free UID that is not in use."""

    def __init__(self, uid):
        self.message("Can't free UID '%s' because it isn't in use" % str(uid))

class UIDBadFormat(Exception):
    """Thrown if user tries to free UID with a bad format."""

    def __init__(self, uid):
        self.message("Can't free UID '%s' because it has a bad format"
                     % str(uid))


class UIDBadPrefix(Exception):
    """Thrown if user tries to push UID with unknown prefix."""

    def __init__(self, expected, uid):
        self.message("Can't push UID '%s', expected prefix '%s'"
                     % (uid, expected))


class UID(object):

    def __init__(self, uid_format=None):
        """Create a UID instance."""

        self.free = []
        self.next_higher = 0;
        self.uid_format = uid_format
        if uid_format is None:
            self.uid_format = '{0:d}'

    def pop(self, uid=None):
        """Provide the next free UID, or the 'uid' suggested.

        uid  the possible returned UID

        Throws UIDNotAvailable exception if 'uid' not available.
        """

        if uid is not None:
            # adjust internal state so we return 'uid', if possible
            if uid > self.next_higher:
                self.free.extend(range(self.next_higher, uid))
                self.free.insert(0, uid)
                self.next_higher = uid + 1
            else:
                # check if 'uid' is free
                if uid in self.free:
                    self.free.remove(uid)
                    self.free.insert(0, uid)
                else:
                    raise UIDNotAvailable(uid)

        try:
            result = self.free.pop(0)
        except IndexError:
            # free list empty, get new number and return that
            # TODO: more efficient to get more than one from self.next_higher?
            result = self.next_higher
            self.next_higher += 1

        return self.uid_format.format(result)

    def push(self, uid, fast=False):
        """Push a no-longer used UID back into the pool.

        uid   the UID number that is no longer needed
        fast  True if we need to be fast and not do a compact
        """

        # convert UID back to a number
        try:
            uid = int(uid)
        except ValueError:
            raise UIDBadFormat(uid)

        # check the UID has been issued
        if uid in self.free or uid >= self.next_higher:
            raise UIDNotInUse(uid)

        # put UID back into free list and sort
        self.free.append(uid)
        self.free.sort()

        # if we don't have to be fast try to compact self.free (simple approach)
        # TODO: make this faster
        while self.free[-1] == self.next_higher + 1:
            value = self.free.pop()
            self.next_higher -= 1

class PUID(UID):
    """Like a UID class, but has a user-supplied prefix and format string."""

    def __init__(self, prefix=None, uid_format=None):
        """Define a UID instance with:

        prefix  the prefix string to use
        uid_format  how to format the number part of the PUID
        """

        super().__init__(prefix=prefix)

        self.uid_format = uid_format
        if uid_format is None:
            self.uid_format = '%d'

    def pop(self, uid=None):
        """Get the next available UID."""

        value = super().pop(uid=uid)
        return self.prefix + value

    def push(self, uid, fast=False):
        """Push a no-longer used UID back into the pool.

        uid   the UID that is no longer needed
        fast  True if we need to be fast and not do a compact
        """

        if not uid.startswith(self.prefix):
            raise UIDBadPrefix(self.prefix, uid)

        num_uid = uid.replace(self.prefix, '')
        super().push(num_uid, fast=fast)
