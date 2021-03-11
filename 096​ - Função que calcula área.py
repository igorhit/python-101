# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.


def area(larg, comp):
    a = larg * comp
    print(f'As dimensões do terreno são:'
          f'\nLargura: {larg}m'
          f'\nComprimento: {comp}m'
          f'\nÁrea: {a}m²')


l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
area(l, c)
