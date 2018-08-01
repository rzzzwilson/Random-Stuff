import time

LOOPS = 200000000

start = time.time()
for _ in range(LOOPS):
    """a comment?
    A longer line in a string that some think is a comment.
    An even longer line in a string that some think is a comment.
    """
    pass
delta = time.time() - start
print('       string comment: %.2fs' % delta)

start = time.time()
for _ in range(LOOPS):
    pass
delta2 = time.time() - start
print('    no string comment: %.2fs' % delta2)

percent_diff = 100*(delta - delta2)/delta2
print('String comment takes %.1f%% more time' % percent_diff)
