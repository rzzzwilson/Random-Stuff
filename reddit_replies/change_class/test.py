"""
https://www.reddit.com/r/learnpython/comments/5nwdpb/how_to_convert_an_instance_to_another_instance/
"""

class Animal(object):
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

class Dog(Animal):
    def __init__(self, age, sex, health):
        super(Dog,self).__init__(age, sex)
        self.health = health

dog = Animal(10, 'male')
dog.health = 100
dog.__class__ = Dog

print(type(dog))
dog.woof()
