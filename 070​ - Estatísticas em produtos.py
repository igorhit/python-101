# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

precototal = acima1000 = barato = qt = 0
prodbarato = ' '
while True:
    prod = str(input('Digite um produto: ')).upper().strip()
    preco = float(input('Digite o valor do produto: R$'))
    qt += 1
    precototal += preco
    if qt == 1 or preco < barato:
        barato = preco
        prodbarato = prod
    if preco > 1000:
        acima1000 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar(S/N)? ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'O gasto total da compra é de R${precototal:.2f}.'
      f'\n{acima1000} produtos com valor acima de R$1000.00.'
      f'\n{prodbarato} é o produto mais barato da compra no valor de R${barato:.2f}.')
