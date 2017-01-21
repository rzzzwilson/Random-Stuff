#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Code used in an answer to the Reddit question:
https://www.reddit.com/r/learnpython/comments/5nwdpb/how_to_convert_an_instance_to_another_instance/

Show how to create a new real instance of Dog given an existing instance of Animal.
"""

class Animal():
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

class Dog():
    def __init__(self, animal, health):
        self.animal = animal
        self.health = health

    def woof(self):
        print('Woof!')

    def get_age(self):
        return self.animal.age

dog = Animal(10, 'male')
new_dog = Dog(dog, 100)
new_dog.woof()
print("I'm a dog, and my age is %d." % new_dog.get_age())
