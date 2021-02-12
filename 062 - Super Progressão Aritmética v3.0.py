# Melhore o DESAFIO 061, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.

prtr = int(input('Primeiro termo: '))
rz = int(input('Razão de: '))
termo = prtr
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
       print(f'{termo} >> ', end='')
       termo += rz
       cont += 1
    print('Esperando...')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print(f'Progressão Aritmética finalizada com {total} termos exibidos.')
print('FIM')