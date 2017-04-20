#!/usr/bin/python3

'''
Implementacao simples de uma
calculadora

@Author Gabriel Fernandes
'''

from tkinter import *
from functools import partial

def update_screen(button):
    screen_text += button
    screen['text'] = screen_text

def main(args):
    global janela
    janela = Tk()

    ######
    global screen_text
    screen_text = ''
    global screen
    screen = Label(janela, text='0', height=2, font='Helvetica 15 bold')

    #numerics buttos
    num0 = Button(janela, text='0', width=10, height=5)
    num0['command'] = partial(update_screen, '0')
    num1 = Button(janela, text='1', width=10, height=5)
    num1['command'] = partial(update_screen, '1')
    num2 = Button(janela, text='2', width=10, height=5)
    num2['command'] = partial(update_screen, '2')
    num3 = Button(janela, text='3', width=10, height=5)
    num3['command'] = partial(update_screen, '3')
    num4 = Button(janela, text='4', width=10, height=5)
    num4['command'] = partial(update_screen, '4')
    num5 = Button(janela, text='5', width=10, height=5)
    num5['command'] = partial(update_screen, '5')
    num6 = Button(janela, text='6', width=10, height=5)
    num6['command'] = partial(update_screen, '6')
    num7 = Button(janela, text='7', width=10, height=5)
    num7['command'] = partial(update_screen, '7')
    num8 = Button(janela, text='8', width=10, height=5)
    num8['command'] = partial(update_screen, '8')
    num9 = Button(janela, text='9', width=10, height=5)
    num9['command'] = partial(update_screen, '9')

    #operators buttons
    addition = Button(janela, text='+', width=10, height=5)
    subtraction = Button(janela, text='-', width=10, height=5)
    multiplication = Button(janela, text='*', width=10, height=5)
    division = Button(janela, text='/', width=10, height=5)
    equal = Button(janela, text='=', width=10, height=5)
    dot = Button(janela, text='.', width=10, height=5)

    ######

    screen.grid(row=0, column=1, columnspan=4, sticky='e')

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
    addition.grid(row=4, column= 2)
    subtraction.grid(row=4, column=3)
    multiplication.grid(row=2, column= 4)
    division.grid(row=1, column=4)
    equal.grid(row=4, column= 4)
    dot.grid(row=3, column=4)

    ######

    janela.title('Calculator')
    janela.geometry('450x400')
    janela.mainloop()

if __name__=='__main__':
	main(sys.argv)
