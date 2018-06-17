in_str = '(A1,19),(A2,4),(A3,2),(A4,1)'
print(f'in_str={in_str}')
tmp = in_str.replace('),(', '|')
tmp = tmp[1:-1].split('|')
out_str = []
for t in tmp:
    (a, b) = t.split(',')
    out_str.append((a, int(b)))
# "out_str" = [('A1',19),('A2',4),('A3',2),('A4',1)]
print(f'out_str={out_str}')

lines = ('[1,1,1,0]\n'
         '[1,1,0,1]\n'
         '[1,0,1,1]\n'
         '[0,1,1,1]')
print(f'lines:\n{lines}')
out_array = []
for l in lines.split():
    row = [int(val) for val in l[1:-1].split(',')]
    out_array.append(row)
print(f'out_array={out_array}')
