def calc():
    while True:
        choice = input('Please choose your command: ')
        if choice == 'exit':
            break
        elif choice == 'clear':
            # more code
        elif choice == 'add':
            firstInt = int(input('Enter the first number: '))
            secondInt = int(input(str(firstInt) + ' + '))
            result = firstInt + secondInt
            print('Answer: ' + str(result))
        elif choice == 'sub':
            # more code
        elif choice == 'mul':
            # more code
        elif choice == 'div':
            # more code
        else:
            print('Invalid command')

print(info)     # 'info' defined as before
calc()
