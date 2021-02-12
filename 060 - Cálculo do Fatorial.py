# Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
n = int(input('Digite um número para calcular seu FATORIAL: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}')
