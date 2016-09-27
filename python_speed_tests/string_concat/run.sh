#!/bin/bash

#
# Run the python speed test code and also run a memory-usage logging
# process in parallel.
#

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
rm -f *.out *.log *.png

# start the test suite (python2)
python test.py > test.2.out 2>&1 &
TEST_PID=$!
echo "Running 'python test.py' in process $TEST_PID"

# catch ^C so we can kill forked process if terminated
trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

# now run the memory-usage logging program
python memprof.py $TEST_PID test.2.log

python plot_memprof test.2.log "Memory usage of test.py - python2"

##################################################

# start the test suite (python3)
python3 test.py >> test.3.out 2>&1 &
TEST_PID=$!
echo "Running 'python3 test.py' in process $TEST_PID"

# catch ^C so we can kill forked process if terminated
trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

# now run the memory-usage logging program
python memprof.py $TEST_PID test.3.log

python plot_memprof test.3.log "Memory usage of test.py - python3"

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

##################################################

# start the test2 suite (python3)
python3 test2.py >> test2.3.out 2>&1 &
TEST_PID=$!
echo "Running 'python3 test2.py' in process $TEST_PID"

# catch ^C so we can kill forked process if terminated
trap "kill_test $TEST_PID; exit" SIGINT SIGTERM

# now run the memory-usage logging program
python memprof.py $TEST_PID test2.3.log

python plot_memprof test2.3.log "Memory usage of test2.py - python3"

