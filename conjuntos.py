import sys

"""
Command line program in python, here are implemented some basics operations
at sets

@author Gabriel Fernandes
"""

def uniao(conjA,conjB):
    resp = set([])
    for e in conjA:
        resp.add(e)
    for e in conjB:
        resp.add(e)
    printador(resp)
  
def intersecao(conjA,conjB):
    resp = set([])
    for e in conjA:
        if e in conjB:
            resp.add(e)
    printador(resp)
  
def diferenca(conjA,conjB):
    resp = set([])
    for e in conjA:
        if e not in conjB:
            resp.add(e)
    printador(resp)
  
def complemento(conj,univ):
    resp = set([])
    for e in conj:
        if e not in univ:
            raise ValueError("Universo precisa conter todos os elementos do conjunto")
    for e in univ:
        if e not in conj:
            resp.add(e)
    printador(resp)

def main():
    print "> ===== Operacoes entre conjuntos ====="
    print "> 1. Uniao"
    print "> 2. Intersecao"
    print "> 3. Diferenca"
    print "> 4. Complemento"
    print "> 0. Sair"

    while 1:
        try:
            entrada = int(raw_input("> Insira a operacao que deseja realizar: "))
        except:
            print "Escolha um valor entre 0 e 4 por favor"
            continue
            
        tuplaDePossibilidades = (0,1,2,3,4)
        if entrada not in tuplaDePossibilidades:
            print "Escolha um valor entre 0 e 4 por favor"
        elif entrada == 0:
            sys.exit(0)
        else:
            utilitario(entrada)

def utilitario(n):
    conjA = set([])
    conjB = set([]) 
    if n == 4:
        conj1 = splitao(raw_input("> Insira o conjunto: "))
        conj2 = splitao(raw_input("> Insira o universo: "))
    else:
        conj1 = splitao(raw_input("> Insira o primeiro conjunto: "))
        conj2 = splitao(raw_input("> Insira o segundo conjunto: "))

    for e in conj1:
        conjA.add(e)

    for e in conj2:
        conjB.add(e)

    if n == 1:
        uniao(conjA,conjB)
    elif n == 2:
        intersecao(conjA,conjB)
    elif n == 3:
        diferenca(conjA,conjB)
    elif n == 4:
        try:
            complemento(conjA,conjB)
        except ValueError as e:
            print e

def printador(conj):
    listinha = [None]*len(conj)
    count = 0
    for e in conj:
        listinha[count] = e
        count += 1
    listinha.sort()
    
    finalPrint = "> Resultado: {"
    for i in range(len(listinha)-1):
        finalPrint += str(listinha[i])+", "
    if len(listinha) == 0:
        finalPrint += "}"
    else:
        finalPrint += str(listinha[-1])+"}"
    
    print finalPrint
    
def splitao(string):
    if string == "":
        return []
    novaString = ""
    toRemove = ("(",")","[","]","{","}")
    for i in range(len(string)):
        if string[i] not in toRemove:
            if string[i] == ",":
                novaString += " "
            else:
                novaString += string[i]
    return novaString.split()

if 1 == 1:
    main()
