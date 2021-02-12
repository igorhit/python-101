# Faça um programa que leia um número inteiro e diga se ele é ou
# não um número primo.

num = int(input('Digite um número: '))
vezes = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        vezes += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {vezes} vezes.'
      f'\nOs números em AZUL indicam por quais números o número {num} foi divisível')
if vezes == 2:
    print(f'Portanto, o número {num} É PRIMO.')
else:
    print(f'Portanto, o número {num} NÃO É PRIMO.')
