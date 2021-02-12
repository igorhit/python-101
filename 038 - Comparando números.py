# Escreva um programa que leia dois números inteiros e compare-os.

a = float(input('Digite um número: '))
b = float(input('Digite mais um número: '))
if a > b:
    print('O \033[4mprimeiro\033[m valor é maior.')
elif a < b:
    print('O \033[4msegundo\033[m valor é maior.')
elif a == b:
    print('Os dois números são \033[4miguais\033[m.')
