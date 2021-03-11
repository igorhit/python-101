# Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário
# em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for j in range(1, 5):
    jogadores[f'{j}ºjogador'] = randint(1, 20)
for k, v in jogadores.items():
    print(f'{k} rolou: {v}')
    sleep(1)
sleep(2)
print()
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(rank):
    print(f'{k+1}º lugar: {v[0]} com {v[1]} no dado')
