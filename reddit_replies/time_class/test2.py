import time

class MyClass(object):
    def __init__(self,label):
        self.label = label

def myfunc1():
    my_dict = {}
    my_dict['a'] = 'a'

def myfunc2():
    my_dict = {}
    my_dict['a'] = MyClass('a')

start = time.time()
myfunc1()
delta = time.time() - start
print(f'myfunc1(): {delta*1000000:1.10f}s')

start = time.time()
myfunc2()
delta = time.time() - start
print(f'myfunc2(): {delta*1000000:1.10f}s')

