def foo(num):
    if isinstance(num, list):
        return [x+1 for x in num]
    else:
        return num + 1

print(f'foo(6)={foo(6)}')

print(f'foo([1,2,3])={foo([1,2,3])}')
