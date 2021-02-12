# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a
# R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

salario = float(input('Digite o salário sujeito ao aumento: R$'))
if salario > 1250:
    print(f'O novo salário, com 10% de aumento, é de R${salario * 1.1:.2f}')
else:
    print(f'O novo salário, com 15% de aumento, é de R${salario * 1.15:.2f}')
