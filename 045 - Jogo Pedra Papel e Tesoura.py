# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
jokenpo = ('PEDRA', 'PAPEL', 'TESOURA')
npc = randint(0, 2)
print('=' * 100)
print('Vamos jogar Jokenpô?!'
      '\nAposto que não consegue me ganhar! hahaha \033[30;107m8\033[31mD\033[m'
      '\n[ 0 ] PEDRA'
      '\n[ 1 ] PAPEL'
      '\n[ 2 ] TESOURA')
print('=' * 100)
pc = int(input('Digite o número correspondente a sua escolha,'
               '\nmas pense bem antes de escolher pra não perder pra mim: '))
print('=' * 100)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!!!')
print('=' * 100)
if pc <= 2:
    print(f'Você escolheu {jokenpo[pc]}!'
           '\nE eu escolhi...')
else:
    print('Tem que digitar 0, 1 ou 2 né burrão!'
          '\nJá que você é café com leite, vou te dar mais uma chance...')
sleep(3)
if pc == 0:
    if npc == 0:
        print(f'{jokenpo[npc]}!')
        print('Empatamos! Vamos jogar de novo para decidir quem é o maior e mais fodão!')
    elif npc == 1:
        print(f'{jokenpo[npc]}!')
        print('AHA! EU sou o maior e mais fodão! Perdeeeeeu \033[30;107mX\033[31mD\033[m')
    elif npc == 2:
        print(f'{jokenpo[npc]}!')
        print('Impossível!!! Você só pode ter roubado! Assim não tem graça...você ganhou \033[30;107m:\033[31m(\033[m')
elif pc == 1:
    if npc == 1:
        print(f'{jokenpo[npc]}!')
        print('Empatamos! Vamos jogar de novo para decidir quem é o maior e mais fodão!')
    elif npc == 2:
        print(f'{jokenpo[npc]}!')
        print('AHA! EU sou o maior e mais fodão! Perdeeeeeu \033[30;107mX\033[31mD\033[m')
    elif npc == 0:
        print('Impossível!!! Você só pode ter roubado! Assim não tem graça...você ganhou \033[30;107m:\033[31m(\033[m')
elif pc == 2:
    if npc == 2:
        print(f'{jokenpo[npc]}!')
        print('Empatamos! Vamos jogar de novo para decidir quem é o maior e mais fodão!')
    elif npc == 0:
        print(f'{jokenpo[npc]}!')
        print('AHA! EU sou o maior e mais fodão! Perdeeeeeu \033[30;107mX\033[31mD\033[m')
    elif npc == 1:
        print(f'{jokenpo[npc]}!')
        print('Impossível!!! Você só pode ter roubado! Assim não tem graça...você ganhou \033[30;107m:\033[31m(\033[m')
print('=' * 100)
print('FIM')
