# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3c = maior2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Posição {l},{c}: "))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if l == 1 and matriz[l][c] > maior2l:
            maior2l = matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
    print()
print(f'A soma dos pares é {somapar}.'
      f'\nA soma da terceira coluna é {soma3c}.'
      f'\nO maior número da segunda linha é {maior2l}.')
