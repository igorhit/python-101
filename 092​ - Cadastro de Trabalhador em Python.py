# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um
# dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.

from datetime import date
funcionario = {'Nome': str(input('Nome: ')).upper().strip()}
nasc = int(input('Ano de nascimento: '))
funcionario['Idade'] = date.today().year - nasc
ctps = int(input('CTPS (0 caso não possua): '))
if ctps != 0:
    funcionario['CTPS'] = ctps
    funcionario['Contrato'] = int(input('Início do contrato: '))
    funcionario['Aposentadoria'] = 35 - (date.today().year - funcionario['Contrato'])
    funcionario['Salário'] = int(input('Salário: R$'))
for k, v in funcionario.items():
    print(f'{k}: {v}')
