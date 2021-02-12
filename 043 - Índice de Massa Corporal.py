# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 24,9: Peso Ideal
# - 25 até 29,9: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

h = float(input('Digite sua altura (em cm): '))
p = float(input('Digite seu peso (em Kg): '))
imc = p / ((h / 100) ** 2)
print(f'Seu IMC é {imc:.1f}')
if imc <= 18.5:
    print('Seu status na categoria de peso é: ABAIXO DO PESO')
elif imc <= 24.9:
    print('Seu status na categoria de peso é: PESO IDEAL')
elif imc <= 29.9:
    print('Seu status na categoria de peso é: SOBREPESO')
elif imc <= 40:
    print('Seu status na categoria de peso é: OBESIDADE')
else:
    print('Seu status na categoria de peso é: OBESIDADE MÓRBIDA')
