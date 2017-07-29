#!/usr/bin/python3
from time import sleep

def haha():
	n = 0
	while(1):
		print(n, end='', flush=True)
		n += 1
		sleep(0.1)
		print('\b'*len(str(n)), end='')


haha()
