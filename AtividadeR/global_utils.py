def obter_numero_inteiro(label="Digite um número: "):
    numero = input(label)

    while not numero.isnumeric() or numero == "":
        print('Valor inválido!')
        numero = input(label)

    return int(numero)

def enter_limpar_tela():
    input("<Pressione Enter>...")
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_ao_vetor(vetor, elemento):
    novo_vetor = vetor + [elemento]
    return novo_vetor

def limpar_vetor(vetor):
    vetor = []

    return vetor

def gerar_valor_aleatorio(min, max):
    import random
    valor = random.randint(min, max)

    return valor

def mostrar_texto(texto):
    print(texto)
