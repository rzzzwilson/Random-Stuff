import turtle
import math
import sys
import time
from turtle import *
 
s = float(input("Enter the length of the sides: "))
if s < 1:
    print("Error: Enter positive value for radius.")
    sys.exit()
 
n = eval(input("Enter the number of parallelograms in the pinwheel: "))
if n < 1:
    print("Error: Enter a positive number of parallelograms.")
    sys.exit()
   
color = input("Enter the color of the parallelogram: ")
 
 
def parallelogram(s, color):#creates a single parallelogram
    turtle.showturtle()
    turtle.shape('turtle')
    time.sleep(3)
    turtle.pensize(3)
    turtle.fillcolor(color)
    turtle.begin_fill()
    fd(s)
    turtle.left(45)
    fd(s)
    turtle.left(135)
    fd(s)
    turtle.left(45)
    fd(s)
    turtle.end_fill()
   
    turtle.done()
print(parallelogram(s, color))
 
#def pinwheel(s ,n, color):
#goal is for this function to call the parallelogram function and create a 8,4, and 3 parallelogram pinwheel
