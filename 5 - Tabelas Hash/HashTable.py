from typing import List

class Contato:
    def __init__(self, nome: str, numero: int | str) -> None:
        '''
        Inicializa um novo Contato, que armazena um nome e um número de telefone.
        '''
        self.nome = nome.title()
        self.numero = str(numero)

    def __str__(self) -> str:
        return f'({self.nome} - {self.numero})'

class HashTable:
    def __init__(self) -> None:
        '''
        Instancia uma Hash Table para nomes de contatos, cujas chaves sejam as letras
        do alfabeto, de A-Z (case insentivive)
        '''
        self._contatos = {chr(i+65) : None for i in range(26)}

    def get_lista_nomes(self, inicial: str) -> List[str] | None:
        '''
        Retorna uma lista com os nomes presentes na lista da chave atual.
        '''
        novo = []
        if isinstance(self._contatos[inicial], list):
            for ctt in self._contatos[inicial]:
                novo.append(ctt.nome)
            return novo
        return None

    def adicionar_contato(self, novo: Contato) -> None:
        inicial = novo.nome[0].upper()
        valor_contatos = self._contatos[inicial]

        # Chave sem nenhum contato adicionado
        if valor_contatos is None:
            self._contatos[inicial] = novo  
            print(f'Contato {novo} adicionado como único valor da chave "{inicial}".')
            return

        # Chave já possui uma atribuição
        if isinstance(valor_contatos, Contato):
            if valor_contatos.nome == novo.nome:
                print(f'Contato com o nome "{novo.nome}" já existente na lista de contatos.')
            else:
                self._contatos[inicial] = [valor_contatos, novo]
                print(f'Novo contato {novo} adicionado à lista da chave "{inicial}", que já apresentava 1 contato.')
            return 

        # A chave é uma lista, que contém os contatos com a mesma inicial
        if isinstance(valor_contatos, list):
            nomes = self.get_lista_nomes(inicial)
            if novo.nome in nomes:
                print(f'Contato com o nome "{novo.nome}" já existente na lista, com o index: {nomes.index(novo.nome)}.')
            else:
                valor_contatos.append(novo)
                print(f'Novo contato {novo} adicionado na lista da chave "{inicial}" com 2+ contatos.')
            return

ctt1 = Contato('Pedro de Alcantara', '19 999812568')
ctt2 = Contato('Pedro Dantas', '19 999812568')
ctt3 = Contato('Alice Braganca', '19 999812568')
ctt4 = Contato('alice braganca', '19 999812568')
ctt5 = Contato('William Souza', '19 999812568')
ctt6 = Contato('Pietro Augustini', '19 999812568')

lista_contatos = HashTable()
lista_contatos.adicionar_contato(ctt1)
lista_contatos.adicionar_contato(ctt2)
lista_contatos.adicionar_contato(ctt3)
lista_contatos.adicionar_contato(ctt4)
lista_contatos.adicionar_contato(ctt5)
lista_contatos.adicionar_contato(ctt6)