# Imports

import os

# Variables

__author__ = "Rodrigo 'ItsPaper' Muñoz"
__authoremail__ = "Rodrigo.mcuadrada@gmail.com"
__version__ = "Alpha"


ReplaceDict = {' ': 0,   'A': 1,   'B': 2,   'C': 3,   'D': 4,   'E': 5,   'F': 6,
               'G': 7,   'H': 8,   'I': 9,   'J': 10,  'K': 11,  'L': 12,  'M': 13,
               'N': 14,  'O': 15,  'P': 16,  'Q': 17,  'R': 18,  'S': 19,  'T': 20,
               'U': 21,  'V': 22,  'W': 23,  'X': 24,  'Y': 25,  'Z': 26,  '0': 'A',
               '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H',
               '8': 'I', '9': 'J',
               }

DecryptDict = {v: k for k, v in ReplaceDict.items()}

XDecryptDict = {  1: 'A',   2: 'B',   3: 'C',   4: 'D',   5: 'E',   6: 'F',   7: 'G',
                  8: 'H',   9: 'I',  10: 'J',  11: 'K',  12: 'L',  13: 'M',  14: 'N',
                 15: 'O',  16: 'P',  17: 'Q',  18: 'R',  19: 'S',  20: 'T',  21: 'U',
                 22: 'V',  23: 'W',  24: 'X',  25: 'Y',  26: 'Z', 'A': '0', 'B': '1',
                'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7', 'I': '8',
                'J': '9', 0: ' ',
               }

print('DecryptDict == XDecryptDict returns %s' % str(DecryptDict == XDecryptDict))

# Functions


def welcome():
    print("Welcome to IMES: Itspaper's Message Encryption System!")
    print("Made by: {}. You are using Version: {}".format(__author__, __version__))


def fetch():
#    os.system("cls")
    filename = input("Please enter file name...") + ".txt"
    print("Fetching file...")
    os.system("pause")
    try:
        file = open("{}".format(filename), "r")
        print("{} fetched!".format(filename))
#        os.system("pause")
        return filename
    except FileNotFoundError:
        print("{} does not exist...".format(filename))
#        os.system("pause")



def contact_us():
    print("Thank you for sending me your feedback at {}.".format(__authoremail__))


def grab_text(x):
    file = open("{}".format(x))
    txt = file.read()
    file.close()
    return txt

def replace(char):
    return ReplaceDict.get(char.upper(), char)

def new_file(x, y):
    try:
        file = open("{}".format(x), "r")
        file.close()
        os.remove("{}".format(x))
        new_file(x,y)
    except FileNotFoundError:
        file = open("{}".format(x), "w")
        file.write("THIS FILE HAS BEEN ENCRYPTED USING IMES\n")
        file.write(y)
        file.close()


def get_code():
    os.system("cls")
    code = input("Please enter encryption code...")
    if code == "":
        os.system("cls")
        code = input("Code must be at least one Character long...")
    return code


def check_int(x):
    try:
        int(x)
    except ValueError:
        return False
    return True
    
def encrypt():
    filename = fetch()
    code = get_code()
    original_code = len(code)
    code = original_code
    code_changed = 0
    replaced = 0
    if filename == None:
        return
    txt = grab_text(filename)
    etext = ""
    for char in txt:
        # For Each Character in text file replace character
        x = replace(char)
        y = check_int(x)
        if y is True:
            x += code
            while x > 26:
                x -= 26
        etext += str(x) + " "
        """Replaces each character in the text
        with its corresponding number from the alphabet +
        the number of letters in the code"""
        replaced += 1
        if replaced == original_code:
            code = code + original_code
            code_changed += 1
            replaced = 0
            """After the amount of replaced letters is the same
            of the number of letters in the code the number of letters
            in the code doubles"""
            if code_changed == original_code:
                """If the code has changed the same number of times
                than the number of letters in the original_code
                then the code goes back to its original form..."""
                code = original_code
                code_changed = 0
                replaced = 0
    imes_file = "IMES {}".format(filename)
    new_file(imes_file,etext)


def find_char(x):
    e_char = ""
    txt = []
    for char in x:
        if char == " ":
            txt.append(e_char)
            e_char = ""
            continue
        e_char += char
    return txt

def check_encrypted(x):
    file = open("{}".format(x), "r")
    x = file.readline()
    if x == "THIS FILE HAS BEEN ENCRYPTED USING IMES\n":
        y = file.read()
        file.close()
        return True, y
    else:
        print("File is Not encrypted!")
        os.system("pause")
        return False, False


def decryp_char(char):
    return DecryptDict.get(char, str(char))

def decrypt():
    filename = fetch()
    code = get_code()
    original_code = len(code)
    code = original_code
    replaced = 0
    code_changed = 0
    is_int = False
    decrypt_code = []
    if filename == None:
        return
    is_encrypted, txt = check_encrypted(filename)
    if is_encrypted is False:
        return
    txt = find_char(txt)
    for instance in txt:
        is_int = check_int(instance)
        if is_int is False:
            decrypt_code.append(instance)
            continue
        else:
            char = int(instance)
        char -= code
        replaced += 1
        if replaced == original_code:
            code += original_code
            code_changed += 1
            replaced = 0
            if code_changed == original_code:
                code = original_code
                code_changed = 0
                replaced = 0
        if char < 0:
            char += 26
        decrypt_code.append(char)
    dtxt = ""
    for char in decrypt_code:
        dchar = decryp_char(char)
        dtxt += dchar
    new_filename = input("Please enter the name for the new file...") + ".txt"
    while new_filename == ".txt":
        new_filename = input("Please enter a valid file name...") + ".txt"
    file = open("{}".format(new_filename), "w")
    file.write(dtxt)


def menu():
    os.system("cls")
    welcome()
    print("1.Encrypt File")
    print("2.Decrypt file")
    print("3.Send Feedback to author")
    menusel = input("Please enter the number of the option, or type exit to quit...")
    is_int = check_int(menusel)
    if is_int is True:
        if int(menusel) == 1:
            encrypt()
        elif int(menusel) == 2:
            decrypt()
        elif int(menusel) == 3:
            contact_us()
    elif menusel == "EXIT" or menusel == "exit" or menusel == "Exit":
        exit()
    else:
        print("Option not recognized! Please try again!")
        os.system("pause")


# Main Code

while True:
    menu()
