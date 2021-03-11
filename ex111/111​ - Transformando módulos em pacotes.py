# Crie um pacote chamado utilidades CeV que tenha
# dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios
# 107, 108 e 109 para o primeiro pacote e mantenha
# tudo funcionando.

from ex111.utilidadescev import moeda

preco = float(input('Informe o preço: R$'))
moeda.resumo(preco, 25, 14)
