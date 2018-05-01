import os
 
FileName = 'writetotxt2.txt'
 
numbers = [1, 2, 3]
keuze = {'V': 'View list', 'F': 'create + fill list', 'A': 'append list',
         'R': 'remove last list' ,'D': 'delete list', 'S': 'stop'}

for key, value in keuze.items():
    print(key+':', value)

def fileopen(fname, mode):
    try:
        fd = open(fname, mode)
    except FileNotFoundError as e:
        print(f'File {fname} not found, mode is {mode}')
        return None
    return fd
 
while True:
    uinput = input('Keuze: ').upper()
    if uinput in keuze:
        print(f'Running program: {keuze[uinput]}')
 
        if uinput == 'V':
            with fileopen(FileName, 'r') as fd:
                viewlist = fd.readlines()
            print([lines.strip('\n') for lines in viewlist])
 
        elif uinput == 'F':
            with fileopen(FileName, 'w') as fd:
                for c in numbers:
                    fd.write(str(c)+'\n')
 
        elif uinput == 'A':
            with fileopen(FileName, 'a') as fd:
                for c in numbers:
                    fd.write(str(c)+'\n')
 
        elif uinput == 'R':
            with fileopen(FileName, 'r') as fd:
                lines = fd.readlines()
            with fileopen(FileName, 'w') as fd:
                for item in lines[0:-3]:
                    fd.write(item)
 
        elif uinput == 'D':
            try:
                os.remove(FileName)
            except FileNotFoundError:
                print(f'File {FileName} not found')
 
        elif uinput == 'S':
                print('Stopping')
                break
 
    else:
        print(f'***** Unrecognized command: {uinput}')
