# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro para ser convertido: '))
base = int(input('Escolha uma base para a conversão:'
                 '\n[ 1 ] para conversão em BINÁRIO'
                 '\n[ 2 ] para conversão em OCTAL'
                 '\n[ 3 ] para conversão em HEXADECIMAL'
                 '\nDigite o número correspondente a sua opção: '))
if base == 1:
    print(f'O número {num} convertido para BINÁRIO é = {bin(num)}')
elif base == 2:
    print(f'O número {num} convertido para OCTAL é = {oct(num)}')
elif base == 3:
    print(f'O número {num} convertido para HEXADECIMAL é = {hex(num)}')
else:
    print('Opção inválida! Tente novamente.')
