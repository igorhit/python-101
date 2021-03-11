# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.

from random import randint
lst = []
jogos = []
tot = 1
qt = int(input('Deseja fazer quantos jogos? '))
while tot <= qt:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in lst:
            lst.append(n)
            c += 1
        if c >= 6:
            break
    lst.sort()
    jogos.append(lst[:])
    lst.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
