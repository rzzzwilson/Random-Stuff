import random
import time
 
def intro():
        print('Text Adventure')
        time.sleep(2)
        print('A Story')
        choice1()
        choice2()
        choice3()
 
 
 
def choice1():
    print("While walking you stumble across a path")
    time.sleep(2)
    print("Confused you are unsure of which way to go")
    time.sleep(2)
    path = input("Do you go right or left?")
    choice2(path)
 
def choice2(path):
    if path=="right":
        time.sleep(2)
        print("You go right")
        time.sleep(3)
        print("You see shady man in the woods")
        path2 = input("He asks if you want to see lizard, it has tongue that spits. Do you pet the lizard or no")
    elif path=="left":
        time.sleep(2)
        print("You encounter a thief, do you give him your watch or run away")
        path2 = input("Do you give him your watch or run away?")
 
    else:
        print("return")
 
        choice3(path2)
 
def choice3(path2):
        if path2=="pet":
                time.sleep(2)
                print("lizard spit in your face")
                time.sleep(2)
                print("RIP")
        elif path2=="no":
                time.sleep(2)
                print("blabla")
        elif path2=="give watch":
                print("you lost your watch")
        elif path2=="run away":
                print("thief catches you and kills you")
        else:
            print("return")
 
 
intro()
