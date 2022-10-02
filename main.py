from tkinter import *
import os
import random
import webbrowser    

windywindow = Tk()
windywindow.geometry("280x390")
windywindow.resizable(0, 0)
windywindow.title("Calculators with a Twist")
access_functions = ""
equation = StringVar()
equation.set("0")
entry_numbers = Entry(windywindow, textvariable=equation)
input_frame = Frame(windywindow, width=100, height=50, bd=3, highlightbackground="black")

def input_number(number, equation):
    global access_functions
    access_functions = access_functions + str(number)
    equation.set(access_functions)

def symbol_equal():
    try:
        global access_functions
        total = str(eval(access_functions))
        equation.set(total)
        access_functions = ""
    except:
        equation.set("Baik lempint")
        access_functions = ""

def window_to_game():
    webbrowser.open_new_tab(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def symbol_clear_c():
    global access_functions
    access_functions = ""
    equation.set("0")

def symbol_random():
    windywindow.config(background = random.choice(["black", "red", "green", "blue", "yellow", "cyan", "white", "purple", "pink", "orange", "grey"]))

def symbol_quit():
    quit()

button_number_7 = Button(windywindow, width=8, height=4, text="7", command=lambda:input_number(7, equation))
button_number_8 = Button(windywindow, width=8, height=4, text="8", command=lambda:input_number(8, equation))
button_number_9 = Button(windywindow, width=8, height=4, text="9", command=lambda:input_number(9, equation))
button_divide = Button(windywindow, width=8, height=4, text="/", command=lambda:input_number("/", equation))

button_number_4 = Button(windywindow, width=8, height=4, text="4", command=lambda:input_number(4, equation))
button_number_5 = Button(windywindow, width=8, height=4, text="5", command=lambda:input_number(5, equation))
button_number_6 = Button(windywindow, width=8, height=4, text="6", command=lambda:input_number(6, equation))
button_multiply = Button(windywindow, width=8, height=4, text="*", command=lambda:input_number("*", equation))

button_number_1 = Button(windywindow, width=8, height=4, text="1", command=lambda:input_number(1, equation))
button_number_2 = Button(windywindow, width=8, height=4, text="2", command=lambda:input_number(2, equation))
button_number_3 = Button(windywindow, width=8, height=4, text="3", command=lambda:input_number(3, equation))
button_substract = Button(windywindow, width=8, height=4, text="-", command=lambda:input_number("-", equation))

button_number_0 = Button(windywindow, width=8, height=4, text="0", command=lambda:input_number(0, equation))
button_dot = Button(windywindow, width=8, height=4, text =".", command=lambda:input_number(".", equation))
button_equal = Button(windywindow, width=8, height=4, text="=", command=symbol_equal)
button_plus = Button(windywindow, width=8, height=4, text="+", command=lambda:input_number("+", equation))

window_to_game_button = Button(windywindow, width=8, height=4, text="Game", command=window_to_game)
button_clear_c = Button(windywindow, text="C", width=8, height=4, command=lambda:symbol_clear_c())
button_random = Button(windywindow, width=8, height=4, text="Random", command=symbol_random)
button_quit = Button(windywindow, width=8, height=4, text="Quit", command=symbol_quit)

entry_numbers.grid(columnspan=4)
button_number_7.grid(row=1, column=0)
button_number_8.grid(row=1, column=1)
button_number_9.grid(row=1 ,column=2)
button_divide.grid(row=1, column=3)

button_number_4.grid(row=2, column=0)
button_number_5.grid(row=2, column=1)
button_number_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_number_1.grid(row=3, column=0)
button_number_2.grid(row=3, column=1)
button_number_3.grid(row=3, column=2)
button_substract.grid(row=3, column=3)

button_number_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

window_to_game_button.grid(rows=5, column=0)
button_clear_c.grid(row=5, column=1)
button_random.grid(row=5, column=2)
button_quit.grid(row=5, column=3)

windywindow.mainloop()