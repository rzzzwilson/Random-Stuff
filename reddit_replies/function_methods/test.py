class Test:
    def foo(self):
        print('foo')

x = Test()
x.foo()

bar = x.foo  # note no parenthesis, just regular attribute access
#bar(x)       # calling this is the same as x.foo(), gets error!
bar()
x.foo()
