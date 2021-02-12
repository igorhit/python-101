# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

n = cont = tot = 0
n = int(input('Digite um número: '))
while n != 999:
    cont += 1
    tot += n
    n = int(input('Digite um número: '))
print(f'{cont} números foram digitados.'
      f'\nO total da soma entre eles é {tot}')
