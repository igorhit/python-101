# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os
# valores pares e ímpares em ordem crescente.

lst = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        lst[0].append(num)
    else:
        lst[1].append(num)
print(f'Números digitados: {lst}.'
      f'\nNúmeros pares: {sorted(lst[0])}.'
      f'\nNúmeros pares: {sorted(lst[1])}.')
