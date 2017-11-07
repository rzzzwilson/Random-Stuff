# show shallow copy
import copy
x = [1, [2, 3]]
y = copy.copy(x)
print(f'x={x}, id(x)={id(x)}')
print(f'y={y}, id(y)={id(y)}')
