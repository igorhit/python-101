# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.
ano = int(input('Digite o ano do seu nascimento: '))
anohj = 2021
anoat = anohj - ano
falta = 17 - anoat
devia = anoat - 17
print(f'Nascidos em {ano} tem {anoat} ano(s).')
if anoat == 17:
    print('\033[32mEstá na hora de se alistar!\033[m Procure a junta militar mais próxima!')
elif anoat < 17:
    print(f'Ainda faltam {falta} ano(s) para o ano em que estará com 17 anos.'
          '\n\033[34mAinda não está na hora de ajudar seu país.\033[m '
          '\nTente novamente no ano em que for completar 17 anos.'
          f'\nSeu alistamento será em {anohj + falta}.')
else:
    print(f'Você deveria ter se alistado a {devia} ano(s) atrás.'
          '\n\033[31mVocê está inadimplente com as forças armadas!\033[m '
          '\nProcure a junta militar mais próxima!'
          f'\nSeu alistamento foi em {anohj - devia}.')
