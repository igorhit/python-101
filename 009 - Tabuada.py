n = float(input('Digite um número e te mostrarei seus múltiplos até 10: '))
print('--------------------------------')
print('{0} x  1 = {0:.2f}\n{0} x  2 = {1:.2f}\n{0} x  3 = {2:.2f}\n{0} x  4 = {3:.2f}\n{0} x  5 = {4:.2f}\n'
      '{0} x  6 = {5:.2f}\n{0} x  7 = {6:.2f}\n{0} x  8 = {7:.2f}\n{0} x  9 = {8:.2f}\n{0} x 10 = {9:.2f}'
      '\n--------------------------------'
      .format(n, (n * 2), (n * 3), (n * 4), (n * 5), (n * 6), (n * 7), (n * 8), (n * 9), (n * 10)))
