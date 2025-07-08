def cadastrar_produto():
    produto = input('Informe o produto: ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto

produto = cadastrar_produto()
print(f'Produto cadastrado: {produto}')


