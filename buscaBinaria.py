#coding:utf-8

######## Busca Binária ########

delimiter = 0
def buscaBinariaIndice(lista, valor):
	global delimiter
	
	if delimiter < len(lista):
		
		if lista[delimiter] == valor:
			return delimiter
			
		else:	
			delimiter += 1
			return buscaBinariaIndice(lista,valor)
			
	else:
		return -1

####### Quicksort ##########

def partition(list, start, end):
    pivot = list[end]                          
    bottom = start-1                           
    top = end                                  

    done = 0
    while not done:                            

        while not done:                       
            bottom = bottom+1                  

            if bottom == top:                  
                done = 1                      
                break

            if list[bottom] > pivot:           
                list[top] = list[bottom]       
                break                         

        while not done:                        
            top = top-1                        
            
            if top == bottom:                 
                done = 1                       
                break

            if list[top] < pivot:             
                list[bottom] = list[top]      
                break                         

    list[top] = pivot
    return top                                 


def quicksort(list, start, end):
    if start < end:                            
        split = partition(list, start, end)    
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
    else:
        return


######## interface com usuário #########
print "Digite os números da lista que deseja usar em sequencia: "
lista = raw_input().split()
inicio = 0
fim = len(lista)-1
quicksort(lista,inicio,fim)
for i in range(len(lista)):
	lista[i] = int(lista[i])
print "Lista ordenada: "
print lista

print "Digite um número que deseja procurar na lista: "
num = int(raw_input())
print buscaBinariaIndice(lista,num)
