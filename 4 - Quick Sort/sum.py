from typing import List

def recsum(array: List[int]) -> int:
    '''
    Implementação de uma função que soma todos os itens de uma
    lista de inteiros de forma recursiva.
    '''
    # Caso base: o array não possui nenhum elemento
    if len(array) == 0:
        return 0
    return array[0] + recsum(array[1:]) # Caso recursivo

numbers = [2, 4, 6, 8]
print(recsum(numbers))