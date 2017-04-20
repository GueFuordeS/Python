#!/usr/bin/python3

'''
a simple clock with a gui

@Author Gabriel Fernandes
'''

import sys
import tkinter
from time import strftime

def main(args):
	tk = tkinter.Tk()
	tk.title('Clock')
	global window
	window = tkinter.Label(tk)
	window['font'] = 'Helvetica 80 bold'
	window['text'] = strftime('%H:%M:%S')

	window.pack(expand=True)
	update_time()
	tk.geometry('450x150+400+200')
	window.mainloop()

def update_time():
	window['text'] = strftime('%H:%M:%S')
	window.after(10, update_time)

if __name__=='__main__':
	main(sys.argv)
