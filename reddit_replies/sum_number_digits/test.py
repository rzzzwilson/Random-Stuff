number = input('Enter a number: ')
result = 0
for ch in number:
    digit = int(ch)
    result += digit
print(f'Number {number} has sum {result}')
