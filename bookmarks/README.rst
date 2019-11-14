After struggling long and hard with the so-called "synch" method of
coordinating bookmarks across many devices with Google Chrome, I've decided
to take control of the mess and manage my bookmarks myself.

This means I need tools to:

* Convert a Chrome HTML bookmarks file to a neutral format data file
* Sort a bookmark data file
* Convert a bookmark data file to a Chrome HTML bookmarks file

This will help me have a consistent and stable set of bookmarks across all
my devices running Chrome.  It will also ease any problems moving to another
browser.

Data file format
----------------

The "data" file has the format of one line per bookmark item, with each line
having this form:

    <path> <TAB> <URL>

where <path> is a `/` delimited absolute path with the last folder being the
                 bookmark name
and   <URL>  is the URL for the bookmark.
