from typing import List

def pesquisa_simples(array: List[int], target: int) -> int | None:
    '''
    Implementação do algoritmo de Pesquisa Simples, com tempo de
    execução O(n).
    '''
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None


def pesquisa_binaria(array: List[int], target:int) -> int | None:
    '''
    Implementação do algoritmo de Pesquisa Binária, com o tempo de
    execução O(log n).
    Para que o algoritmo de Pesquisa Binária funcione efetivamente, é necessário
    que a lista passad como parâmetro esteja ORDENADA.
    '''
    ini = 0
    fim = len(array)-1
    while (ini<=fim):
        meio = (ini + fim) // 2
        if (array[meio] == target):
            return meio
        elif (array[meio] < target):
            ini = meio + 1
        else:
            fim = meio - 1
    return None


lista = [1, 2, 4, 9, 12, 16, 27]
print(f'Index do elemento 27 (pesquisa simples): {pesquisa_simples(lista, 27)}')
print(f'Index do elemento 27 (pesquisa binária): {pesquisa_binaria(lista, 27)}')
