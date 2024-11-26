votos = {}

if __name__ == '__main__':
    while True:
        nome = str(input('Insira o nome do eleitor: '))
        if nome == 'parar':
            print('\nLista de Eleitores:')
            for nome in votos.keys():
                print(nome)
            print('\nEncerrando o programa.')
            break

        if nome in votos.keys():
            print(f'{nome} já votou. Próximo!')
            continue

        votos[nome] = True
        print('Deixe votar!')