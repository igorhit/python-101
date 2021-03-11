# Aprimore o desafio 93 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

artilheiro = {}
gols = []
time = []
while True:
    artilheiro.clear()
    artilheiro['Jogador'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input('Quantas partidas jogadas? '))
    gols.clear()
    for part in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {part}? ')))
    artilheiro['Gols'] = gols[:]
    artilheiro['Total'] = sum(gols)
    time.append(artilheiro.copy())
    while True:
        r = str(input('Continuar? (S/N) ')).strip().upper()[0]
        if r in 'SN':
            break
        print('Digite somente S ou N.')
    if r == 'N':
        break
print('=' * 60)
print('cod. ', end='')
for i in artilheiro.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k+1:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    stats = int(input('Mostrar estatísticas de qual jogador? (999 encerra) '))
    if stats == 999:
        break
    if stats > len(time):
        print(f'ERRO! Jogador {stats} não encontrado!')
    else:
        print(f'Estatísticas do jogador {time[stats-1]["Jogador"]}')
        for i, g in enumerate(time[stats-1]['Gols']):
            print(f'Jogo {i+1}, marcou {g} gols.')
    print('-' * 50)
print('=' * 60)
print('<<  PROGRAMA ENCERRADO!!!  >>')
