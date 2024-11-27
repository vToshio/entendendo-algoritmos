# definição de uma constante com os 26 números primos
PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]


def prime_hashing(string: str, size: int) -> int:
    '''
    Função escrita com base no algoritmo D de Hashing proposto na página 113.
    O Hashing recebe uma string com argumento, e realiza o somatório de quaisquer dos 26 primeiros números primos, associados à um caractere do alfabeto.
    Após a obtenção de um valor, o resto desse somatório pelo tamanho da hash table (também passado como parâmetro) é o resultado do identificador da mesma dentro do hash map.
    
    Levanta ValueError ao passar uma string vazia como parâmetro.
    '''
    string = string.strip()
    if not string:
        raise ValueError('A string fornecida não pode ser vazia ou apenas espaços.')
    summ = 0
    for ch in string:
        if 'A'<=ch<='Z':
            summ += PRIME_NUMBERS[ord(ch)-ord('A')]
        elif 'a'<=ch<='z':
            summ += PRIME_NUMBERS[ord(ch)-ord('a')]
        else:
            raise ValueError(f'Caractere {ch} é inválido. A função aceita apenas caracteres alfabéticos.') 
    return summ % size

print(prime_hashing('bag', 10))