vendas = ('Michele', 32, 1500.50, 'Vendedora', True)
nome = vendas[0]
print(f'Nome: {nome}')
idade = vendas[1]
print(f'Idade: {idade}')
vendas_totais = vendas[2]
print(f'Vendas Totais: R$ {vendas_totais}')    
cargo = vendas[3]
print(f'Cargo: {cargo}')
ativo = vendas[4]
print(f'Usuário ativo: {ativo}')

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

faturamento = 0
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item 
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_unitario
        

#data, produto, cor, capacidade, unidades, valor_unitario = vendas[0]

#faturamento = unidades * valor_unitario
print('O faturamento de IPhone no dia 20/08/2020 foi de {}'.format(faturamento))

produto_mais_vendido = ''
qtde_produto_mais_vendido = 0
cor_produto_mais_vendido = ''
capacidade_produto_mais_vendido = ''
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if data == '21/08/2020':
        if unidades > qtde_produto_mais_vendido:
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = unidades
            cor_produto_mais_vendido = cor
            capacidade_produto_mais_vendido = capacidade

print('Meu produto mais vendido no dia 21/08/2020 foi o {} com {} unidades. Cor: {}, Capacidade {}'
      .format(produto_mais_vendido, qtde_produto_mais_vendido, cor_produto_mais_vendido, capacidade_produto_mais_vendido))
