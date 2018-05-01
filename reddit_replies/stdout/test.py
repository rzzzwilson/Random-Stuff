import sys
import time
for i in range(5):
    print '\rIteration %d' % i,
#    sys.stdout.flush()      # flush the stdout buffer
    time.sleep(1)
print '\nDone!'
