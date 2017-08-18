#/usr/bin/env python3
# A ideia eh n usar nem loop nem recursao
# para calcular o fatorial
# Gabriel Fernandes

num = int(input('Digite um numero: '))
result = 'O fatorial de %d eh' %num

if num > 0:
    total = num

    pedaco = 'num -= 1\ntotal *= num\n'
    pedaco *= (num - 1)

    exec(pedaco)

elif num < 0:
    raise ArithmeticError('Fatorial abaixo de 0!')

else:
    total = 1

print(result, total)
