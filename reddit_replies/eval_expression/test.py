"""
A small program to investigate ideas from:

https://old.reddit.com/r/learnpython/comments/8jr27h/how_to_input_a_function_that_allows_numerical/
"""

# input an expression.  try "(x**2 + 1)/y"
expression = input('Expression: ')

exp_locals = {}

while True:
    try:
        result = eval(expression, {}, exp_locals)
        break
    except NameError as e:
        if 'is not defined' in str(e):
            # get name that isn't defined and put its value into the environment
            (_, name, _) = str(e).split("'")
            exp_locals[name] = int(input(f"Value for variable '{name}': "))
        else:
            raise

print(f'\n{expression} = {result}')
for (name, value) in exp_locals.items():
    print(f'when {name} = {value}')
