File Fixit
==========

This problem is quite simply stated.  The first question we have is "how do we
solve this?".

The problem is in two parts.  We must read the description of the existing
directories first and build some sort of data structure.

Next we read the list of required directories.  For each of these we look at
the data structure of existing directories and figure out how many *mkdir*
commands are required to create the directory (this may be 0).

The approach appears simple.  We create an in-memory tree of existing
directories in the first phase.  Then for each required directory in the second
phase we walk the tree, creating directories where required.  Each directory
created counts as one *mkdir*.

The in-memory tree starts with a root node containinng '/'.

We implement the above in **file_fixit.py**.  To make things easier on
ourselves, we build the program incrementally.  We copy **rope_intranet.py**
as a template since it already has a lot of boilerplate for handling options,
etc, in it.  Then we have to decide how we are going to represent the tree
in memory.  As an aid, we also write debug "print the tree" routines.  This
helps us ensure the "add given directories" phase is working.

Running this first attempt and hand-checking some cases with the small dataset
shows that it might be working.  Let's
`screw our courage to the sticking place <http://nfs.sparknotes.com/macbeth/page_44.html>`_
and submit it to Google (after removing our debug prints!).

The small dataset (**A-small-practice.in**) produces the output in
**file_fixit.py.small** which Google says is correct!  Generate the large
dataset output in **file_fixit.py.large**.  Google says this data is also
correct!

So that's that.  The program runs quickly withe sample datasets, so performance
may not be a problem, though real Google contest datasets may be different.

This was a little too simple.

-----------------------------

Of course, in the *real* world we have the **-p** option:

::

    MKDIR(1)                                                  User Commands                                                 MKDIR(1)
    
    NAME
           mkdir - make directories
    
    SYNOPSIS
           mkdir [OPTION]... DIRECTORY...
    
    DESCRIPTION
           Create the DIRECTORY(ies), if they do not already exist.
    
           Mandatory arguments to long options are mandatory for short options too.
    
           -m, --mode=MODE
                  set file mode (as in chmod), not a=rwx - umask
    
           -p, --parents
                  no error if existing, make parent directories as needed
    
