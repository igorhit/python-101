# Desenvolva um programa que leia o nome, idade e sexo de
# 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somidade = 0
midade = 0
idadehvelho = 0
nomehvelho = ''
totm20 = 0
qtpess = int(input('Digite o número de pessoas que gostaria de analisar: '))
# for p in range(1, 5):
for p in range(1, qtpess + 1):
    print(f'{p}ª PESSOA')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somidade += idade
    if p == 1 and sexo in 'Mm':
        idadehvelho = idade
        nomehvelho = nome
    if sexo in 'Mm' and idade > idadehvelho:
        idadehvelho = idade
        nomehvelho = nome
    if sexo in 'Ff' and idade < 20:
        totm20 += 1
midade = somidade / qtpess
#print(f'A média de idade das 4 pessoas é de {midade} anos')
print(f'A média de idade das {qtpess} pessoas é de {midade} anos')
print(f'O nome do homem mais velho é {nomehvelho}. Ele tem {idadehvelho} anos.')
print(f'O total de mulheres com menos de 20 anos é de {totm20}.')
