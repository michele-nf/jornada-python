mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# pegando a informação com a chave
print(vendas_tecnologia['iphone'])
print(vendas_tecnologia['samsung galaxy'])

# pegando a informação com o método get
print(vendas_tecnologia.get('iphone'))
print(vendas_tecnologia.get('samsung galaxy'))

lucro_1tri = {'janeiro': 15000, 'fevereiro': 12000, 'março': 10000}
lucro_2tri = {'abril': 14300, 'maio': 1720, 'junho': 1000}

# Adicionar e modificar valores
print(lucro_1tri)
lucro_1tri['abril'] = 10000
print(lucro_1tri)
lucro_1tri.update(lucro_2tri)
print(lucro_1tri)

# Deletar valores
del lucro_1tri['abril']
print(lucro_1tri)
valor = lucro_1tri.pop('maio')
print(lucro_1tri)
print(valor)

total_notebooks = 0

for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]

print(f'Total de vendas de notebooks: {total_notebooks}')

for produto, vendas in vendas_tecnologia.items():
    if vendas > 5000:
        print(f'O produto {produto} teve vendas acima de 5000 unidades, totalizando {vendas} unidades vendidas.')

for chave in vendas_tecnologia:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades vendidas.')
print('-' * 40)

lista_chaves = list(vendas_tecnologia.keys())
lista_chaves.sort()

for chave in lista_chaves:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades vendidas.')

lista_a = [1, 2, 3, 4, 5]
Lista_b = ['João', 'Maria', 'José', 'Ana', 'Pedro']

lista_ab = zip(lista_a, Lista_b)
print(lista_ab)
dicionario_ab = dict(lista_ab)
print(dicionario_ab)