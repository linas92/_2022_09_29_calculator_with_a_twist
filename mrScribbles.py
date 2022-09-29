from turtle import *
import tkinter as tk

# no idea what one to make first.
# i guess ill start with:
# 1. a basic tkinter interface and work a calculator in it with colors and buttons n stuff
# 2. then put a game inside a calculator. Sounds easy :DDDD Omg I went insane thinking about it :DDDDDDDD

# bet pirma, pazaisikite su situ nauju dalyku kuri perskaiciau :D


print("Hello dear friends and students!")
print("Welcome to the hidden game!")
print("These are the Calculators with a Twist - Game Instructions")
print("Thing is, I'm not the brightest, so you can only use 3 buttons!!!")
print("Or use the keyboard ^_^\nArrow up \"↑\" goes STRAIGHT")
print("Arrows left \"←\" or right \"→\" turns to the side 90 degrees (BUT IT DOES NOT MAKE IT MOVE)")
print("ENJOY THIS A+ PROJECT(Girdejote Kestai? A++) AND GAME!")

gamers_input = input("")

pirmny = forward(100)
kaire = left(90)
desine = right(90)

if gamers_input == "w":
    forward(20)
elif gamers_input == "a":
    left(90)
elif gamers_input == "d":
    right(90)

