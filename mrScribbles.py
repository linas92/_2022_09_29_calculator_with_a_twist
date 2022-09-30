import turtle
import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
import os
# CIA YRA BAISUS JUODRASTIS KAD MATYCIAU KAIP MANO LOGINIS MASTYMAS IR SMEGENYS DIRBA. KUR REIKIA PADIRBETI IR T.T

# no idea what one to make first.
# i guess ill start with:
# 1. a basic tkinter interface and work a calculator in it with colors and buttons n stuff
# 1.1 tkinter window, buttons, grid, frames, entry
# 1.2 tkinter calculator. working, functioning calculator.
# 1.3 turtle game inside the calculator... ughhh... ONLY do extra
# 2. put a game inside the calculator. Sounds easy :DDDD Omg I went insane thinking about it :DDDDDDDD
# 3. jeigu turesiu laiko, sukurti dar 1 window. kad butu login -> calculator -> game. Log ijn butu pagal varda ir password. Kad tipo reikia prisijungti. 
# 3.1 gal net iseitu ideti countdown (tipo kaip authentication)

# bet pirma, pazaisiu su situ nauju dalyku kuri perskaiciau :D

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
############################################################################         CODE FOR FUTURE GAME THAT MIGHT NOT BE FINISHED ????? WHY ???

    # def number_buttons():
    #     for number in range(0,10):
    #         number += 0

    # def press():pass
windywindow = tk.Tk()
windywindow.geometry("320x400")
windywindow.resizable(0,0)
windywindow.title("Calculators with a Twist")

def number_plus():pass
def number_substract():pass
def number_multiply():pass
def number_divide():pass
def number_7():pass
def number_8():pass
def number_9():pass
def number_4():pass
def number_5():pass
def number_6():pass
def number_1():pass
def number_2():pass
def number_3():pass
def number_0():pass

# entry_numbers = tk.Entry(windywindow)
# button_number_0 = tk.Button(windywindow, text=number_buttons, command=number_buttons)
# button_symbol_plus = tk.Button(windywindow, text="+", command=number_plus)

button_number_7 = tk.Button(windywindow, text="7", command=number_7)
button_number_8 = tk.Button(windywindow, text="8", command=number_8)
button_number_9 = tk.Button(windywindow, text="9", command=number_9)
button_number_4 = tk.Button(windywindow, text="4", command=number_4)
button_number_5 = tk.Button(windywindow, text="5", command=number_5)
button_number_6 = tk.Button(windywindow, text="6", command=number_6)
button_number_1 = tk.Button(windywindow, text="1", command=number_1)
button_number_2 = tk.Button(windywindow, text="2", command=number_2)
button_number_3 = tk.Button(windywindow, text="3", command=number_3)
button_number_0 = tk.Button(windywindow, text="0", command=number_0)

button_number_7.grid(row=2,column=0)
button_number_8.grid(row=2,column=1)
button_number_9.grid(row=2,column=2)
button_number_4.grid(row=3,column=0)
button_number_5.grid(row=3,column=1)
button_number_6.grid(row=3,column=2)
button_number_1.grid(row=4,column=0)
button_number_2.grid(row=4,column=1)
button_number_3.grid(row=4,column=2)
windywindow.mainloop()

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