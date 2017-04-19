#!/usr/bin/python3

'''
Implementacao simples de relogio

@Author Gabriel Fernandes
'''

import tkinter
from time import strftime

tk = tkinter.Tk()
tk.title('Meu Relogio')
janela = tkinter.Label(tk)
janela['font'] = 'Helvetica 80 bold'
janela['text'] = strftime('%H:%M:%S')

def atualiza_tempo():
	janela['text'] = strftime('%H:%M:%S')
	janela.after(10, atualiza_tempo)

if __name__=='__main__':
	janela.pack()
	atualiza_tempo()
	janela.mainloop()
