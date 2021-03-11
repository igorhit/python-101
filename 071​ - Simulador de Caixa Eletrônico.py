# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('Quanto deseja sacar? R$'))
ced = 50
totced = 0
while True:
    if saque >= ced:
        saque -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saque == 0:
            break
