#This is a simple basic calculator program to run it you only need to clone this repository.

from tkinter import *


#This function adds in the equation_text
import numpy


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

#avoiding duplication code for painting buttons
def paint_button(num):
    button1 = Button(frame, text=num, height=4, width=9, font=30,
                     command=lambda: button_press(num))
    button1.grid(row=int((num-1)/3), column=((num-1)%3))

def equals():
    global  equation_text
    try:
        total  = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Arithmetic error")
        equation_text = ""
    except SyntaxError:
        equation_text = ""
        equation_label.set("Syntax error")


def clear():
    global equation_text
    equation_text = " "
    equation_label.set(equation_text)


def remove():
    global equation_text
    equation_text = equation_text[:len(equation_text)-1]
    equation_label.set(equation_text)

window  = Tk()

window.title("Calculator Program")

window.geometry("600x500")

equation_text = " "
equation_label = StringVar()

label = Label(window,textvariable = equation_label,font =('consolas',20),bg = 'white',width = 24, height =2)
label.pack()

frame = Frame(window)
frame.pack()


#Cicle for painting buttons
for i in range(1,10):
    paint_button(num=i)


#Painting other buttons
button0 = Button(frame, text=0, height=4, width=9, font=30,
                     command=lambda: button_press(0))
button0.grid(row=3, column=0)
buttonPoint = Button(frame, text='.', height=4, width=9, font=30,
                     command=lambda: button_press('.'))
buttonPoint.grid(row=3, column=1)
buttonEqual = Button(frame, text='=', height=4, width=9, font=30,
                     command=equals)
buttonEqual.grid(row=3, column=2)
buttonPlus = Button(frame, text='+', height=4, width=9, font=30,
                     command=lambda: button_press('+'))
buttonPlus.grid(row=0, column=3)
buttonMinus = Button(frame, text='-', height=4, width=9, font=30,
                     command=lambda: button_press('-'))
buttonMinus.grid(row=1, column=3)
buttonMultiply = Button(frame, text='*', height=4, width=9, font=30,
                     command=lambda: button_press('*'))
buttonMultiply.grid(row=2, column=3)
buttonDivide = Button(frame, text='/', height=4, width=9, font=30,
                     command=lambda: button_press('/'))
buttonDivide.grid(row=3, column=3)

clear = Button(frame, text='clear', height=4, width=9, font=30,
                     command=clear)
clear.grid(row=4,column=0)

remove = Button(frame,text = 'remove', height=4,width=9, font =30,command=remove)
remove.grid(row=4,column=1)
window.mainloop()