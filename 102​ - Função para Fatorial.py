# Crie um programa que tenha uma função fatorial() que
# receba dois parâmetros: o primeiro que indique o número
# a calcular e outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo
# de cálculo do fatorial.

def fatorial(n, show):
    f = 1
    while n > 0:
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= n
        n -= 1
    return f


num = int(input('Digite um número: '))
mostrar = str(input('Gostaria de exibir o cálculo completo? (S/N) ')).strip().upper()[0]
if mostrar == 'S':
    mostrar = True
elif mostrar == 'N':
    mostrar = False
print(fatorial(num, mostrar))
