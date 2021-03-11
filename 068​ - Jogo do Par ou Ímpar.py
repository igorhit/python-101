# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
from random import randint
win = 0
tot = 0
while True:
    pc = str(input('PAR ou ÍMPAR? ')).upper().strip()[0]
    while pc not in 'PI':
        pc = str(input('PAR ou ÍMPAR? ')).upper().strip()[0]
    sleep(.5)
    print('Do...')
    sleep(1)
    print('Lá...')
    sleep(1)
    print('Ci...')
    sleep(1)
    print('JÁ!')
    numpc = int(input('Escolha seu número: '))
    numnpc = randint(0, 10)
    tot = numpc + numnpc
    if pc in 'P' and tot % 2 == 0:
        print(f'{numnpc}! deu {tot}!'
              f'\nPARABÉNS! Você me venceu! Vamos de novo!')
        win += 1
    elif pc in 'I' and tot % 2 > 0:
        print(f'{numnpc}! deu {tot}!'
              f'\nPARABÉNS! Você me venceu! Vamos de novo!')
        win += 1
    else:
        print(f'{numnpc}! deu {tot}!'
              f'\nGAME OVER! Você venceu {win} vezes.'
              f'\nInsira outra ficha.')
        break
