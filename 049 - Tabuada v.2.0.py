# Refaça o DESAFIO 009, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número e te direi seus múltiplos até 10: '))
for c in range(1, 11):
    print(f'{num} x {c:2}  = {c * num}')