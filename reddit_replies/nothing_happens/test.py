import sys
import crypt
import string

def checkPass(password, salt, hashString):
    return 
    hashP = crypt.crypt(password, salt)
    if hashString == hashP:
        print(password)
        sys.exit
    
def main():
    hashString = sys.argv[1]
    alphabet = string.ascii_letters
    salt = '50'
    for char1 in alphabet:
        checkPass(char1, salt, hashString)
        for char2 in alphabet:
            checkPass(char1+char2, salt, hashString)
            for char3 in alphabet:
                checkPass(char1+char2+char3, salt, hashString)
                for char4 in alphabet:
                    checkPass(char1+char2+char3+char4, salt, hashString)
                    for char5 in alphabet:
                        print(f'password={char1+char2+char3+char4+char5}')
                        checkPass(char1+char2+char3+char4+char5, salt, hashString)

if __name__ == "__main__":
    main()
