def MainFun(x, count=0):    # note "count=0", means use "0" if count not supplied
    print(f'MainFun: x={x}, count={count}')
    if (x % 2):
        count += 1
    if x == 1:
        return count
    else:
        return MainFun(x-1, count)

print(f'MainFun(5) returns {MainFun(5)}')
print(f'MainFun(8) returns {MainFun(8)}')
