# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: R$'))
pag = int(input('Escolha uma das opções para pagamento:'
                '\n[ 1 ] à vista dinheiro/cheque: 10% de desconto'
                '\n[ 2 ] à vista no cartão: 5% de desconto'
                '\n[ 3 ] em até 2x no cartão: preço normal'
                '\n[ 4 ] 3x ou mais no cartão: 20% de juros'
                '\nDigite o número correspondente a sua opção: '))
o1 = valor - (valor * 10 / 100)
o2 = valor - (valor * 5 / 100)
o3 = valor
o4 = valor + (valor * 20 / 100)

if pag == 1:
    print(f'Para pagamentos em dinheiro/cheque, o valor passa a ser de R${o1:.2f}.')
elif pag == 2:
    print(f'Para pagamentos à vista no cartão, o valor passa a ser de R${o2:.2f}.')
elif pag == 3:
    print(f'Para pagamentos parcelados em até 2x, o valor é de R${o3:.2f}'
          f'\nem 2 parcelas de {o3 / 2:.2f}.')
elif pag == 4:
    parc = int(input('Em quantas parcelas gostaria de parcelar? '))
    print(f'Para pagamentos parcelados em 3x ou mais, o valor passa a ser de R${o4:.2f}.'
          f'\nem {parc} parcelas de R${o4 / parc:.2f}.')
else:
    print('OPÇÃO INVÁLIDA! Por favor, tente novamente.')
