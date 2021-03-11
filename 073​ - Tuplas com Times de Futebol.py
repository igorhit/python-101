# Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = 'Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', \
        'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', \
        'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', \
        'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo'
print(f'CAMPEONATO BRASILEIRO 2020!'
      f'\nOs 5 primeiros colocados são {times[0:5]}'
      f'\nOs 4 últimos colocados são {times[-4:]}'
      f'\nTimes em ordem alfabética: {sorted(times)}'
      f'\nO Flamengo está na {times.index("Flamengo") + 1}ª posição')

