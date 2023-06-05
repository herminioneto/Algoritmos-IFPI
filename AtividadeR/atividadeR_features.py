from global_utils import adicionar_ao_vetor, gerar_valor_aleatorio

def gerar_vetor_valor_padrao():
    N = int(input('Digite a quantidade de posições do vetor: '))
    valor_padrao = int(input('Digite o valor padrão: '))

    vetor = []

    for _ in range(N):
        vetor = adicionar_ao_vetor(vetor, valor_padrao)

    return vetor

def gerar_vetor_manual():
    N = int(input('Digite a quantidade de posições do vetor: '))

    vetor = []

    for i in range(N):
        valor = int(input(f'Digite um valor para a posição {i}: '))
        vetor = adicionar_ao_vetor(vetor, valor)

    return vetor

def gerar_vetor_aleatorio_min_max():
    N = int(input('Digite a quantidade de posições do vetor: '))
    min = int(input('Digite um valor mínimo: '))
    max = int(input('Digite um valor máximo: '))

    vetor = []

    for _ in range(N):
        valor_aleatorio = gerar_valor_aleatorio(min, max)
        vetor = adicionar_ao_vetor(vetor, valor_aleatorio)

    return vetor

def elevar_vetor_a_n(vetor):
    if len(vetor) == 0:
        print('Defina o vetor utilizando umas das 3 primeiras opções para continuar!')
    else:
        n = int(input('Digite o valor ao qual você quer elevar os elementos da lista: '))
        novo_vetor = []

        for valor in vetor:
            valor_elevado = valor**n
            novo_vetor = adicionar_ao_vetor(novo_vetor, valor_elevado)

        print(novo_vetor)

def contar_valores(vetor):
    if len(vetor) == 0:
        print('Defina o vetor utilizando umas das 3 primeiras opções para continuar!')
    else:
        contador_positivos = 0
        contador_negativos = 0
        contador_zeros = 0

        for valor in vetor:
            if valor > 0:
                contador_positivos += 1
            elif valor < 0:
                contador_negativos += 1
            elif valor == 0:
                contador_zeros += 1

        print(f'Positivos: {contador_positivos}')
        print(f'Negativos: {contador_negativos}')
        print(f'Zeros: {contador_zeros}')

def somar_valores(vetor):
    if len(vetor) == 0:
        print('Defina o vetor utilizando umas das 3 primeiras opções para continuar!')
    else:
        somatorio = 0

        for valor in vetor:
            somatorio += valor

        print(f'Somatório = {somatorio}')

def media_e_mediana(vetor):
    if len(vetor) == 0:
        print('Defina o vetor utilizando umas das 3 primeiras opções para continuar!')
    else:
        somatorio = 0

        for valor in vetor:
            somatorio += valor
        
        media = somatorio / 2

        print(f'Média = {media}')

def maior_e_menor(vetor):
    if len(vetor) == 0:
        print('Defina o vetor utilizando umas das 3 primeiras opções para continuar!')
    else:
        maior_valor = float('-inf')
        menor_valor = float('inf')

        for valor in vetor:
            if valor > maior_valor:
                maior_valor = valor
            if valor < menor_valor:
                menor_valor = valor

        print(maior_valor)
        print(menor_valor)
