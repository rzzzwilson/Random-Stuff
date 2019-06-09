#!/bin/bash

#
# Run the python speed test code and also run a memory-usage logging
# process in parallel.
#

OUTPUT="results.rst"

# function to handle termination
# usage: kill_test pid
function kill_test
{
    echo "Killing: $1"

    # decide if process still exists
    kill -0 $1 >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        kill -9 $1 >/dev/null 2>&1
    fi
}

# check the generated string files for equality
function check_files()
{
    DATA_FILES=$(ls *.data)
    LAST_FILE=""
    for F in $DATA_FILES; do
        if [ "$LAST_FILE" != "" ]; then
            if ! cmp $F $LAST_FILE; then
                echo "Files '$F' and '$LAST_FILE' differ!?"
                exit 1
            fi
        fi
        LAST_FILE=$F
    done
    rm -f *.data
}

# delete any old files
rm -f *.out *.log test*.png $OUTPUT *.data

# start the results file
cat <<EOF > $OUTPUT
Test Results
============

This shows the time taken for each test and the memory used for both python2 and
python3, with the garbage collector running and disabled.

Each test shows the timings in a table, followed by a graph showing memory
usage during the test.  The graph shows all the tests in the order as shown
in the timing table.  For instance, in the python2/test.py results immediately
below, we see four major peaks representing the usage for the naive, join,
stringio and comprehension methods respectively.

The *test.py* code tests each concatenation method in a direct manner.  Python
does have some optimizations it applies if it can recognize that string
concatenation is occurring.

The *test2.py* code is designed to disable the optimizations python performs on
string contenation.  The timing figures show expected results, but the memory
usage graphs show odd behaviour.  Still working on that!

EOF

# run all the tests, all combinations
for PYTHON in python python3; do
    for TEST in test.py test2.py; do
        for OPT in "" -g; do
            GC_STATE=ON
            if [ "$OPT" == "-g" ]; then
                GC_STATE=OFF
            fi
            OUTFILE=$TEST.$PYTHON$OPT.out
            LOGFILE=$TEST.$PYTHON$OPT.log
            $PYTHON $TEST $OPT >$OUTFILE 2>&1 &
            TEST_PID=$!
            echo "Running '$PYTHON $TEST' in process $TEST_PID, GC $GC_STATE"

            # catch ^C so we can kill forked process if terminated
            trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

            # now run the memory-usage logging program
            python memprof.py $TEST_PID $LOGFILE

            # append results to the results file
            python plot_memprof $LOGFILE "Memory usage of $TEST - $PYTHON, GC $GC_STATE"
            echo "$PYTHON running $TEST (GC $GC_STATE)" >> $OUTPUT
            echo "-------------------------------" >> $OUTPUT
            echo "" >> $OUTPUT
            python make_table.py $OUTFILE >> $OUTPUT
            echo "" >> $OUTPUT
            echo ".. image:: $LOGFILE.png" >> $OUTPUT
            echo "" >> $OUTPUT

#	    check_files
        done
    done
done

