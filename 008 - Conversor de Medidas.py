#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = int(input('Digite a medida em metros: '))
print('A medida inserida é igual a:\n{} milímetros\n{} centímetros'.format(n * 1000, n * 100))