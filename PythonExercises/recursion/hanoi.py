import sys

def hanoi(n, src, dst, tmp):
    if n > 0:
        hanoi(n-1, src, tmp, dst)
        print('move %s to %s' % (src, dst))
        hanoi(n-1, tmp, dst, src)

number = int(sys.argv[1])
hanoi(number, 'A', 'B', 'C')
