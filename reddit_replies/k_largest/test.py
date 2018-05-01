Input = [1, 6, 2, 1, 6, 1]
ExpectedOutput = [1, 6]

freq = {}
for x in Input:
    try:
        freq[x] = freq[x] + 1
    except KeyError:
        freq[x] = 1

freq = sorted([(val, key) for (key, val) in freq.items()], reverse=True)

out = [n for (f, n) in freq[:2]]

print(f'           out={str(out)}')
print(f'ExpectedOutput={str(ExpectedOutput)}')
