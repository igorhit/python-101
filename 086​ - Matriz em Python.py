# Crie um programa que declare uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Posição {l},{c}: ")))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
