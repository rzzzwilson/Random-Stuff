a = [x for x in range(1, 20+1)]
window = 3
for i in range(4):         # just for testing, change this later
    avg = sum(a[i:window+i]) / window
    print('avg(%d)=%d' % (i, avg))
