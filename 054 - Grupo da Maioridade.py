# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
maior = 0
menor = 0
for anos in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {anos}ª pessoa: '))
    if date.today().year - nasc >= 18:
        maior += 1
    else:
        menor += 1
print('-' * 50)
print(f'\nO total de pessoas maiores de idade é {maior}'
      f'\nO total de pessoas maiores de idade é {menor}')
