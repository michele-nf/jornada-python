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
