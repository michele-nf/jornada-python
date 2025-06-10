for i in range(5):
    print('Michele')

produtos = ['pepsi', 'coca', 'guaraná']
producao = [1500, 5000, 3500]

for i in range(3):
    print('{} unidades produzidas de {}.'.format(producao[i], produtos[i]))

for produto in produtos: #percorre a lista
    print(produto)
