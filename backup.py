from time import time
import random

def sort(array):
    #inicia lista auxiliar com indices disponiveis ate
    #o maior elemento existente em nosso array
    gap = findmin(array)
    aux = [0]*(findmax(array)+1-gap)
    
    #computa repeticoes no array
    for e in array:
        aux[e] += 1
    
    #realca a diferenca pro elemento anterior
    for i in range(1, len(aux)):
        aux[i] = aux[i] + aux[i-1]


    i = len(aux)-1    #i vai ser o iterador para o auxiliar
    j = len(array)-1  #j vai ser o iterador para o array original
    while i > 0:
        if aux[i] > aux[i-1]:
                array[j] = i
                aux[i] -= 1
                j -= 1
        else:
            i -= 1

    #primeiro elemento precisa ser adcionado a parte
    #visto q n tem como comparar ele com o antecessor
    for i in range(aux[0]):
        array[j] = 0
        j -= 1
    
    #para propositos de teste retornamos o array,
    #apesar dele ser in place
    return array


def findmax(array):
    maxi = array[0]
    for e in array:
        if e > maxi:
            maxi = e
    
    return maxi

def findmin(array):
    mine = array[0]
    for e in array:
        if e < mine:
            mine = e
    
    return mine

def test():
    assert sort([4,3,2,1]) == [1,2,3,4]
    assert sort([4,2,3,1]) == [1,2,3,4]
    assert sort([4,5,3,2,1]) == [1,2,3,4,5]

    for _ in range(100):
        tmp = list(range(100))
        random.shuffle(tmp)
        assert sort(tmp) == list(range(100))
    
    return 'test pass!'


def benchmark():
    start = time()
    arr = [i for i in range(1000000)]
    arr2 = arr[:]
    random.shuffle(arr)
    assert arr != arr2
    sort(arr)
    assert arr == arr2
    
    print('Taked time: {:.9f} secs'.format(time()-start))
    
    
if __name__=='__main__':
    benchmark()
