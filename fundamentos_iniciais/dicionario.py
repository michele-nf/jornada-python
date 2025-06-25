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
