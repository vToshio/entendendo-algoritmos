from typing import List

def select_sort(array: List[int], reverse: bool=False) -> None:
    '''
    Funcao que aplica a ordenacao de uma lista de inteiros de acordo
    com o algoritmo de Selection Sort, com tempo de execucao O(n^2).
    '''
    tam = len(array)
    if not reverse:
        for i in range(tam-1):
            index_menor = i
            for j in range(i+1, tam):
                if array[j]<array[index_menor]:
                    index_menor = j
            array[i], array[index_menor] = array[index_menor], array[i]
    else:
        for i in range(tam-1):
            index_maior = i
            for j in range(i+1, tam):
                if array[j]>array[index_maior]:
                    index_maior = j
            array[i], array[index_maior] = array[index_maior], array[i]

lista = [2, 4, 1, 16, 9, 27, 12]
print(f"Lista Original: {lista}")
select_sort(lista)
print(f"Lista após ordenação: {lista}")