number = input('Enter a float: ')

while (not isinstance(number, float)) or (number < .001):
    while not isinstance(number, float):
        print('Please enter a number only...')
        number = input('Enter a float: ')
    while number < .001:
        print('Please enter an amount equal to or larger than .001...')
        number = input('Enter a float: ')

print('Success! Try to break me in another way.')
