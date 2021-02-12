# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite o que quiser e te direi o que é: ')
print('O tipo primitivo é', type(a))
print('Só deu espaços?', a.isspace())
print('Digitou só números?', a.isnumeric())
print('Digitou só letras?', a.isalpha())
print('Digitou letras e números?', a.isalnum())
print('Digitou só em minúsculo?', a.islower())
print('Digitou só em maiúsculo?', a.isupper())
print('Digitou só a primeira letra em maiúsculo?', a.istitle())
