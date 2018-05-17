from somewhere import Ref

a = Ref(1)
b = a
a.obj = 2
assert b.obj == 2
