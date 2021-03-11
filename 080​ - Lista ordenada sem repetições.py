# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela.

lst = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        lst.append(n)
        print('Primeiro número inserido.')
    elif n > lst[-1]:
        lst.insert(lst[-1], n)
        print('Número inserido na última posição.')
    else:
        i = 0
        while i < len(lst):
            if n <= lst[i]:
                lst.insert(i, n)
                print(f'Número inserido na posição {i}.')
                break
            i += 1
print(f'Os números digitados, em ordem, são: {lst}.')
