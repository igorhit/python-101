def aumentar(preco=0, taxa=0, formato=True):
    res = preco + (preco * taxa/100)
    return res if not formato else formatado(res)


def diminuir(preco=0, taxa=0, formato=True):
    res = preco + (preco * taxa / 100)
    return res if not formato else formatado(res)


def dobro(preco=0, formato=True):
    res = preco * 2
    return res if not formato else formatado(res)


def metade(preco=0, formato=True):
    res = preco / 2
    return res if not formato else formatado(res)


def formatado(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
