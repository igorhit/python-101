# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
print('Digite seis números inteiros.')
for c in range(1, 7):
    num = int(input(f'{c}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Os {cont} números somados, ignorando os números ímpares é igual a {soma}')
