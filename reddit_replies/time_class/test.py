import timeit

class MyClass(object):
    def __init__(self,label):
        self.label = label

def myfunc1():
    my_dict = {}
    my_dict['a'] = 'a'

def myfunc2():
    my_dict = {}
    my_dict['a'] = MyClass('a')

print(timeit.timeit('myfunc1()','from __main__ import myfunc1'))
print(timeit.timeit('myfunc2()','from __main__ import myfunc2'))
