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


def resumo(preco=0, taxaa=10, taxar=5):
    print('-=' * 20)
    print('RESUMO DO VALOR'.center(40))
    print('-=' * 20)
    print(f'Preço analisado: \t\t\t{formatado(preco)}')
    print(f'Dobro do preço: \t\t\t{dobro(preco)}')
    print(f'Metade do preço: \t\t\t{metade(preco)}')
    print(f'Com {taxaa}% de aumento: \t\t{aumentar(preco, taxaa)}')
    print(f'Com {taxar}% de desconto: \t\t{diminuir(preco, taxaa)}')
    print('-=' * 20)
