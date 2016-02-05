Here we test various ways of collecting counts into a dictionary.
We need to handle the case where a key is new and there's no entry
in the dictionary for that key.

Proposed methods I found on the 'net:

* use the dictionary .setdefault() method
* use the dictionary .get() method
* use defaultdict
* use a try/except construct to catch the KeyError

Running the test program produces:

::

    Using Python 2.7.11 on Darwin-15.3.0-x86_64-i386-64bit
     dict: took 14.46s
      get: took 13.04s
    ddict: took 6.50s
      try: took 8.09s
    All methods produce identical dictionaries

I used to use the **dictionary .get()** method, but I have now decided that 
**defaultdict** is the way to go if dict performance is critical.
