def f():
    return (2, 3)

x = 0
y = 1
(x, y) += f()
print(f'x={x}, y={y}')
