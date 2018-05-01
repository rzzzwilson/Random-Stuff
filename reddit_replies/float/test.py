number = 100
root = 6
for n in range(1, number + 1):
    result = n ** (1/root)
    guess = int(round(result, 15))    # possible integer root
    if guess**root == n:
        result = guess
    print('n=%d, root=%d, result=%s' % (n, root, str(result)))
