# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função
# leiaFloat() com a mesma funcionalidade.


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO!!! Favor digitar um número Inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO!!! Favor digitar um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um número Inteiro: ')
n2 = leiafloat('Digite um número Real: ')
print(f'O número Inteiro digitado foi {n1} e o Real foi {n2}.')
