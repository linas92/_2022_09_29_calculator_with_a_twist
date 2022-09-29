import turtle
import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
import os

# no idea what one to make first.
# i guess ill start with:
# 1. a basic tkinter interface and work a calculator in it with colors and buttons n stuff
# 1.1 tkinter window, buttons, grid, frames, entry
# 1.2 tkinter calculator. working, functioning calculator.
# 1.3 turtle game inside the calculator... ughhh... ONLY do extra
# 2. put a game inside the calculator. Sounds easy :DDDD Omg I went insane thinking about it :DDDDDDDD

# bet pirma, pazaisikite su situ nauju dalyku kuri perskaiciau :D

#########################################################################################           TURTLE GAME INSTRUCTIONS
# print("Hello dear friends and students!")
# print("Welcome to the hidden game!")
# print("These are the Calculators with a Twist - Game Instructions")
# print("Thing is, I'm not the brightest, so you can only use 3 buttons!!!")
# print("Or use the keyboard ^_^\nArrow up \"↑\" goes STRAIGHT")
# print("Arrows left \"←\" or right \"→\" turns to the side 90 degrees (BUT IT DOES NOT MAKE IT MOVE)")
# print("ENJOY THIS A+ PROJECT(Girdejote Kestai? A++) AND GAME!")

# gamers_input = input("")

# pirmny = forward(100)
# kaire = left(90)
# desine = right(90)

# if gamers_input == "w":
#     forward(20)
# elif gamers_input == "a":
#     left(90)
# elif gamers_input == "d":
#     right(90)
#########################################################################################           CODE???
windywindow = tk.Tk()
textytext = StringVar()

windywindow.geometry("340x500")
entry_numbers = tk.Entry()

def number_buttons():
    for number in range(0,10):
        number += 0

def number_plus():
    pass

button_number_0 = tk.Button(windywindow, text=number_buttons, command=number_buttons)
button_symbol_plus = tk.Button(windywindow, text="+", command=number_plus)
#wtf am i high???
# button_number_1 = tk.Button(windywindow, text="1", command=number_buttons)
# button_number_2 = tk.Button(windywindow, text="2", command=number_buttons)
# button_number_3 = tk.Button(windywindow, text="3", command=number_buttons)
# button_number_4 = tk.Button(windywindow, text="4", command=number_buttons)
# button_number_5 = tk.Button(windywindow, text="5", command=number_buttons)
# button_number_6 = tk.Button(windywindow, text="6", command=number_buttons)
# button_number_7 = tk.Button(windywindow, text="7", command=number_buttons)
# button_number_8 = tk.Button(windywindow, text="8", command=number_buttons)
# button_number_9 = tk.Button(windywindow, text="9", command=number_buttons)
#wtf am i high???

windywindow.mainloop()