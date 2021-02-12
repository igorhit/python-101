#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE2 A SUA ÁREA
# E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA
# UMA ÁREA DE 2m^2

l = float(input('Digite a largura da parede (em metros): '))
h = float(input('Digite a altura da parede (em metros): '))
a = float(l * h)
t = float(a / 2)
print('A quantidade de tinta necessária para pintar a parede, com as medidas inseridas é de {} litros'.format(t))
