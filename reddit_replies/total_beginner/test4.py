def moving_average(data, window):
    result = []
    for i in range(len(data)-window+1):
        avg = sum(a[i:window+i]) / window
        result.append(avg)
    return result

a = [x for x in range(1, 20+1)]
window = 4
result = moving_average(a, window)

print('result=%s' % str(result))
