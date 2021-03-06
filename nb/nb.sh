#!/bin/bash
######
# A program to automate backup and checking of the NOTEBOOK USB stick
######

# where we store the backups
BACKUP_BASE="$HOME/NOTEBOOK_Backups"

# limit (GB) to total backup size on disk
LIMIT=10

# decide if we are linux or MacOS
UNAME=$(uname)

usage()
{
    if [ $# -gt 0 ]; then
        echo $*
    echo
    fi

    echo "A program to backup the NOTEBOOK with automatic fsck."
    echo "usage: nb [-f]"
    echo "where -f turns off the automatic fsck of the NOTEBOOK."
}

abort()
{
    osascript -e "display dialog \"$1\" buttons {\"OK\"} default button \"OK\"" >/dev/null 2>&1
    exit 1
}

# umount and the check filesystem
fs_check()
{
    DEV=$1
    MNT=$2

    say "File system check"
    echo -n "Performing filesystem check on $DEV ... " 

    if [ "$UNAME" == "Linux" ]; then
        umount $MNT
        sudo fsck $DEV
        RES=$?
        if [ $RES -ne 0 ]; then
            echo "ERROR!!!!!!"
            say "Filesystem errors"
        else
            echo "OK"
        fi
    else
        diskutil repairVolume $MOUNT
        RES=$?
        if [ $RES -ne 0 ]; then
            echo "ERROR!!!!!!"
            say "Filesystem errors"
        else
            echo "OK"
        fi
        sleep 2
        diskutil unmount $DEV
        RES=$?
        if [ $RES -ne 0 ]; then
            echo "Dismount failed!?"
            say "Dismount failed"
        fi
    fi
}

# get size of directory in GB
total_size()
{
    BASE=$1

    if [ "$UNAME" == "Linux" ]; then
        SIZE=$(du -B g -d 0 $BASE | awk '{ print $1 }' | sed -e "s/G$//")
    else
        SIZE=$(du -g -d 0 $BACKUP_BASE | awk '{ print $1 }')
    fi
    echo $SIZE
}
######
# Start of program, check options
######

NOFSCK="N"

while getopts "hf" OPTION; do
  case $OPTION in
    h)
      usage
      exit 1
      ;;
    f)
      NOFSCK="Y"
      ;;
    ?)
      usage
      exit 1
      ;;
  esac
done

# determine if NOTEBOOK mounted, note the device and mount point
DF=$(df -h | grep NOTEBOOK)
if [ -z "$DF" ]; then
    echo "Sorry, NOTEBOOK not mounted."
    echo "If it's plugged in, double click on the icon first."
    abort "Sorry, NOTEBOOK isn't mounted.\n\nIf it's plugged in, double click on the icon first."
fi

DEVICE=$(echo $DF | awk '{ print $1 }')
if [ "$UNAME" == "Linux" ]; then
    MOUNT=$(echo $DF | awk '{ print $6 }')
else
    MOUNT=$(echo $DF | awk '{ print $9 }')
fi

# make sure the '.diskid' file exists on the device and contains 'NOTEBOOK'
if [ ! -f $MOUNT/.diskid ]; then
    abort "Sorry, the file $MOUNT/.diskid doesn't exist."
fi

FILE_CONTENTS=$(cat $MOUNT/.diskid)
if [ "$FILE_CONTENTS" != "NOTEBOOK" ]; then
    abort "Device is not a notebook:\n\n$MOUNT/.diskid contains '$FILE_CONTENTS',\nshould be 'NOTEBOOK'."
fi

# copy the 'nb' doing the backup to the NOTEBOOK
echo "Doing: cp $HOME/bin/nb $MOUNT/files/computer/bin/nb"
cp $HOME/bin/nb $MOUNT/files/computer/bin/nb

# get date/time, create backup directory
DATETIME=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR=$BACKUP_BASE/$DATETIME
mkdir -p $BACKUP_BASE/$DATETIME

# copy NOTEBOOK to backup
echo "Copying NOTEBOOK to $BACKUP_DIR"
rsync -q --links -r $MOUNT/* $BACKUP_DIR
cp $MOUNT/.diskid $BACKUP_DIR

# perform filesystem check on device, if required, and dismount
if [ "$NOFSCK" != "Y" ]; then
    fs_check $DEVICE $MOUNT
fi

# delete old backups if over the limit
while true; do
    # get total size of BASE_DIR in GB
    USE_SIZE=$(total_size $BACKUP_BASE)
    if [ $USE_SIZE -gt $LIMIT ]; then
        # delete oldest backup
        OLDEST=$(ls -dt $BACKUP_BASE/2* | tail -1)
        say "Deleting old directory"
        echo "Deleting: $OLDEST"
        rm -Rf $OLDEST
    else
        break
    fi
done

say "Backup finished"
