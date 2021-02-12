# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
# MODIFICAÇÕES MINHAS: invés de 1 até 500, o usuário pode escolher o intervalo

soma = 0
cont = 0
inicio = int(input('Digite o número inicial: ')) #MODIFICADO
final = int(input('Digite o número final: ')) #MODIFICADO
# for c in range(1, 501, 2): ORIGINAL
for c in range(inicio, final, 2): #MODIFICADO
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'Foram encontrados {cont} números entre 1 e 500 que são ímpares múltiplos de 3'
      f'\ne a soma de todos eles é de {soma}.')
