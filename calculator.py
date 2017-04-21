#!/usr/bin/python3

'''
a simple calculator with a gui

@Author Gabriel Fernandes
'''

import sys
from tkinter import *
from functools import partial

screen_text = ''

def update_screen(button):
    global screen_text
    screen_text += button
    if(len(screen_text) > 18):
        screen_text = screen_text[1:]
    screen['text'] = screen_text
    
def clean_screen():
    global screen_text
    screen_text = ''
    screen['text'] = '0'

def clean_last():
    global screen_text
    if(len(screen_text) <= 1):
        screen_text = ''
        screen['text'] = '0'
    else:
        screen_text = screen_text[:-1]
        screen['text'] = screen_text

def raise_result():
    global screen_text
    try:
        is_valid()
        screen['text'] = eval(screen_text)
        screen_text = ''
    except Exception:
        screen['text'] = 'Invalid expression'
        screen_text = ''

def is_valid():
    global screen_text
    if(not screen_text[0].isnumeric() and screen_text[0] is not '+' and screen_text[0] is not '-'):
        raise Exception()
    elif(not screen_text[-1].isnumeric()):
        raise Exception()

def main(args):
    global window
    window = Tk()

    ######
    global screen_text
    global screen
    screen = Label(window, text='0', height=2, font='Helvetica 15 bold')

    #numerics buttos
    num0 = Button(window, text='0', width=10, height=5)
    num0['command'] = partial(update_screen, '0')
    num1 = Button(window, text='1', width=10, height=5)
    num1['command'] = partial(update_screen, '1')
    num2 = Button(window, text='2', width=10, height=5)
    num2['command'] = partial(update_screen, '2')
    num3 = Button(window, text='3', width=10, height=5)
    num3['command'] = partial(update_screen, '3')
    num4 = Button(window, text='4', width=10, height=5)
    num4['command'] = partial(update_screen, '4')
    num5 = Button(window, text='5', width=10, height=5)
    num5['command'] = partial(update_screen, '5')
    num6 = Button(window, text='6', width=10, height=5)
    num6['command'] = partial(update_screen, '6')
    num7 = Button(window, text='7', width=10, height=5)
    num7['command'] = partial(update_screen, '7')
    num8 = Button(window, text='8', width=10, height=5)
    num8['command'] = partial(update_screen, '8')
    num9 = Button(window, text='9', width=10, height=5)
    num9['command'] = partial(update_screen, '9')

    #operators buttons
    addition = Button(window, text='+', width=10, height=5)
    addition['command'] = partial(update_screen, '+')
    subtraction = Button(window, text='-', width=10, height=5)
    subtraction['command'] = partial(update_screen, '-')
    multiplication = Button(window, text='*', width=10, height=5)
    multiplication['command'] = partial(update_screen, '*')
    division = Button(window, text='/', width=10, height=5)
    division['command'] = partial(update_screen, '/')
    equal = Button(window, text='=', width=10, height=5, command=raise_result)
    dot = Button(window, text='.', width=10, height=5)
    dot['command'] = partial(update_screen, '.')
    clear = Button(window, text='C', width=10, height=4, command=clean_screen)
    erase = Button(window, text='<==', width=10, height=4, command=clean_last)
    
    ######
    screen.grid(row=0, column=3, columnspan=2, sticky='e')

    #gridding the numbers
    num0.grid(row=4, column=1)
    num1.grid(row=3, column=1)
    num2.grid(row=3, column=2)
    num3.grid(row=3, column=3)
    num4.grid(row=2, column=1)
    num5.grid(row=2, column=2)
    num6.grid(row=2, column=3)
    num7.grid(row=1, column=1)
    num8.grid(row=1, column=2)
    num9.grid(row=1, column=3)

    #gridding the operators
    addition.grid(row=4, column= 4)
    subtraction.grid(row=3, column=4)
    multiplication.grid(row=2, column= 4)
    division.grid(row=1, column=4)
    equal.grid(row=4, column= 3)
    dot.grid(row=4, column=2)
    clear.grid(row=0, column=1)
    erase.grid(row=0, column=2)

    ######

    window.title('Calculator')
    window.geometry('430x405+250+100')
    window.resizable(width=False, height=False)
    window.mainloop()

if __name__=='__main__':
	main(sys.argv)
