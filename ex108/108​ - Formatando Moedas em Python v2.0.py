# Adapte o código do desafio #107, criando uma função
# adicional chamada moeda() que consiga mostrar os números
# como um valor monetário formatado.

import moeda

preco = float(input('Informe o preço: R$'))
print(f"A metade de R${moeda.formatado(preco)} é R${moeda.formatado(moeda.metade(preco))}")
print(f"O dobro de R${moeda.formatado(preco)} é R${moeda.formatado(moeda.dobro(preco))}")
print(f"Aumentando 10%, temos R${moeda.formatado(moeda.aumentar(preco, 10))}")
print(f"Reduzindo 13%, temos R${moeda.formatado(moeda.diminuir(preco, 13))}")
