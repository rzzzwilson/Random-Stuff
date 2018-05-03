#!/usr/bin/env python3

"""
A simpler (?) interface to configparser.
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

import os.path
import configparser

# default places to look for a config file
ConfigPlaces = ['~', '.']


def canonize(path):
    """Convert path to absolute form."""

    path = os.path.expanduser(path)
    path = os.path.expandvars(path)
    path = os.path.abspath(path)

    return path

def find_config(name, places=None):
    """Look for a config file of given prefix in the usual places.

    name    name of the config file to look for (just a base name)
    places  optional list of paths to search

    Returns the path to the first found config file or None if not found.
    """

    if places is None:
        places = ConfigPlaces

    for path in places:
        path = canonize(path)
        path = os.path.join(path, name)
        if os.path.exists(path) and os.path.isfile(path):
            return path

    return None

def get_config(config_file):
    """Read a config file and return a config object."""

    # constructor for the result objects
    class cfg_obj(object):
        pass

    # open INI file, get data
    config = configparser.RawConfigParser()
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

def list_config(cfg):
    """Get a list of lines describing the passed 'cfg'."""

    result = []

    for item in (x for x in dir(cfg) if not x.startswith('_')):
        item_attr = getattr(cfg, item)
        for item2 in (x for x in dir(item_attr) if not x.startswith('_')):
            value = getattr(item_attr, item2)
            result.append(f'{item}.{item2}={value}')

    return result


if __name__ == '__main__':
    import os
    import unittest
    import tempfile

    TempFilePrefix = 'ConfigTest'
    PortNumber = 8080
    LogFile = '/Users/r-w/backup.log'

    class MyTest(unittest.TestCase):

        Data = '''[main]
port=%d
logfile=%s
[serve]
directory=/Users/r-w/
          /Volumes/DATA
execute=False''' % (PortNumber, LogFile)

        def setUp(self):
            """create a few temporary test config files."""

            # list of filenames to use as config files
            (_, self.temp_file) = tempfile.mkstemp(prefix=TempFilePrefix)
            self.filenames = [self.temp_file, f'./{TempFilePrefix}', f'~/{TempFilePrefix}']

            # list of absolute paths to remove in teardown
            self.rm_filenames = []

            for fname in self.filenames:
                fname = canonize(fname)
                with open(fname, 'w') as handle:
                    handle.write(self.Data)
                self.rm_filenames.append(fname) # remember for teardown

        def tearDown(self):
            """Delete the temporary files."""

            for fname in self.rm_filenames:
                try:
                    os.remove(fname)
                except FileNotFoundError:
                    pass

        def test_smoke(self):
            """Just open the config object."""

            cfg = get_config(self.temp_file)

        def test_simple(self):
            """Open the config object and get existing attribute."""

            cfg = get_config(self.temp_file)
            result = cfg.main.port
            msg = 'cfg.main.port should be %d, got %s' % (PortNumber, str(result))
            self.assertEqual(int(result), PortNumber, msg)

        def test_simple_find_local(self):
            """Find the config file in the local directory and open the config
            object and get existing attribute.
            """

            home_file = os.path.join('~', TempFilePrefix)
            home_file = canonize(home_file)
            try:
                os.remove(home_file)
            except FileNotFoundError:
                pass

            # make up path to expected config file
            cwd = os.getcwd()
            expected_file = os.path.join(cwd, TempFilePrefix)

            filename = TempFilePrefix
            cfg_path = find_config(filename)
            msg = f"Expected to use file '{expected_file}' but got '{cfg_path}'"
            self.assertEqual(cfg_path, expected_file, msg)
            cfg = get_config(cfg_path)
            result = cfg.main.port
            msg = 'cfg.main.port should be %d, got %s' % (PortNumber, str(result))
            self.assertEqual(int(result), PortNumber, msg)

        def test_simple_find_home(self):
            """Find the config file in the home directory and open the config
            object and get existing attribute.
            """

            # make up path to expected config file
            expected_file = os.path.join('~', TempFilePrefix)
            expected_file = canonize(expected_file)

            os.remove(os.path.join('.', TempFilePrefix))
            filename = TempFilePrefix
            cfg_path = find_config(filename)
            msg = f"Expected to use file '{expected_file}' but got '{cfg_path}'"
            self.assertEqual(cfg_path, expected_file, msg)
            cfg = get_config(cfg_path)
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
