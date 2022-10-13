def imprime_maior_elemento(lista):
    print('Maior elemento: {}'.format(max(lista)))

def imprime_menor_elemento(lista):
    print('Menor elemento: {}'.format(min(lista)))

def imprime_numeros_pares(lista):
    for item in lista:
        if item % 2 == 0:
            print(item)

def imprime_ocorrencias_primeiro_elemento(lista):        
    cont = 0

    for item in lista:
        if item == lista[0]:
            cont += 1

    print('A quantidade de ocorrencias do elemento {} é {}.'.format(lista[0], cont))

def imprime_media(lista):    
    soma = 0
    elementos = len(lista)

    for item in lista:
        soma += item        

    print('A média dos {} elementos da lista é {}.'.format(elementos, soma / elementos))

def imprime_soma_negativos(lista):    
    soma = 0    

    for item in lista:
        if item < 0:
            soma += item        

    print('A soma dos elementos negativos é {}.'.format(soma))

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

imprime_maior_elemento(lista)
imprime_menor_elemento(lista)
imprime_numeros_pares(lista)
imprime_ocorrencias_primeiro_elemento(lista)
imprime_media(lista)
imprime_soma_negativos(lista)