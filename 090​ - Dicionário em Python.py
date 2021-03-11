# Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.

aluno = {}
aluno['Nome'] = str(input('Nome: ')).upper().strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Status'] = 'Aprovado'
elif aluno['Média'] > 5 < 7:
    aluno['Status'] = 'Recuperação'
else:
    aluno['Status'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k} -> {v}.')
