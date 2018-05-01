def is_odd(n):
    if n % 2:   # if remainder is non-zero it's odd
        return True
    else:
        return False

    # more professionally
#    return n % 2

for n in range(10):
    if is_odd(n) is True:
        print('%d is odd' % n)
    if is_odd(n) is False:
        print('%d is even' % n)
