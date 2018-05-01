"""
Move files to appropriate destination based on file extension.
"""

import os


# lists of known file types: <file type> : <list of extensions>
extension_mapping = {
                     'Documents': ['.doc', '.docx', '.odt', '.pdf', '.rtf',
                                   '.tex', '.txt', '.wks', '.wps', '.wpd',
                                   '.ods', '.xlr', '.xls', '.xlsx', '.key',
                                   '.odp', '.pps', '.ppt', '.pptx', '.csv',
                                   '.dat', '.db', '.dbf', '.log', '.mdb',
                                   '.sav', '.sql', '.tar', '.xml'],

                     'Music': ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa',
                               '.ogg', '.wav', '.mwa', '.wpl'],

                     'Pictures': ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg',
                                  '.png', '.ps', '.psd', '.svg', '.tif', '.tiff'],

                     'Videos': ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v',
                                '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm',
                                '.swf', '.vob', '.wmv'],

                     'programs': ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com',
                                  '.exe', '.gadget', '.jar', '.py', '.wsf']
                    }

# we really want a dict: <extension> : <file type>
# convert 'extension_mapping' to the above form
extension_to_type = {ext: ftype for (ftype, extlist) in extension_mapping.items() for ext in extlist}

# could have inverted above dict using this
#extension_to_type = {}
#for (ftype, extlist) in extension_mapping.items():
#    for ext in extlist:
#        extension_to_type[ext] = ftype

def get_destination(extension_mapping, ext):
    """Return destination directory given an extension.
   
    Not sure this is worth a function now.
    Just do: destination = extension_to_type.get(ext, NOne)
    """

    # use dict.get() so we can return None if extension not found
    return extension_mapping.get(ext, None)


# make a list of all of the files and folders in the cwd
files = os.listdir()

# get the home directory
home_dir = os.path.expanduser('~')      # user running the script
#home_dir = os.path.expanduser('~fred')  # other user with name 'fred'
#                                        # may have permissions problem doing this

# take the files one at a time
for f in files:
    # we only want files, so ignore directories, etc
    if not os.path.isfile(f):
        print("Ignoring non-file '%s'\n" % f)
        continue

    # split file into two parts, file name and extension """
    filename, extension = os.path.splitext(f)

    # use the get_destination function to find the folder that it belongs in
    # is it worth calling a function for this now?
    destination = get_destination(extension_to_type, extension)

    # print out some checks to make sure everything is going alright
    if destination:
        # if the extension is recognized move the file
        print("File", f, 'has the extension', extension)
        print("And will be moved to", os.path.join(home_dir, destination))
        print("Current directory is", os.getcwd())

        # actually moving the file
        print("Would do: os.rename(%s, %s)\n"
              % (f, os.path.join(home_dir, destination, f)))
#        os.rename(f, os.path.join(home_dir, destination, f)
    else:
        print("Unknown extension for file '%s'\n" % f)
