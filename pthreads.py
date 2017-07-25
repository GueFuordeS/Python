#! /usr/bin/python3
# Gabriel Fernandes

from time import sleep
from threading import Thread


def pin(id):
    print('Hello, i\'m the', id)
    sleep(5)
    print('Goodbye, i\'m the', id)


print('EXECUCAO SINCRONA:')
pin(2)
pin(15)

print('='*12)

thread = Thread(target=pin, args=(7,))
thread2 = Thread(target=pin, args=(19,))

print('EXECUCAO ASSINCRONA:')
thread.start()
thread2.start()
