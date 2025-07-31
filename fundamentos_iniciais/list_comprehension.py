preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

#digamos que o imposto sobre os produtos é de 30%, ou seja, 0.3. Como eu faria para criar uma lista com os 
#valores de imposto de cada produto?

# Usando for
impostos = []
for preco in preco_produtos:
    impostos.append(preco * 0.3)
print(impostos)

# Usando list comprehension
impostos_comprehension = [preco * 0.3 for preco in preco_produtos]
print(impostos_comprehension)

# Ordenar duas listas relacionadas
lista_auxiliar = list(zip(produtos, preco_produtos))
lista_auxiliar.sort()
produtos = [produto for produto in lista_auxiliar]

print(produtos)
