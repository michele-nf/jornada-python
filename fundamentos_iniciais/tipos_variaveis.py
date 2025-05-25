idade = 32
peso = 54.35
nome = "Michele Ferreira"
mulher = True

print(type(idade), type(peso), type(nome), type(mulher)) # exibe tipos de variáveis
print("A " + str(nome) + " tem " + str(idade) + " anos e pesa " + str(peso) + "kg.") # concatena variáveis
print("A {} tem {} anos e pesa {}kg." .format(nome, idade, peso)) # utiliza método format()
print(f"A {nome} tem {idade} anos e pesa {peso}kg.") # utiliza f-string

# mudança de tipo de variável
faturamento = float(input("Qual é o seu faturamento?"))
custo = float(input("Qual é o seu custo?"))

lucro = faturamento - custo

print(lucro)
