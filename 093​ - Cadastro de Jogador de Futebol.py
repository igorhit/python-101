# Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

artilheiro = {'jogador': str(input('Nome do jogador: ')).strip()}
gols = []
partidas = int(input('Quantas partidas jogadas? '))
for part in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {part}? ')))
artilheiro['gols'] = gols[:]
artilheiro['totalgols'] = sum(gols)
print(f'O jogador {artilheiro["jogador"]} jogou {partidas} '
      f'partidas.')
for i, v in enumerate(artilheiro['gols']):
    print(f'Partida {i+1}, marcou {v} gols.')
print(f'Total de {artilheiro["totalgols"]} gols marcados.')
