# Faça um mini-sistema que utilize o Interactive Help do
# Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o
# programa se encerrará. Importante: use cores.

from time import sleep
c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m',
     '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m')


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[2], end='')
    help(com)
    print(c[2], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 6
    print(c[cor], end='')
    print('~' * tam)
    print(f'   {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 6)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('VOLTE SEMPRE!', 6)
