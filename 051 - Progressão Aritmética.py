# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# MODIFICAÇÃO MINHA: perguntar quantos primeiros termos o usuário gostaria

prtr = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = (prtr + (10 - 1) * raz) + raz
# qttr = int(input('Quantos termos: '))
# qttrfr = (prtr + (qttr - 1) * raz) + raz FÓRMULA NÃO FUNCIONA

for c in range (prtr, dec, raz):
    print(f'{c}', end=' < ')
print('FIM')
