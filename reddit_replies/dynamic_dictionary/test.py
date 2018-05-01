from copy import deepcopy

numbers_data = {
    "second" : 1,
    "third" : 2,
    "fourth" : 3,
    "fifth" : 4,
    "sixth" : 5,
    "seventh" : 6,
    "eighth" : 7,
    "ninth" : 8,
    "tenth" : 9
}

def addition():
    newaction = input ("That's not in my dictionary, would you like to add it?\n")
    if newaction not in ("yes", "no"):
        print("Please respond yes or no.\n")
    if newaction == "yes":
        newaction_id = input ("What's the identifier? ")
        newaction_val = input ("What's the Value? ")
        #might have to add a deep copy for multiple entries
        numbers_data[newaction_id] = newaction_val
        print(f'Done! Added "{newaction_id}": {newaction_val}')
        print(f'Dictionary = {numbers_data}')
        if newaction == "no":
            print("Okay, thank you!")
            main_menu()

def main_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("second")
    print("third")
    print("fourth")
    print("fifth")
    print("sixth")
    print("seventh")
    print("eighth")
    print("ninth")
    print("tenth")
    print(66 * "-")
    action = input ("Which number would you like to see?\n")
    if action not in ("second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"):
        addition()
    elif action == "second":
        print(numbers_data[action])
    elif action == "third":
        print(numbers_data[action])
    elif action == "fourth":
        print(numbers_data[action])
    elif action == "fifth":
        print(numbers_data[action])
    elif action == "sixth":
        print(numbers_data[action])
    elif action == "seventh":
        print(numbers_data[action])
    elif action == "eighth":
        print(numbers_data[action])
    elif action == "ninth":
        print(numbers_data[action])
    elif action == "tenth":
        print(numbers_data[action])

loop = True

while loop:
    while True:
        main_menu()
