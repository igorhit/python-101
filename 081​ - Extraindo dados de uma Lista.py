# Crie um programa que vai ler vários números e colocar
# em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lst = []
r = ''
while True:
    lst.append(int(input('Digite um número: ')))
    r = str(input('Deseja digitar mais um número? (S/N) ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Foram digitados {len(lst)} números.'
      f'\nEm ordem decrescente são: {sorted(lst, reverse=True)}')
if 5 in lst:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não faz parte da lista.')
