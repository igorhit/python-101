# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

from random import randint
npc = randint(0, 10)
print('Nos encontramos novamente!'
      '\nDessa vez vou te dar uma ajudinha pra acertar em qual número,'
      '\nentre 0 e 10, eu escolhi.'
      '\nVamos lá?!')
ok = False
tent = 0
while not ok:
    pc = int(input('Qual número você acha que é? '))
    tent += 1
    if pc == npc:
        ok = True
    else:
        if pc < npc:
            print('É mais...Tenta de novo.')
        else:
            print('É menos...Tenta de novo.')
if tent == 1:
    print('Acertou de primeira! Suas capacidades psíquicas de adivinhação são incríveis!')
else:
    print(f'Acertou! Precisou só de {tent} tentativas pra conseguir.')
