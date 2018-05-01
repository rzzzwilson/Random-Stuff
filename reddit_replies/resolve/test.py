import socket
import sys
import os

def getfile():
    strigedinput = str(input("Enter the file of hostnames to resolve. "))
    with open(strigedinput, 'r') as f:
        lines = f.readlines()   
    for line in lines:
        addresses = ("'" + line.replace('\n', '') + "'")
        print(addresses + socket.gethostbyname(addresses))
getfile()
