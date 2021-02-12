# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por Km rodado.
km = float(input('Quantos Km percorridos? '))
dias = int(input('Quantos dias de aluguel? '))
preco = (0.15 * km) + (60 * dias)
print('O total a ser pago é de R${:.2f}'.format(preco))
