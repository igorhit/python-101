# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar
# valores.

soma = qt = med = maior = menor = 0
r = 'S'
while r in 'S':
    num = int(input('Digite um número: '))
    qt += 1
    soma += num
    med = soma / qt
    if qt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer digitar mais um número? (S/N) ')).upper().strip()[0]
print(f'O maior número digitado foi {maior}.'
      f'\nO menor número digitado foi {menor}.'
      f'\nA média de todos os valores digitados é {med}.')
