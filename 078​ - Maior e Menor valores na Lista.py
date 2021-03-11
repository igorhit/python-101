# Faça um programa que leia 5 valores numéricos e guarde-os em
# uma lista. No final, mostre qual foi o maior e o menor valor
# digitado e as suas respectivas posições na lista.

lst = []
maior = menor = 0
for c in range(0, 5):
    lst.append(int(input('Digite um número: ')))
print(f'Os números digitados foram {lst[0]}, {lst[1]}, {lst[2]}, {lst[3]} e {lst[4]}.'
      f'\nO maior número é {max(lst)}. Na posição ', end='')
for i, v in enumerate(lst):
    if v == max(lst):
        print(f'{i}... ', end='')
print()
print(f'O menor número é {min(lst)}. Na posição ', end='')
for i, v in enumerate(lst):
    if v == min(lst):
        print(f'{i}... ', end='')
