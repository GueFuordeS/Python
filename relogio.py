#!/usr/bin/python3

'''
Implementacao simples de relogio

@Author Gabriel Fernandes
'''

import sys
import tkinter
from time import strftime

def main(args):
	tk = tkinter.Tk()
	tk.title('Meu Relogio')
	global janela
	janela = tkinter.Label(tk)
	janela['font'] = 'Helvetica 80 bold'
	janela['text'] = strftime('%H:%M:%S')

	janela.pack(expand=True)
	atualiza_tempo()
	tk.geometry('450x150+400+200')
	janela.mainloop()

def atualiza_tempo():
	janela['text'] = strftime('%H:%M:%S')
	janela.after(10, atualiza_tempo)

if __name__=='__main__':
	main(sys.argv)
