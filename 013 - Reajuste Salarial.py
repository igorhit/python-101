#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU
#NOVO SALÁRIO COM 15% DE AUMENTO

salario = float(input('Digite o salário do funcionário: R$'))
aumento = float(input('Digite a quantidade de aumento (em porcentagem): '))
salarionovo = salario + (salario * aumento / 100)
print('O salário do funcionário, com {}% de aumento passará a ser de R${:.2f}'.format(aumento, salarionovo))
