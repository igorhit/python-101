# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro = {}
lstcadastro = []
somaidade = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip()
    while True:
        cadastro['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO!!! Digite somente (M/F)')
    cadastro['idade'] = int(input('Idade: '))
    somaidade += cadastro['idade']
    lstcadastro.append(cadastro.copy())
    cadastro.clear()
    while True:
        r = str(input('Continuar? (S/N) ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO!!! Digite somente (S/N)')
    if r == 'N':
        break
medidade = somaidade / len(lstcadastro)
print(f'Total de {len(lstcadastro)} cadastros realizados'
      f'\nA média de idade de todos os cadastros é {medidade:.2f} anos.')
print('Cadastros femininos: ', end='')
for f in lstcadastro:
    if f['sexo'] in 'F':
        print(f'({f["nome"]})', end=' ')
print()
print('Cadastros acima da média de idade: ', end='')
for v in lstcadastro:
    if v['idade'] > medidade:
        print(f'({v["nome"]})', end=' ')
