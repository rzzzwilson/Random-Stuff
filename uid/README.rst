The 'uid' code is an attempt to provide a data structure that manages
Unique Identifier (UID) for a system that requires sequential IDs.

The aims:

* O(1) or O(logN) performance for pop() and push()
* pop() returns the lowest sequence number free
* push() will make a single UID or list of UIDs reusable
* memory usage will be minimal
* a user-supplied prefix
