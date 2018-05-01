FLOAT_MIN = 0.001
while True:
    try:
        number = float(input('Enter a float: '))
    except ValueError:
        print('Please enter a number only...')
        continue
    if number >= FLOAT_MIN:
        break
    print(f'Please enter an amount equal to or larger than {FLOAT_MIN}...')

print(f'number={number}')
