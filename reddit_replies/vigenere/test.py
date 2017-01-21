"""
https://www.reddit.com/r/Python/comments/5o7tyn/help_with_a_vigenere_cipher_in_python_for_cs50/
"""

import sys

def main():

    k = len(sys.argv)
    key = sys.argv[1]

    #Makes sure key is valid.

    if not k == 2:
        print("Please include a single keyword in your command line. Try again.")
        return 1;

    if not str.isalpha(key):
        print("Key must be all alphabetical characters. Try again.")
        return 2;

    #Turn strings into lists so they can be changed.
    keylist = list(key)
    message = input("Enter message to encode: ")
    m = len(message)
    messlist = list(message)

    #Loop through, checking each letter and converting as necessary.
    for i in range(m):

        for j in range(k):

            print('messlist=%s, i=%d, messlist[i]=%s' % (str(messlist), i, str(messlist[i])))

            if ord(messlist[i]) >= ord('A') and ord(messlist[i]) <= ord('Z'):
                messlist[i] = ((ord(messlist[i]) - ord('A')) + (ord(keylist[j]) - ord('A')) % 26) + ord('A')
            elif ord(messlist[i]) >= ord('a') and ord(messlist[i]) <= ord('z'):
                messlist[i] = ((ord(messlist[i]) - ord('a')) + (ord(keylist[j]) - ord('a')) % 26) + ord('a')

            if i == m:

                break

            if i == k - 1:

                i = -1

    "".join(messlist)
    print("{}".format(messlist))
    return 0

if __name__ == "__main__": main()

