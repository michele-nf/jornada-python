produtos = ["tv", "celular", "mouse", "teclado", "tablet"]
vendas = [1000, 1500, 350, 270, 900]

vendas[1] = 2000
print("Vendas do produto {} foram de {} unidades".format(produtos[1], vendas[1]))
print(vendas)

texto = "michele@teste.com"
texto = texto.replace("michele", "isabela")
print(texto)

i = produtos.index("teclado")
qtd_vendas = vendas[i] 

print(f"A quantidade de vendas do produto {produtos[i]} é de: {qtd_vendas} unidades.") 

# adicionar item
produtos.append("geladeira")
print(produtos)

# remover item
produtos.pop(0)
produtos.remove("geladeira")
print(produtos)

# 2 formas de tratar erro
remover_produtos = "casa"
if remover_produtos in produtos:
    produtos.remove(remover_produtos)
else:
    print(f"O produto {remover_produtos} não existe na lista.")

try:
    produtos.remove(remover_produtos)
except:
    print(f"O produto {remover_produtos} não existe na lista.")
