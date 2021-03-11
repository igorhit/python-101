# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior18 = m = f20menos = 0
while True:
    idade = int(input('Idade: '))
    sex = str(input('Sexo: ')).upper().strip()[0]
    while sex not in 'MF':
        sex = str(input('Sexo: ')).upper().strip()[0]
    if idade > 18:
        maior18 += 1
    elif sex == 'M':
        m += 1
    elif sex == 'F' and idade < 20:
        f20menos += 1
    cont = str(input('Deseja realizar mais um cadastro? ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja realizar mais um cadastro? ')).upper().strip()[0]
    if cont == 'N':
        break
print('-' * 50,
      f'\n{maior18} com mais de 18 anos.'
      f'\n{m} sexo masculino.'
      f'\n{f20menos} sexo feminino com menos de 20 anos.')
