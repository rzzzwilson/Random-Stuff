a = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
c = [0,-1,-2,-3,-4,-5,-6,-7,-8,-9, 0,-1,-2,-3,-4,-5]
my_list = [a, b, c]

expected = [[0, 5, 6, 0, 1, 5], [0, -5, -6, 0, -1, -5]]

zipped = zip(*my_list)

res_b = []                      # accumulate b and c results here
res_c = []

prev_a = None
prev_b = None
prev_c = None

for (aa, bb, cc) in zipped:
    if prev_a:
        # if we're not at first element
        if aa != prev_a:
            # it's a change
            res_b.append(prev_b)
            res_c.append(prev_c)
            res_b.append(bb)
            res_c.append(cc)
    else:
        res_b.append(bb)
        res_c.append(cc)
    prev_a = aa
    prev_b = bb
    prev_c = cc

res_b.append(my_list[1][-1])    # last of a and b always in list
res_c.append(my_list[2][-1])

result = [res_b, res_c]
print(f'  result={result}')
print(f'expected={expected}')
print(result == expected)
