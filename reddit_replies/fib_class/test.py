class Fib:

    def __init__(self,value=0):
        self.value = value
    
    def next(self):
        if self.value==0:
            self.temp=self.value
            self.value,self.prev=(self.value+1),self.value
            return self
        else:
            self.value,self.prev=(self.value+self.prev),self.value
            return self
f = Fib(2)
print(f)
print(f.next())
print(f.next())
print(f.next())
print(f.next())

f.next()
