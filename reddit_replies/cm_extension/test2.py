import os
 
FileName = 'writetotxt2.txt'
 
numbers = [1, 2, 3]
keuze = {'V': 'View list', 'F': 'create + fill list', 'A': 'append list',
         'R': 'remove last list' ,'D': 'delete list', 'S': 'stop'}

for key, value in keuze.items():
    print(key+':', value)
 
while True:
    uinput = input('Keuze: ').upper()
    if uinput in keuze:
        print('Running program: '+keuze[uinput])
 
        if uinput == 'V':
            try:
                with open(FileName, 'r') as fd:
                    viewlist = fd.readlines()
                    print([lines.strip('\n') for lines in viewlist])
            except FileNotFoundError:
                print('Bestand niet gevonden, Creeer eerst met F')
 
        elif uinput == 'F':
            with open(FileName, 'w') as fd:
                for c in numbers:
                    fd.write(str(c)+'\n')
 
        elif uinput == 'A':
            with open(FileName, 'a') as fd:
                for c in numbers:
                    fd.write(str(c)+'\n')
 
        elif uinput == 'R':
            try:
                with open(FileName, 'r') as fd:
                    lines = fd.readlines()
                with open(FileName, 'w') as fd:
                    for item in lines[0:-3]:
                        file.write(item)
            except FileNotFoundError:
                print('Bestand niet gevonden, Creeer eerst met F')
 
        elif uinput == 'D':
            try:
                os.remove(FileName)
            except FileNotFoundError:
                print('Bestand niet gevonden, Creeer eerst met F')
 
        elif uinput == 'S':
                print('S')
                break
 
    else:
        print('***** Uw keuze is niet gevonden, kies opniew:')
