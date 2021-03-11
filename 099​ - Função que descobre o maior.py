# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer
# qual deles é o maior.

from time import sleep


def maior(*n):
    print('Você digitou os números:')
    for c in num:
        print(f'{c}...', end=' '), sleep(.5)
    print()
    print(f'Em ordem crescente: {sorted(num)}')
    print(f'O maior número entre eles é o {max(num)}')


num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Continuar? (S/N) ')).strip().upper()[0]
    while r not in 'SN':
        print('ERRO! Digite S ou N: ')
        r = str(input('Continuar? (S/N) ')).strip().upper()[0]
    if r in 'N':
        break
maior(num)
