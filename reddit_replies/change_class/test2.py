#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Code used in an answer to the Reddit question:
https://www.reddit.com/r/learnpython/comments/5nwdpb/how_to_convert_an_instance_to_another_instance/

Show how to create a new real instance of Dog given an existing instance of Animal.
"""

class Animal(object):
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

class Dog(Animal):
    def __init__(self, age, sex, health):
        super(Dog,self).__init__(age, sex)
        self.health = health

    def woof(self):
        print('Woof!')

def make_dog(animal_instance, health):
    """Return an instance of Dog given an Animal instance."""

    age = animal_instance.age
    sex = animal_instance.sex

    return Dog(age, sex, health)


dog = Animal(10, 'male')

new_dog = make_dog(dog, 100)

print(type(new_dog))
new_dog.woof()
