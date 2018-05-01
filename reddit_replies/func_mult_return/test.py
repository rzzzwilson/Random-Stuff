def double_iterator(start1, value1, start2, value2, step=1):
    temp_start2 = start2
    for i in range(start1, value1, step):
        if i % value2 == 0:
            temp_start2 = start2
            yield i, temp_start2
        else:
            temp_start2 = temp_start2 + step
            yield i, temp_start2
a = double_iterator(0, 30, 0, 4)
print(list(a))
