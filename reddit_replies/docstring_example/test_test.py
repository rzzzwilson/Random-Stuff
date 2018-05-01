import test

my_class = test.MyClass()

print(f'  module docstring={test.__doc__}')
print(f'   class docstring={test.MyClass.__doc__}')
print(f'  method docstring={my_class.my_method.__doc__}')
print(f'function docstring={test.my_function.__doc__}')
