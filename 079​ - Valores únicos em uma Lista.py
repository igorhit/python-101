# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.

lst = []
resp = ''
while True:
    num = int(input('Digite um número: '))
    if num in lst:
        print('Falha no cadastro! Número já cadastrado!')
    else:
        print('Cadastro realizado com sucesso!')
        lst.append(num)
    resp = str(input('Deseja digitar mais um número? (S/N) ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'A lista dos números digitados: {sorted(lst)}')
