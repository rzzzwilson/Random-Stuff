class Fib:

    def __init__(self):
        self.prev = 0
        self.value = 1
    
    def next(self):
        (self.prev, self.value) = (self.value, self.value + self.prev)
        return self.value

f = Fib()
print(f.next())
print(f.next())
print(f.next())
print(f.next())
print(f.next())
