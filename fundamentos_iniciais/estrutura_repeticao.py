for i in range(5):
    print('Michele')

produtos = ['pepsi', 'coca', 'guaraná']
producao = [1500, 5000, 3500]

for i in range(3):
    print('{} unidades produzidas de {}.'.format(producao[i], produtos[i]))

for produto in produtos: #percorre a lista
    print(produto)

vendas = [1200, 500, 3000, 890, 2340]
meta = 1000

qtd_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtd_bateu_meta += 1

qtd_funcionarios = len(vendas)

print('O percentual de pessoas que bateram a meta foi de {:.1%}'.format(qtd_bateu_meta / qtd_funcionarios))

produtos = ['pepsi', 'coca', 'guaraná']
estoque = [1500, 5000, 25]
nivel_minimo = 50

for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print(f'{produtos[i]} está abaixo do nível mínimo de estoque. Temos apenas {estoque[i]} unidades.')

estoque = [
    [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
    [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
    [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
    [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
    [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
]
fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
nivel_minimo = 50
fabricas_nivel_baixo = []

for i, lista in enumerate(estoque):
    for qtde in lista:
        if qtde < nivel_minimo:
            if fabricas[i] in fabricas_nivel_baixo:
                pass
            else:
                fabricas_nivel_baixo.append(fabricas[i])

print(fabricas_nivel_baixo)
