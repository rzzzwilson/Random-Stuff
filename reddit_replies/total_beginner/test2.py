a = [x for x in range(1, 20+1)]
window = 3
for i in range(len(a)-window+1):
    avg = sum(a[i:window+i]) / window
    print('avg(%d)=%d' % (i, avg))
