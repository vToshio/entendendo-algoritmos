from collections import deque

class Grafo:
    def __init__(self) -> None:
        self._grafo = {}

    def printg(self):
        print('Grafo:')
        for vertice, link in self._grafo.items():
            print(f'{vertice} --> {link}')

    def adicionar_aresta(self, nome1:str, nome2:str, directed:bool=True):        
        # Garantir existência dos vértices
        if nome1 not in self._grafo.keys():
            self._grafo[nome1] = []
        if nome2 not in self._grafo.keys():
            self._grafo[nome2] = []

        # Adicionar as arestas
        self._grafo[nome1].append(nome2)
        if not directed:
            self._grafo[nome2].append(nome1)

    def pesquisa_vendedor(self, ini: str) -> bool:
        def pessoa_eh_vendedor(nome: str) -> bool:
            return nome[-1] == 'm'
        
        fila = deque()
        fila += self._grafo[ini]
        visitados = []

        while fila:
            pessoa = fila.popleft()
            if not pessoa in visitados:
                if pessoa_eh_vendedor(pessoa):
                    print(f'{ini} é um vendedor de manga!')
                    return True
                else:
                    fila += self._grafo[pessoa]
                    visitados.append(pessoa)
        print('Não foi encontrado nenhum vendedor de manga!')
        return False

if __name__ == '__main__':
    g = Grafo()
    g.adicionar_aresta('voce', 'bob')
    g.adicionar_aresta('voce', 'claire')
    g.adicionar_aresta('voce', 'alice')
    g.adicionar_aresta('bob', 'anuj')
    g.adicionar_aresta('bob', 'peggy')
    g.adicionar_aresta('alice', 'peggy')
    g.adicionar_aresta('claire', 'thom')
    g.adicionar_aresta('claire', 'jonny')

    # Imprimir grafo
    g.printg()

    # Pesquisa em Largura
    g.pesquisa_vendedor('voce')