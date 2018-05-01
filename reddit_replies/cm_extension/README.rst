The code here was prompted by this reddit posting:

https://www.reddit.com/r/learnpython/comments/7im7ix/question_for_my_testlearning_script_python3/

The user's original code is in **test.py**.

**test2.py** is my simplified and cleaned up version of test.py with local usage
of the "with" statement.

**test3.py** is the version with a simple fileopen() function that moves all the
try/except code into the function, but closes the file.  Dutch messages replaced
with English.  The `fileopen()` function is::

    def fileopen(fname, mode):
        try:
            fd = open(fname, mode)
        except FileNotFoundError as e:
            print(f'File {fname} not found, mode is {mode}')
            return None
        return fd

And we use the function this way::

    if uinput == 'V':
        fd = open(FileName, 'r')
        viewlist = fd.readlines()
        fd.close()

This is less than satisfactory.  We would like to still use the "context manager"
to automatically close files.

**test4.py** is an attempt to enhance *test3.py* to use context managers.  The
idea is to try using the "fd" returned by the fileopen() function above as a
context manager.  That is, we want to be able to do::

        if uinput == 'V':
            with fileopen(FileName, 'r') as fd:
                viewlist = fd.readlines()

This *should* work, but there will probably be a problem when the fileopen()
function encounters an error::

    Keuze: d
    Running program: delete list                # file deleted here
    Keuze: v
    Running program: View list                  # view contents of the deleted file
    File writetotxt2.txt not found, mode is r   # error message, so far so good
    Traceback (most recent call last):          # but ERROR
      File "test4.py", line 26, in <module>     #    because "fd" isn't really a context managet
        with fileopen(FileName, 'r') as fd:
    AttributeError: __enter__

**test5.py** is a rewrite of fileopen() to be a real context manager.  One
problem we must solve here is what happens if there is a problem in the fileopen()
function.  We want the "with" block of code to be skipped in that case.

