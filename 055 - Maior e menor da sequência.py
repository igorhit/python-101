# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa(em Kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior:.1f}Kg.'
      f'\nO menor peso foi {menor:.1f}Kg.')
