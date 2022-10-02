# import turtle
from tkinter import *
# import tkinter as tk
import os
import random
import webbrowser

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

# bet pirma, pazaisiu su situ nauju dalyku kuri perskaiciau :D turtle

#########################################################################################           TURTLE GAME INSTRUCTIONS
# print("Hello dear friends and students!")
# print("Welcome to the hidden game!")
# print("These are the Calculators with a Twist - Game Instructions")
# print("Thing is, I'm not the brightest, so you can only use 3 buttons!!!")
# print("Or use the keyboard ^_^\nArrow up \"↑\" goes STRAIGHT")
# print("Arrows left \"←\" or right \"→\" turns to the side 90 degrees (BUT IT DOES NOT MAKE IT MOVE)")
# print("ENJOY THIS A+ PROJECT(Girdejote Kestuti?!!? A++) GAME!")

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
windywindow=Tk()
windywindow.geometry("280x390")
windywindow.resizable(0,0)
windywindow.title("Calculators with a Twist")
access_functions=""
equation=StringVar()#sita vis trinu ir is naujo parrasau, WHY!?> man gi jo reikes. LEAVE IT ALONE
equation.set("0")
entry_numbers=Entry(windywindow,textvariable=equation)
input_frame=Frame(windywindow,width=100,height=50,bd=3,highlightbackground="grey")

#I SHOULD IMPORT MATH# or not
def input_number(number,equation):
    global access_functions
    access_functions=access_functions+str(number)
    equation.set(access_functions)

# def number_7():pass############################################# these turned out to be useless :O
# def number_8():pass############################################# these turned out to be useless :O
# def number_9():pass############################################# these turned out to be useless :O
# def number_4():pass############################################# these turned out to be useless :O
# def number_5():pass############################################# these turned out to be useless :O
# def number_6():pass############################################# these turned out to be useless :O
# def number_1():pass############################################# these turned out to be useless :O
# def number_2():pass############################################# these turned out to be useless :O
# def number_3():pass############################################# these turned out to be useless :O
# def number_0():pass############################################ these turned out to be useless :O

# def symbol_dot():pass############################################# this turned out to be useless :O

def symbol_equal():#su equal turejau labai daug errors ir kankinausi... Galiausiai pasiklioviau "good old trusted duck duck go search"
    # total = str(eval(access_functions))#su equal turejau labai daug errors ir kankinausi... Galiausiai pasiklioviau "good old trusted duck duck go search"
    # equation.set(total)#su equal turejau labai daug errors ir kankinausi... Galiausiai pasiklioviau "good old trusted duck duck go search"
    try:
        global access_functions
        total=str(eval(access_functions))
        equation.set(total)
        access_functions=""
    except:
        equation.set("Baik lempint")
        access_functions=""

# def symbol_plus():pass############################################# this turned out to be useless :O
# def symbol_substract():pass############################################# this turned out to be useless :O
# def symbol_multiply():pass############################################# this turned out to be useless :O
# def symbol_divide():pass############################################# this turned out to be useless :O

def window_to_game():pass

def symbol_clear_c():#kodel n
    global access_functions
    access_functions=""
    equation.set("0")
    # entry_numbers.delete(0),len(entry_numbers.get())

def symbol_random():
    windywindow.config(background=random.choice(["black","red","green","blue", "yellow","cyan","white","purple","pink","orange","grey"]))
    
    # access_functions = access_functions[:1]
    # current = equation.get():#had to google how to do it as i would NEVER THINK THIS WAY
    # length = len(current)-1
    # equation.delete(length, END)

    # global access_functions
    # access_functions = equation.get()[:-1]
    # if equation =="":
    
    # equation.set("")

    # entry_numbers.delete[::-1],len(entry_numbers.get())#well tthis didnt work at all :D

def symbol_quit():
    quit()

button_number_7=Button(windywindow,width=8,height=4,text="7",command=lambda:input_number(7,equation))
button_number_8=Button(windywindow,width=8,height=4,text="8",command=lambda:input_number(8,equation))
button_number_9=Button(windywindow,width=8,height=4,text="9",command=lambda:input_number(9,equation))
button_divide=Button(windywindow,width=8,height=4,text="/",command=lambda:input_number("/", equation))

button_number_4=Button(windywindow,width=8,height=4,text="4",command=lambda:input_number(4,equation))
button_number_5=Button(windywindow,width=8,height=4,text="5",command=lambda:input_number(5,equation))
button_number_6=Button(windywindow,width=8,height=4,text="6",command=lambda:input_number(6,equation))
button_multiply=Button(windywindow,width=8,height=4,text="*",command=lambda:input_number("*",equation))

button_number_1=Button(windywindow,width=8,height=4,text="1",command=lambda:input_number(1,equation))
button_number_2=Button(windywindow,width=8,height=4,text="2",command=lambda:input_number(2,equation))
button_number_3=Button(windywindow,width=8,height=4,text="3",command=lambda:input_number(3,equation))
button_substract=Button(windywindow,width=8,height=4,text="-",command=lambda:input_number("-",equation))

button_number_0=Button(windywindow,width=8,height=4,text="0",command=lambda:input_number(0,equation))
button_dot=Button(windywindow,width=8,height=4,text=".",command=lambda:input_number(".",equation))
button_equal=Button(windywindow,width=8,height=4,text="=",command=symbol_equal)
button_plus=Button(windywindow,width=8,height=4,text="+",command=lambda:input_number("+",equation))

button_game=Button(windywindow,width=8,height=4,text="Game",command=window_to_game)
# button_clear_c =tk.Button(windywindow,width=8,height=4,text="C",command=symbol_clear_c)
button_clear_c=Button(windywindow,text="C",width=8,height=4,command=lambda:symbol_clear_c())
button_random=Button(windywindow,width=8,height=4,text="Random",command=symbol_random)
button_quit=Button(windywindow,width=8,height=4,text="Quit",command=symbol_quit)

entry_numbers.grid(columnspan=4)
# input_frame.grid(row=0,column=1)
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

#wtf am i high??? nejaugi visus buttons po 1 programuosiu ?
# button_number_1 = tk.Button(windywindow, text="1", command=number_buttons)
# button_number_2 = tk.Button(windywindow, text="2", command=number_buttons)
# button_number_3 = tk.Button(windywindow, text="3", command=number_buttons)
# button_number_4 = tk.Button(windywindow, text="4", command=number_buttons)
# button_number_5 = tk.Button(windywindow, text="5", command=number_buttons)
# button_number_6 = tk.Button(windywindow, text="6", command=number_buttons)
# button_number_7 = tk.Button(windywindow, text="7", command=number_buttons)
# button_number_8 = tk.Button(windywindow, text="8", command=number_buttons)
# button_number_9 = tk.Button(windywindow, text="9", command=number_buttons)
#wtf am i high??? nejaugi visus buttons po 1 programuosiu ?