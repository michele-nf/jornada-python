email = "michele.ferreira@email.com"
nome = "Michele Ferreira"

print(len(email))
print(len(nome))    

print(email[0])
print(nome[1]) 
print(email[-3])
print(nome[:7]) #não considera índice 7
print(nome[7:]) #considera índice 7
print(nome[2:7])

faturamento = 1000
custo = 500
lucro = faturamento - custo

print("O faturamento da loja foi de: " + str(faturamento))
print("O faturamento da loja foi de: {}." .format(faturamento))
print("O faturamento da loja foi de: {0}. O custo da loja foi de: {1}, lembrando que o faturamento foi de: {0}." .format(faturamento, custo))
print("O faturamento da loja foi de: %d. O custo da loja foi de: %d." % (faturamento, custo))
print(nome.capitalize())
print(nome.casefold())
print(nome.count('e'))
print(nome.endswith("Ferreira"))
print(nome.find('F'))
print(nome.isalnum())
print(nome.isalpha())
print(nome.isnumeric())
print(nome.replace('Ferreira', 'Desenvolvedora'))
print(nome.split(' '))
print(nome.startswith('Mi'))
print(nome.strip()) 
print(nome.title())
print(nome.upper())
