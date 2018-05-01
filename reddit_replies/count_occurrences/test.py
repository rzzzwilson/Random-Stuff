from collections import defaultdict

a = [('A', 'Dog'), ('A', 'Cat'), ('B', 'Cow')]
d = defaultdict(int)
for (k, v) in a:
    d[k] += 1
