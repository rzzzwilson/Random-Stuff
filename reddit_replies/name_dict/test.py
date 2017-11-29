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
X = len(namelist)
print('X=%s' % str(X))
while X < 0:
    for namelist[X] in Names:
        print(namelist[X], "Occured" , Names.get(namelist[X]), "times.")
        X = X - 1
        print('namelist=%s' % str(namelist))
