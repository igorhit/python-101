# Modifique as funções que foram criadas no desafio 107 para
# que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda

preco = float(input("Informe o preço: R$"))
print(f"A metade de R${moeda.formatado(preco)} é R${moeda.metade(preco)}")
print(f"O dobro de R${moeda.formatado(preco)} é R${moeda.dobro(preco)}")
print(f"Aumentando 10%, temos R${moeda.aumentar(preco, 10)}")
print(f"Reduzindo 13%, temos R${moeda.diminuir(preco, 13)}")
