backup
======

This program has been used since about 2004.  It is used to backup
a selection of directories to an external hard drive.  Some of its
features are:

* the target external drive must be mounted and correct
* target backups are saved in a timestamped directory
* use the rsync "link to old backup" feature to save space and time
* performs a target filesystem check if requested

This program will eventually be rewritten into python and enhanced:

* allow external and local source directories
* use "volume ID" file on external source disks
* allow backup from only local or external sources
* allow skip of non-mounted external source disks
* allow filesystem check on source disks (external or local)
* allow execution on MacOS, Linux and, perhaps, Windows

The basic functionality of the bash program has been implemented in python.
The file "backup.py" is this new rewrite.  The "issues" system will be used
to keep track of desired enhancements and progress.
