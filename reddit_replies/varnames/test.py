b = 2
def lol():
    a = 1
    print(str(lol.__code__.co_varnames))
    for x in lol.__code__.co_varnames:
        print(x)  
    for i in range(10):
        pass
    print(str(lol.__code__.co_varnames))
    print(i)
lol()
print(str(dir(locals())))
print(str(dir(globals())))
print(dir())
#vars = [vname for vname in dir() if not vname.startswith('__') and vname != 'vname']
vars = [vname for vname in dir() if not vname.startswith('__')]
print(str(vars))
