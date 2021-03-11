# Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

lst = []
while True:
    aluno = str(input('Aluno: ')).strip().upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lst.append([aluno, [nota1, nota2], media])
    r = str(input('Continuar? (S/N)')).strip().upper()[0]
    if r in 'N':
        break
print(f'{"N":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lst):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    r2 = int(input('Para mostrar as notas, digite o número do aluno.'
                   '\n(Digite 000 para encerrar) '))
    if r2 == 000:
        break
    if r2 <= len(lst) - 1:
        print(f'As notas de {lst[r2-1][0]} são {lst[r2-1][1]}')
