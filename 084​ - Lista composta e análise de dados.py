# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
lst = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lst) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lst.append(temp[:])
    temp.clear()
    r = str(input('Cadastrar de novo? (S/N) ')).upper().strip()[0]
    if r in 'N':
        break
print(f'{len(lst)} cadastros realizados')
for nome in lst:
    if nome[1] == maior:
        print(f'"{nome[0]}"', end=' ')
print(f'são os mais pesados com {maior}Kg.')
for nome in lst:
    if nome[1] == menor:
        print(f'"{nome[0]}"', end=' ')
print(f'são os mais leves com {menor}Kg.')
