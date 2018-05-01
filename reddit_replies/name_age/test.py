'''
Don't know why the young 'uns want to use "regex" for EVERYTHING.
'''

a = input('What is your name and age?')
(name, age) = a.strip().split()
age = int(age)
print(f'name={name}, age={age}')
