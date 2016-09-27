#!/bin/bash

#
# Run the python speed test code and also run a memory-usage logging
# process in parallel.
#

# catch ^C so we can kill forked process
trap "kill -9 $TEST_PID" SIGINT SIGTERM

# start the test suite, which waits a few seconds so we can set up logging
python test.py > test.log 2>&1 &
TEST_PID=$!
echo "TEST_PID=$TEST_PID"

# now run the memory-usage logging program
python memprof.py $TEST_PID memprof.log
