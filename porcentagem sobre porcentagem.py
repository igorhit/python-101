num = float(input('Digite o valor desejado: '))
por1 = float(input('Digite o valor da primeira porcentagem '
                   'de desconto a ser aplicada: '))
por2 = float(input('Digite o valor da porcentagem a ser aplicada sobre a '
                   'primeira: '))
desc1 = num - (num * por1 / 100)
desc2 = desc1 - (desc1 * por2 / 100)
portotal = (num - desc2) / (num / 100)
print(f'O valor \033[1;4;31m{num}\033[m com \033[1;4;33m{por1}%\033[m de desconto é de \033[1;4;34m{desc1:.2f}\033[m'
      f'\nAplicando mais \033[1;4;33m{por2}%\033[m de desconto, o valor fica em \033[1;4;94m{desc2:.2f}\033[m'
      f'\nO valor total de porcentagem de desconto foi de \033[1;4;32m{portotal:.2f}%\033[m aplicado sobre '
      f'o valor inicial')