# Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.

ext = 'zero', 'um', 'dois', 'três', 'quatro',\
      'cinco', 'seis', 'sete', 'oito', 'nove',\
      'dez', 'onze', 'doze', 'treze', 'quatorze',\
      'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Qual número, entre 0 e 20, quer escrito por extenso? '))
    if 0 > num > 20:
        print('Número inválido.')
    else:
        print(f'O número escolhido foi "{ext[num]}"')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja escolher outro número (S/N)? ')).upper().strip()[0]
    if cont == 'N':
        break
