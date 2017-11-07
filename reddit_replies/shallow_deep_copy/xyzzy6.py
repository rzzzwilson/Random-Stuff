# show deep copy
import copy
x = [1, [2, 3]]
y = copy.deepcopy(x)
print(f'x={x}, id(x)={id(x)}')
print(f'y={y}, id(y)={id(y)}')
print(f'x[0]={x[0]}, id(x[0])={id(x[0])}')
print(f'y[0]={y[0]}, id(y[0])={id(y[0])}')
