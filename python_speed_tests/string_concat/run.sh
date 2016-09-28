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

# delete any produced files
rm -f *.out *.log *.png $OUTPUT

# start the results file
cat <<EOF > $OUTPUT
The results file.  Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.

EOF

# start the test suite (python2)
python test.py > test.2.out 2>&1 &
TEST_PID=$!
echo "Running 'python test.py' in process $TEST_PID"

# catch ^C so we can kill forked process if terminated
trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

# now run the memory-usage logging program
python memprof.py $TEST_PID test.2.log

# append results to the results file
python plot_memprof test.2.log "Memory usage of test.py - python2"
echo "python2 running test.py" >> $OUTPUT
echo "=======================" >> $OUTPUT
echo "" >> $OUTPUT
python make_table.py test.2.out >> $OUTPUT
echo "" >> $OUTPUT
echo ".. image:: test.2.log.png" >> $OUTPUT
echo "" >> $OUTPUT

##################################################

# start the test suite (python3)
python3 test.py >> test.3.out 2>&1 &
TEST_PID=$!
echo "Running 'python3 test.py' in process $TEST_PID"

# catch ^C so we can kill forked process if terminated
trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

# now run the memory-usage logging program
python memprof.py $TEST_PID test.3.log

# append results to the results file
python plot_memprof test.3.log "Memory usage of test.py - python3"
echo "python3 running test.py" >> $OUTPUT
echo "=======================" >> $OUTPUT
echo "" >> $OUTPUT
python make_table.py test.3.out >> $OUTPUT
echo "" >> $OUTPUT
echo ".. image:: test.3.log.png" >> $OUTPUT
echo "" >> $OUTPUT

##################################################

# start the test2 suite (python2)
python test2.py > test2.2.out 2>&1 &
TEST_PID=$!
echo "Running 'python test2.py' in process $TEST_PID"

# catch ^C so we can kill forked process if terminated
trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

# now run the memory-usage logging program
python memprof.py $TEST_PID test2.2.log

python plot_memprof test2.2.log "Memory usage of test2.py - python2"

# append results to the results file
python plot_memprof test2.2.log "Memory usage of test2.py - python2"
echo "python2 running test2.py" >> $OUTPUT
echo "=======================" >> $OUTPUT
echo "" >> $OUTPUT
python make_table.py test2.2.out >> $OUTPUT
echo "" >> $OUTPUT
echo ".. image:: test2.2.log.png" >> $OUTPUT
echo "" >> $OUTPUT

##################################################

# start the test2 suite (python3)
python3 test2.py >> test2.3.out 2>&1 &
TEST_PID=$!
echo "Running 'python3 test2.py' in process $TEST_PID"

# catch ^C so we can kill forked process if terminated
trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

# now run the memory-usage logging program
python memprof.py $TEST_PID test2.3.log

# append results to the results file
python plot_memprof test2.3.log "Memory usage of test2.py - python3"
echo "python3 running test2.py" >> $OUTPUT
echo "=======================" >> $OUTPUT
echo "" >> $OUTPUT
python make_table.py test2.3.out >> $OUTPUT
echo "" >> $OUTPUT
echo ".. image:: test2.3.log.png" >> $OUTPUT
echo "" >> $OUTPUT

