import json

dict_a = {1: 'one', 2: 'two', 3: 'three'}
dict_b = {100: 'one hundred', 200: 'two hundred'}
filename = 'test.txt'

# write dicts to the file
with open(filename, 'w') as fd:
    fd.write(json.dumps([dict_a, dict_b]))

# read dicts back from the file
with open(filename, 'r') as fd:
    (dict_x, dict_y) = json.load(fd)
print(f'original dict_x={dict_x}')
print(f'original dict_y={dict_y}')

# convert dict_x and dict_y to numeric keys
dict_x = {int(k): v for (k, v) in dict_x.items()}
dict_y = {int(k): v for (k, v) in dict_y.items()}

# test if dicts we read are the same as originals
if dict_x != dict_a:
    print('dict_x != dict_a:\n'
          f'dict_x={dict_x}\n'
          f'dict_a={dict_a}\n')

if dict_y != dict_b:
    print('dict_y != dict_b:\n'
          f'dict_y={dict_y}\n'
          f'dict_b={dict_b}\n')

