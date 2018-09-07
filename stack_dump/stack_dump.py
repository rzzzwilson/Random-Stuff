"""
A class to dump execution stack frames as a debugging aid.
"""

import os
import io
import sys
import traceback


class StackDumpException(Exception):
    pass

class StackDump:

    MaxFilenameWidth = 12
    MaxLinenumberWidth = 3

    def __init__(self, stream=None, depth=None, verbose=None):
        # prepare the output stream
        if stream is None:
            stream = sys.stdout

        if isinstance(stream, str):
            # filename passed
            try:
                self.output = open(stream, 'w')
            except TypeError:
                sys.stderr.write("Supplied stream isn't file-like\n")
                raise StackDumpException("Supplied stream isn't file-like")
            except PermissionError:
                sys.stderr.write("Can't write to stream: permissions\n")
                raise StackDumpException("Can't write to stream: permissions")

        else:
            # assume it's a file-like writable object
            self.output = stream

        # if there is a problem with 'stream', find out early
        # we do this by announcing the start of dumping
        try:
            self.output.write('%s\n' % ('*'*60))
            self.output.write('StackDump: started\n')
            self.output.write('%s\n' % ('*'*60))
        except AttributeError:
            sys.stderr.write("Supplied stream isn't file-like\n")
            raise StackDumpException("Supplied stream isn't file-like")
        except io.UnsupportedOperation:
            sys.stderr.write("Supplied stream isn't writable\n")
            raise StackDumpException("Supplied stream isn't writable")

    def __call__(self, msg=None):
        # ensure we always have a string to write
        if msg is None:
            msg = ''

        # get caller information - look back for first module != <this module name>
        # after this, 'fname' and 'lnum' are module name and line number of call
        frames = traceback.extract_stack()
#        frames.reverse()

        try:
            (_, mod_name) = __name__.rsplit('.', 1)
        except ValueError:
            mod_name = __name__

        for (fpath, lnum, mname, _) in frames[::-1]:
            fname = os.path.basename(fpath).rsplit('.', 1)
            if len(fname) > 1:
                fname = fname[0]
            if fname != mod_name:
                break

        # dump execution stack to output
        self.output.write('%+*s:%-*d|%s\n' %
                          (self.MaxFilenameWidth, fname,
                           self.MaxLinenumberWidth, lnum, msg))

if __name__ == '__main__':
    sd = StackDump()
    sd()
