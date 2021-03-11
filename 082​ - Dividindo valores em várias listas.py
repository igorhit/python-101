# Crie um programa que vai ler vários números e colocar em uma
# lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

todos = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    todos.append(n)
    if n % 2:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Deseja digitar mais um número? '
                  '\n(Digite "N" para encerrar) ')).strip().upper()[0]
    if r in "N":
        break
print(f'A lista completa dos números digitados é: {todos}.'
      f'\nA lista dos números pares é: {sorted(pares)}.'
      f'\nA lista dos números impares é: {sorted(impares)}.')
