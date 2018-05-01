# Compares and prints same items between two lists

list_one = ['red', 'purple', 'blue', 'yellow', 'green']
list_two = ['puppies', 'football', 'purple', 'crayon', 'soccer', 'green']

for x in list_two:
    if x in list_one:
        print x
