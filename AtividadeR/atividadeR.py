from global_utils import obter_numero_inteiro, enter_limpar_tela, limpar_vetor
from atividadeR_features import *

def main():
    opcoes = menu()
    
    numeros = []

    opcao = obter_numero_inteiro(opcoes)

    while opcao != 0:
        if opcao == 1:
            limpar_vetor(numeros)
            numeros = gerar_vetor_valor_padrao()
        elif opcao == 2:
            limpar_vetor(numeros)
            numeros = gerar_vetor_manual()
        elif opcao == 3:
            limpar_vetor(numeros)
            numeros = gerar_vetor_aleatorio_min_max()
        elif opcao == 4:
            print(numeros)
        elif opcao == 5:
            elevar_vetor_a_n(numeros)
        elif opcao == 6:
            contar_valores(numeros)
        elif opcao == 7:
            somar_valores(numeros)
        elif opcao == 8:
            media_e_mediana(numeros)
        elif opcao == 9:
            maior_e_menor(numeros)
        # elif opcao == 10:
        #     sortear_positivo_e_negativo(numeros)
        # elif opcao == 11:
        #     gerar_grupos(numeros)
        # elif opcao == 12:
        #     novo_vetor()  
        # elif opcao == 13:
        #     top_maiores(numeros)
        # elif opcao == 14:
        #     top_menores(numeros)
        # elif opcao == 15:
        #     valor_medio_maiores_menores(numeros)
        # elif opcao == 17:
        #     operacoes_media()
        # elif opcao == 18:
        #     ordenar_crescente(numeros)
        # elif opcao == 19:
        #     ordenar_decrescente(numeros)
        # elif opcao == 20:
        #     eliminar_multiplos(numeros)

        enter_limpar_tela()
        opcao = obter_numero_inteiro(opcoes)

    

def menu():
    menu_options = "***** Arrays Game *****"
    menu_options += "\n-----------------------"
    menu_options += "\n1 - Gerar vetor com N posições e valor padrão"
    menu_options += "\n2 - Preencher manualmente o vetor sugerindo valores"
    menu_options += "\n3 - Preencher vetor aleatoriamente, delimitando um valor mínimo e máximo"
    menu_options += "\n4 - Mostrar vetor"
    menu_options += "\n5 - Elevar vetor a uma potência n"
    menu_options += "\n6 - Contar positivos, negativos e zeros"
    menu_options += "\n7 - Somatório de todos os valores"
    menu_options += "\n8 - Exibir média e mediana"
    menu_options += "\n9 - Exibir maior e menor número"
    menu_options += "\n10 - Sortear num positivo e num negativo"
    menu_options += "\n11 - Gerar N grupos de T tamanhos sem repetir valores"
    menu_options += "\n12 - Pedir um novo vetor e verificar se está 100% presente nos números \
                            do sistema (e na mesma ordem)"
    menu_options += "\n13 - Top N maiores números"
    menu_options += "\n14 - Top N menores números"
    menu_options += "\n15 - Listar valor médio, e listar números maiores que a Média e Menores que a Média"
    menu_options += "\n17 - Somatório da Média dos Números Positivos múltiplos dois COM o Produto \
                            acumulado dos números negativos pares reduzidos à metade"
    menu_options += "\n18 - Ordenar em ordem crescente"
    menu_options += "\n19 - Ordenar em ordem decrescente"
    menu_options += "\n20 - Eliminar múltiplos de N e M (simultaneamente)"
    menu_options += "\n0 - Sair"
    menu_options += "\n\n>> "

    return menu_options

main()
