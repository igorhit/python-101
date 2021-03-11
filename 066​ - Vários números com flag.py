# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre elas (desconsiderando o flag).

num = qt = maior = menor = soma = 0
while True:
    num = int(input('Digite um número (000 para parar): '))
    if num == 000:
        break
    qt += 1
    soma += num
    if qt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Foram digitados {qt} números.'
      f'\nO menor valor foi {menor} e o maior valor foi {maior}'
      f'\nA soma de todos os números digitados é {soma}.')
