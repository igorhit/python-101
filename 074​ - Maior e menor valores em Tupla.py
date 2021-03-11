# Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
num = randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)
print(f'Os números sorteados foram: {sorted(num)}'
      f'\nO menor número foi {min(num)}'
      f'\nO maior número foi {max(num)}')
