#Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127O número 6.127 tem a parte Inteira 6.

#from math import trunc
#n = float(input('Digite um número com dígitos decimais: '))
#print('O valor inserido foi {} e sua porção inteira é {}'.format(n, trunc(n)))
n = float(input('Digite um número com dígitos decimais: '))
print('O valor inserido foi {} e sua porção inteira é {}'.format(n, int(n)))