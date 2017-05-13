from sys import argv

'''
a simple python module with
exclusive the factorial implementetion

@Author Gabriel Fernandes
'''

def factorial(num):
    if(num < 0):
        raise ValueError('must be a natural number')
    
    if(not num <= 1):
        num = num * factorial(num - 1)

    return 1 if num is 0 else num


if(__name__=='__main__'):
    try:
        factorial(int(argv[1]))
        
    except(IndexError, ValueError) as e:
        print(str(type(e))[8:-2], ': Please, insert a natural number after "factorial.py" in command line', sep='')
