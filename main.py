from tkinter import *
import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
import os
import random

windywindow=tk.Tk()
windywindow.geometry("280x420")
windywindow.resizable(0,0)
windywindow.title("Calculators with a Twist")
access_functions=""
equation=StringVar()
equation.set("0")
entry_numbers=tk.Entry(windywindow,textvariable=equation)

def input_number(number,equation):
    global access_functions
    access_functions=access_functions+str(number)
    equation.set(access_functions)

def symbol_equal():
    try:
        global access_functions
        total=str(eval(access_functions))
        equation.set(total)
        access_functions=""
    except:
        equation.set("Error")
        access_functions=""

def window_to_game():pass

def symbol_clear_c():
    global access_functions
    access_functions=""
    equation.set("0")

def symbol_random():
    windywindow.config(background=random.choice(["black","red","green","blue", "yellow",]))

def symbol_quit():
    quit()

button_number_7=tk.Button(windywindow,width=8,height=4,text="7",command=lambda:input_number(7,equation))
button_number_8=tk.Button(windywindow,width=8,height=4,text="8",command=lambda:input_number(8,equation))
button_number_9=tk.Button(windywindow,width=8,height=4,text="9",command=lambda:input_number(9,equation))
button_divide=tk.Button(windywindow,width=8,height=4,text="/",command=lambda:input_number("/", equation))

button_number_4=tk.Button(windywindow,width=8,height=4,text="4",command=lambda:input_number(4,equation))
button_number_5=tk.Button(windywindow,width=8,height=4,text="5",command=lambda:input_number(5,equation))
button_number_6=tk.Button(windywindow,width=8,height=4,text="6",command=lambda:input_number(6,equation))
button_multiply=tk.Button(windywindow,width=8,height=4,text="*",command=lambda:input_number("*",equation))

button_number_1=tk.Button(windywindow,width=8,height=4,text="1",command=lambda:input_number(1,equation))
button_number_2=tk.Button(windywindow,width=8,height=4,text="2",command=lambda:input_number(2,equation))
button_number_3=tk.Button(windywindow,width=8,height=4,text="3",command=lambda:input_number(3,equation))
button_substract=tk.Button(windywindow,width=8,height=4,text="-",command=lambda:input_number("-",equation))

button_number_0=tk.Button(windywindow,width=8,height=4,text="0",command=lambda:input_number(0,equation))
button_dot=tk.Button(windywindow,width=8,height=4,text=".",command=lambda:input_number(".",equation))
button_equal=tk.Button(windywindow,width=8,height=4,text="=",command=symbol_equal)
button_plus=tk.Button(windywindow,width=8,height=4,text="+",command=lambda:input_number("+",equation))

button_game=tk.Button(windywindow,width=8,height=4,text="Game",command=window_to_game)
button_clear_c=tk.Button(windywindow,text="C",width=8,height=4,command=lambda:symbol_clear_c())
button_random=tk.Button(windywindow,width=8,height=4,text="Backspace",command=symbol_random)
button_quit=tk.Button(windywindow,width=8,height=4,text="Quit",command=symbol_quit)

entry_numbers.grid(columnspan=4,ipadx=50,ipady=10)
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
button_plus.grid(row=4,column=3)

button_game.grid(rows=5,column=0)
button_clear_c.grid(row=5,column=1)
button_random.grid(row=5,column=2)
button_quit.grid(row=5,column=3)

windywindow.mainloop()