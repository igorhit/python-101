# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opc = 0
while opc != 5:
    opc = int(input('Qual operação você gostaria de realizar?'
                    '\n[ 1 ] somar'
                    '\n[ 2 ] multiplicar'
                    '\n[ 3 ] maior e menor'
                    '\n[ 4 ] novos números'
                    '\n[ 5 ] sair do programa'
                    '\nDigite o número de uma das opções: '))
    if opc == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opc == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior é {n1}.')
        else:
            print(f'Entre {n1} e {n2}, o maior é {n2}.')
    elif opc == 4:
        print('Digite novos números')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opc == 5:
        print('Encerrando...')
    else:
        print('Opção inválida! Por favor, tente novamente.')
print('Programa finalizado com sucesso! Volte sempre!')