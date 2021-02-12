#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

n = float(input('Quantos Reais você tem? '))
print('{} Reais compram:\n{:.2f} dólares americanos\n{:.2f} euros\n{:.2f} ienes'
      .format(n, n / 5.43, n / 6.56, n / 0.0518))
