import turtle
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

windywindow = tk.Tk()
windywindow.geometry("320x400")
windywindow.resizable(0,0)
windywindow.title("Calculators with a Twist")

def number_7():pass
def number_8():pass
def number_9():pass
def symbol_divide():pass

def number_4():pass
def number_5():pass
def number_6():pass
def symbol_multiply():pass

def number_1():pass
def number_2():pass
def number_3():pass
def symbol_substract():pass

def number_0():pass
def symbol_dot():pass
def symbol_equal():pass
def symbol_plus():pass

def window_to_game():pass
def symbol_clear_c():
    entry_numbers.delete(0,len(entry_numbers.get()))
def symbol_backspace():
    entry_numbers.delete(0),len(entry_numbers.get())
def symbol_quit():
    quit()

entry_numbers = tk.Entry(windywindow)

button_number_7 = tk.Button(windywindow,width=8,height=4,text="7",command=number_7)
button_number_8 = tk.Button(windywindow,width=8,height=4,text="8",command=number_8)
button_number_9 = tk.Button(windywindow,width=8,height=4,text="9",command=number_9)
button_divide = tk.Button(windywindow,width=8,height=4,text="÷",command=symbol_divide)

button_number_4 = tk.Button(windywindow,width=8,height=4,text="4",command=number_4)
button_number_5 = tk.Button(windywindow,width=8,height=4,text="5",command=number_5)
button_number_6 = tk.Button(windywindow,width=8,height=4,text="6",command=number_6)
button_multiply = tk.Button(windywindow,width=8,height=4,text="*",command=symbol_multiply)

button_number_1 = tk.Button(windywindow,width=8,height=4,text="1",command=number_1)
button_number_2 = tk.Button(windywindow,width=8,height=4,text="2",command=number_2)
button_number_3 = tk.Button(windywindow,width=8,height=4,text="3",command=number_3)
button_substract = tk.Button(windywindow,width=8,height=4,text="-",command=symbol_substract)

button_number_0 = tk.Button(windywindow,width=8,height=4,text="0",command=number_0)
button_dot = tk.Button(windywindow,width=8,height=4,text=".",command=symbol_dot)
button_equal = tk.Button(windywindow,width=8,height=4,text="=",command=symbol_equal)
button_add = tk.Button(windywindow,width=8,height=4,text="+",command=symbol_plus)

button_game = tk.Button(windywindow,width=8,height=4,text="Game",command=window_to_game)
button_clear_c =tk.Button(windywindow,width=8,height=4,text="C",command=symbol_clear_c)
button_backspace = tk.Button(windywindow,width=8,height=4,text="Backspace",command=symbol_backspace)
button_quit = tk.Button(windywindow,width=8,height=4,text="Quit",command=symbol_quit)

entry_numbers.grid(row=0,columnspan=3)

button_number_7.grid(row=1,column=0)
button_number_8.grid(row=1,column=1)
button_number_9.grid(row=1,column=2)
button_divide.grid(row=1,column=3)

button_number_4.grid(row=2,column=0)
button_number_5.grid(row=2,column=1)
button_number_6.grid(row=2,column=2)
button_multiply.grid(row=2,column=3)

button_number_1.grid(row=3,column=0)
button_number_2.grid(row=3,column=1)
button_number_3.grid(row=3,column=2)
button_substract.grid(row=3,column=3)

button_number_0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_add.grid(row=4,column=3)

button_game.grid(rows=5,column=0)
button_clear_c.grid(row=5,column=1)
button_backspace.grid(row=5,column=2)
button_quit.grid(row=5,column=3)

windywindow.mainloop()