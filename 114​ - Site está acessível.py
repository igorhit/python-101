# Crie um código em Python que teste se o site pudim
# está acessível pelo computador usado.

import urllib
from urllib import request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site não acessível!')
else:
    print('Site acessado com sucesso!')
    print(site.read())
