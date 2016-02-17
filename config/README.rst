Overview
========

This is just a little bit of code to make actually using config information
in python code less verbose.

Suppose we have a configuration file in INI format, like this:

::

    [main]
    port=8080
    logfile=/Users/r-w/local_server.log

    [directories]
    /Users/r-w/
    /Volumes/DATA

The aim is to be able to use the information in the file in a less verbose
manner:

::

    import config

    cfg = config.get_config('test.cfg')
    port = cfg.main.port
    for directory in cfg.serve.directory:
        # do something

Note that ALL config attributes are strings or lists of strings, so user
code must convert integer strings to integers, etc.  Similarly, User code
must fill in default values if a value is missing.  All this can be done
as a separate phase before using the config object.

Later
-----

Could add code to:

* Coerce config attributes to a particular data type, like integer, boolean, etc.
* Supply a 'default' file (or string) that will set default values for attributes
  not defined in the original config file.
