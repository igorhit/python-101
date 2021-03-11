# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('Casa', 'Tempo', 'Ano', 'Dia', 'Vez', 'Homem', 'Senhor', 'Senhora')
for vogais in palavras:
    print(f'\nVogais da palavra ({vogais.upper()}): ', end='')
    for letra in vogais:
        if letra.lower() in 'aeiou':
            print(letra, end='')
