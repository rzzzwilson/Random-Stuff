Names = dict()
namelist = []
loop = 1
while loop == 1:
    nameinput = input("Enter a name (write 'done' if finished): ")
    if nameinput == 'done':
        loop = 0
        print(Names)
        print(namelist)
    else:
        if nameinput not in namelist:
            Names[nameinput] = 1
            namelist.append(nameinput)
        else:
            Names[nameinput] = Names[nameinput] + 1

for (name, num) in Names.items():
    print(f'{name} occurred {num} times')
