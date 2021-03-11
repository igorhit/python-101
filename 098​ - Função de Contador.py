# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa
# tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def contador(i, f, p):
    print('-' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        print('Impossível contar de 0 em 0. Alterando passo para 1.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print()
    print('-' * 30)


print('-' * 30)
print('a) de 1 até 10, de 1 em 1')
contador(1, 10, 1)
print('b) de 10 até 0, de 2 em 2')
contador(10, 0, 2)
print('Personalize sua contagem!')
i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
print('c) uma contagem personalizada')
contador(i, f, p)
print('PROGRAMA ENCERRADO')


