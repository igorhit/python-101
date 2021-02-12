# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
npc = randint(1, 5)
print('=' * 90)
print('Vou escolher um número entre 1 e 5. \nAdivinhe, se puder...')
pc = int(input('Então, que número eu escolhi? '))
print('Vamos ver se você é bom mesmo...')
sleep(3)
if pc == npc:
    print('Parabéns! Você acertou! Suas habilidades psíquicas de adivinhação são incríveis! \nOu você só deu sorte...')
else:
    print('Que pena! O número que eu escolhi era o {}'
          '\nTente novamente com mais vontade.'.format(npc))
print('=' * 90)