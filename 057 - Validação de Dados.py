# Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
# até ter um valor correto.
# MODIFICAÇÃO MINHA = #MM

gen = str(input('Qual o seu gênero?'
                '\nDigite (M) para MASCULINO'
                '\nDigite (F) para FEMININO'
                '\nDigite (NDA) caso não queira se identificar: ')).strip().upper()  # MM
while gen not in 'MFNDA':
    print('\nDados inválidos. Por favor, \033[1;4mDIGITE EXATAMENTE\033[m '
          'uma das opções demonstradas entre parênteses')
    print('=' * 100)
    gen = str(input('Qual o seu gênero?'
                    '\nDigite (M) para MASCULINO'
                    '\nDigite (F) para FEMININO'
                    '\nDigite (NDA) caso não queira se identificar: ')).strip().upper()
if gen == 'M':
    print('Sexo \033[95mMASCULINO\033[m registrado com sucesso!')  # MM
elif gen == 'F':
    print('Sexo \033[34mFEMININO\033[m registrado com sucesso!')  # MM
else:
    print('Sexo NÃO IDENTIFICADO registrado com sucesso!')  # MM
