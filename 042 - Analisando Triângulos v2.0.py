# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima \033[4mPODEM\033[m formar um triângulo!')
    if seg1 == seg2 == seg3:
        print('O triângulo, formado com os segmentos escolhidos, é \033[4mEQUILÁTERO\033[m.')
    elif seg1 != seg2 != seg3 != seg1:
        print('O triângulo, formado com os segmentos escolhidos, é \033[4mESCALENO\033[m.')
    else:
        print('O triângulo, formado com os segmentos escolhidos, é \033[4mISÓSCELES\033[m.')
else:
    print('Os segmentos acima \033[4mNÃO PODEM\033[m formar um triângulo!')