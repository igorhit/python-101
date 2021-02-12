# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

radar = float(input('Qual a velocidade que o carro passou no radar? '))
if radar > 80:
    print('\033[1;4;31mMULTADO!\033[m Você excedeu o limite permitido de 80Km/h'
          '\nA multa é de R${:.2f}'.format((radar - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')