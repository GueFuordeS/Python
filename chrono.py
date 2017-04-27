#!usr/bin/python3

from sys import argv
from time import time, sleep


def chrono(secs):
	start = time()
	count = 0
	while True:
		if(time()-start > secs):
			break
		count += 1
		sleep(1)
		print('%6d seconds paste' %(count))

if __name__=='__main__':
	try:
		chrono(float(argv[1]))
	except Exception:
		print('NaN: not a number as a argument')
