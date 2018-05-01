def number_of_groups(l, n):
    """Split list 'l'into 'n' groups."""

    d = (len(l)+n-1) // n
    return [l[x:x+d] for x in range(0, len(l), d)]

l = [x for x in range(10)]
for n in range(1, 6):
    ll = number_of_groups(l, n)
    print(f'n={n}, ll={ll}')
