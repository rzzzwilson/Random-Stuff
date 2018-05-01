import os
 
numbers = [1, 2, 3]
keuze = {"V":"View list","F":"create + fill list","A":"append list","R":"remove last list","D":"delete list","S":"stop"}
 
for key, value in keuze.items():
    print(key+":", value)
 
while True:
 
    uinput = input("Keuze: ")
 
    if uinput in keuze:
        print("Running program: "+keuze[uinput])
 
        if uinput == "V":
            try:
                file = open("writetotxt2.txt", "r")
                viewlist = file.readlines()
                print([lines.strip("\n") for lines in viewlist])
                file.close()
            except FileNotFoundError:
                print("Bestand niet gevonden, Creeer eerst met F")
 
        elif uinput == "F":
            file = open("writetotxt2.txt", "w")
            for c in numbers:
                file.write(str(c)+"\n")
            file.close()
 
        elif uinput == "A":
            file = open("writetotxt2.txt", "a")
            for c in numbers:
                file.write(str(c)+"\n")
            file.close()
 
        elif uinput == "R":
            try:
                file = open("writetotxt2.txt", "r")
                lines = file.readlines()
                file.close()
                file = open("writetotxt2.txt", "w")
                for item in lines[0:-3]:
                    file.write(item)
                file.close()
            except FileNotFoundError:
                print("Bestand niet gevonden, Creeer eerst met F")
 
        elif uinput == "D":
            try:
                os.remove("writetotxt2.txt")
            except FileNotFoundError:
                print("Bestand niet gevonden, Creeer eerst met F")
 
        elif uinput == "S":
                print("S")
                break
 
    else:
        print("***** Uw keuze is niet gevonden, kies opniew:")
