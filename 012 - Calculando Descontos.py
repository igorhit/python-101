# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM
# PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO

preço = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o desconto (em porcentagem): '))
final = 100 - desconto
total = (preço * final / 100)
print('O valor do produto, com {}% de desconto, é de R${:.2f}'.format(desconto, total))
