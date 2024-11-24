from typing import List

def quicksort(array: List[int], reverse: bool=False) -> None:
    '''
    Função de ordenação que aplica o algoritmo do Quick Sort, com tempo
    de execução O(log n) em uma lista de valores inteiros.
    '''
    if len(array) < 2:
        return array  # Caso base: listas com 0 ou 1 elemento já estão ordenadas.
    else:
        pivot = array[len(array) // 2]

        menores = [item for item in array if item < pivot]
        iguais = [item for item in array if item == pivot]
        maiores = [item for item in array if item > pivot]

        # Caso recursivo, com base no parâmetro Reverse
        if reverse:
            return quicksort(maiores, reverse=True) + iguais + quicksort(menores, reverse=True)
        else:
            return quicksort(menores) + iguais + quicksort(maiores)
        

lista = [2, 4, 1, 16, 9, 27, 12]
print(f"Lista Original: {lista}")

crescente = quicksort(lista)
decrescente = quicksort(lista, reverse=True)
print(f"Lista crescente: {crescente}")
print(f"Lista decrescente: {decrescente}")
