class Foo():

    def __init__(self, f, g):
        print('Foo() called')
        if f:
            self.f = f
        if g:
            self.g = g

    def f(self):
        print 'original f() called'

    def g(self):
        print 'original g() called'

    def h(self):
        print 'Start h()'
        self.f()
        self.g()
        print 'End h()'

def bar1():
    print 'bar1() called'

def bar2(self):
    print 'bar2()'

foo = Foo(bar1, None)
#foo = Foo(None, None)

foo.h()

foo.f()

#print('Replacing foo.f')
#bar1(None)
#foo.f = bar1
#foo.f(foo)

foo.g()
