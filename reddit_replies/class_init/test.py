class Test:
    def __init__(self):
        pass

class Test2:
    def test(self):
        pass

t = Test()
print(str(dir(t)))
t2 = Test2()
print(str(dir(t2)))
