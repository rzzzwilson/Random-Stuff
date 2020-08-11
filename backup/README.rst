backup
======

This program has been used since about 2004.  It is used to backup
a selection of directories to an external hard drive.  Some of its
features are:

* the target external drive must be mounted and correct
* target backups are saved in a timestamped directory
* use the rsync "link to old backup" feature to save space and time
* performs a target filesystem check if requested

This program has now been rewritten into python and enhanced with
things like:

* allow external and local source directories
* allow external and local target directories
* use "volume ID" file on external source/target disks
* etc

The file "backup.py" is this new rewrite.  The "issues" system will be used
to keep track of desired enhancements and progress.
