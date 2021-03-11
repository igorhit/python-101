# Crie um pequeno sistema modularizado que permita cadastrar
# pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e
# listar todas as pessoas cadastradas

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqexiste(arq):
    criararq(arq)

while True:
    resp = menu(['Ver Cadastros', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerarq(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Encerrando o sistema...Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
