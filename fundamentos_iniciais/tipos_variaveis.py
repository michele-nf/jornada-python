idade = 32
peso = 54.35
nome = "Michele Ferreira"
mulher = True

print(type(idade), type(peso), type(nome), type(mulher)) # exibe tipos de variáveis
print("A " + str(nome) + " tem " + str(idade) + " anos e pesa " + str(peso) + "kg.") # concatena variáveis
print("A {} tem {} anos e pesa {}kg." .format(nome, idade, peso)) # utiliza método format()
print(f"A {nome} tem {idade} anos e pesa {peso}kg.") #utiliza f-string
