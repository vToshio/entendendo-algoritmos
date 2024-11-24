def menor_lado(x: int, y: int) -> float:
    '''
    Encontrar o tamanho do lado do menor quadrado que subdivide igualmente
    uma área de x metros de largura por y metros de altura.
    '''
    if (y>x):
        x, y = y, x

    # Caso base: encontra uma area retangular que pode
    # ser dividida exatamente ao meio 
    if (x%y==0):
        return x/2
    else:
        # Caso recursivo: subdivide a area ate encontrar o menor lado
        lado = menor_lado(y, x-y) 
    return lado

lado = round(menor_lado(1680, 640))
print(f'Menor quadrado (1680x640): {lado}x{lado}')    