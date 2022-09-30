import turtle
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

windywindow = tk.Tk()
textytext = StringVar()

windywindow.geometry("320x400")
windywindow.resizable(0,0)
windywindow.title("Calculators with a Twist")
entry_numbers = tk.Entry()

def number_buttons():
    for number in range(0,10):
        number += 0

def number_plus():
    pass
def number_substract():
    pass
def number_multiply():
    pass
def number_divide():
    pass

button_number_0 = tk.Button(windywindow, text=number_buttons, command=number_buttons)
button_symbol_plus = tk.Button(windywindow, text="+", command=number_plus)

windywindow.mainloop()