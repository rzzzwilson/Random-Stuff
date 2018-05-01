names = None
with open('Pets.txt', 'r') as fR:
    for line in fR:
        if line.startswith('(Dog:'):
            # split out the dog names
            dogs = line[5:].strip()[:-1].split(',')

            #dogs = line[5:]         # remove '(Dog:' prefix
            #dogs = dogs.strip()     # get rid of leading/trailing whitespace
            #dogs = dogs[:-1]        # cut off trailing ')'
            #dogs = dogs.split(',')  # get single dog names with whitespace and '

            # remove the enclosing ''
            #names = [x.strip().strip("'") for x in dogs]
            names = [x.strip(" '") for x in dogs]
            break
print(names)
