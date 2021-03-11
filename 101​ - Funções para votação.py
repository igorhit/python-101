# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return 'Voto NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'Voto OPCIONAL'
    else:
        return 'Voto OBRIGATÓRIO'


nasc = int(input('Digite o ano de seu nascimento: '))
print(voto(nasc))
