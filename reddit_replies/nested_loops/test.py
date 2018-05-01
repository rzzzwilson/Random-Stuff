#Compares and prints same items between two lists

list_one = ['red', 'purple', 'blue', 'yellow', 'green']
list_two = ['puppies', 'football', 'purple', 'crayon', 'soccer', 'green']

for y in list_one:
    for x in list_two:
        if y == x:
            print y
