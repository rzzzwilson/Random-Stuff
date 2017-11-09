#!/usr/bin/env python3

"""
A small program to perform a ROT13 translation on a string.

Usage: rot13.py

The program will read the string to translate from STDIN and
write the translated string to STDOUT.
"""

import codecs

def rot13(str):
    """Perform a ROT13 translation on a string and return it."""

    enc = codecs.getencoder("rot-13")
    return enc(str)[0]

if __name__ == '__main__':
    str = input('Enter string to ROT13: ')
    print(rot13(str))
