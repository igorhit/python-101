# Exercício Python 022: Crie um programa que leia o nome completo de
# uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: '))
print('- Seu nome, escrito somente em letras maiúsculas, fica assim: {}'
      .format(nome.upper()))
print('- Seu nome, escrito somente em letras mainúsculas, fica assim: {}'
      .format(nome.lower()))
print('- Seu nome contém {} letras'.format(len(nome) - nome.count(' ')))
print('- O seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
