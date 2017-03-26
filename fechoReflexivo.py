#coding: utf-8

"""
Implementacao simples em python de funcao que realiza o fecho reflexivo em uma relacao
Matematica discreta - UFCG - 2016.2

@author Gabriel Fernandes
"""

def fechoReflexivo(conjunto, matriz):
	fecho = [] #note, nos referimos ao reflexivo aqui
	
	for i in conjunto:
		if [i,i] not in matriz:  #uso de facilidades do python aqui, afinal:
			fecho.append([i,i])                             #Don't reinvent the wheel
	'''
	if fecho == []: #nao foi pedido, mas se o retorno eh vazio a relacao ja eh reflexiva
		return "Relacao ja eh reflexiva no conjunto dado"
	'''
	return fecho #retorna apenas os pares iguais a adcionar na relacao para torna-la reflexiva

'''
conjunto = [1,2,3]
matriz =  [[1,2], [1,1], [1,3]]
matriz2 =  [[2,2], [1,1], [3,3]] #print teria como resultado = [] ou seja, relacao ja eh reflexiva
print fechoReflexivo(conjunto, matriz) #print tem como resultado = [[2,2], [3,3]]
'''
