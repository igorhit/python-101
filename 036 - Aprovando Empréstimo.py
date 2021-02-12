# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não
# pode exceder 30% do salário ou então o empréstimo será negado.

imovel = float(input('Qual o valor do imóvel? R$'))
anos = int(input('Em quantos anos será o financiamento? '))
salario = float(input('Informe sua renda mensal: R$'))
prestacao = imovel / (anos * 12)
print(f'A prestação de um imóvel de valor R${imovel:.2f},'
      f'\nfinanciado em {anos} anos é de R${prestacao:.2f} mensais')
if prestacao >= salario * 0.3:
    print('Infelizmente seu financiamento foi \033[31mNEGADO\033[m')
else:
    print('Parabéns! Seu financiamento foi \033[34mAPROVADO\033[m!')
