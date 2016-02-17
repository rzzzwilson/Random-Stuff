#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simpler (?) interface to ConfigParser.

If we have a config file:
   [main]
   port=8080
   logfile=/Users/r-w/local_server.log

   [serve]
   directory=/Users/r-w/
             /Volumes/DATA
             execute=False

then it would be nice to use it like so:

    import config

    cfg = config.get_config('test.cfg')
    port = cfg.main.port
    for directory in cfg.serve.directory:
        # do something

Note that ALL config attributes are strings or lists of strings, so user
code must convert integer strings to integers, etc.  Similarly, User code
must fill in default values if a value is missing.  All this can be done
as a separate phase before using the config object.
"""

import ConfigParser


def get_config(config_file):
    """Read a config file and return a config object."""

    # constructor for the result objects
    class cfg_obj(object):
            pass

    # open INI file, get data
    config = ConfigParser.RawConfigParser()
    config.read(config_file)

    result = cfg_obj()

    for section in config.sections():
        options = config.options(section)

        section_object = cfg_obj()
        result.__setattr__(section, section_object)

        for option in options:
            value = config.get(section, option)
            value = value.split('\n')

            if len(value) > 1:
                setattr(section_object, option, value)
            else:
                setattr(section_object, option, value[0])

    return result

if __name__ == '__main__':
    import os
    import unittest
    import tempfile

    TempFilePrefix = 'ConfigTest'
#    TempFile = None
    PortNumber = 8080

    class MyTest(unittest.TestCase):

        Data = '''[main]
port=%d
logfile=/Users/r-w/local_server.log

[serve]
directory=/Users/r-w/
          /Volumes/DATA
execute=False''' % (PortNumber)

        def setUp(self):
            """create a temporary test file."""

            (_, self.temp_file) = tempfile.mkstemp(prefix=TempFilePrefix)
            with open(self.temp_file, 'wb') as handle:
                handle.write(self.Data)

        def tearDown(self):
            """Delete the temporary file."""

            os.remove(self.temp_file)

        def test_smoke(self):
            """Just open the config object."""

            cfg = get_config(self.temp_file)

        def test_simple(self):
            """Open the config object and get existing attribute."""

            cfg = get_config(self.temp_file)
            result = cfg.main.port
            msg = 'cfg.main.port should be %d, got %s' % (PortNumber, str(result))
            self.assertEqual(int(result), PortNumber, msg)

        def test_simple2(self):
            """Open the config object and get existing attribute."""

            cfg = get_config(self.temp_file)
            result = cfg.serve.directory
            msg = ('cfg.serve.directory should be 2 element list, got %s'
                   % str(result))
            self.assertEqual(len(result), 2, msg)

        def test_error(self):
            """Open the config object and get missing attribute."""

            cfg = get_config(self.temp_file)
            with self.assertRaises(AttributeError):
                result = cfg.main.port_NONE


    unittest.main()
