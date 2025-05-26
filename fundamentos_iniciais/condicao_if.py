meta = 5000
vendas = 65000

if vendas > meta:
    print(f"Batemos a meta de vendas, vendemos {vendas} celulares.")
else:
    print(f"Não batemos a meta, vendemos {vendas} celulares. A meta era de {meta} unidades.")

meta = 0.05
taxa = 0
rendimento = 0.25

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print(f"A taxa foi de {taxa}")
    else:
        taxa = 0.02
        print(f"A taxa foi de {taxa}")
else:
    taxa = 0
    print(f"A taxa foi de {taxa}")

meta = 20000
vendas = 15000

if vendas < meta:
    print("Não ganhou bônus!")
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print(f"Ganhou {bonus} de bônus")
else:
    bonus = 0.03 * vendas
    print(f"Ganhou {bonus} de bônus")

# comparadores
idade = 18
if idade == 18:
    print("Você tem exatamente 18 anos")
else:
    print("Você não tem 18 anos")

senha = "1234"
if senha != "senha123":
    print("Senha incorreta")
else:
    print("Acesso permitido")

nota = 7.5
if nota > 7.0:
    print("Aprovado")
else:
    print("Recuperação ou reprovado")

estoque = 5
if estoque < 10:
    print("Estoque baixo, é necessário repor")
else:
    pass  # Não faz nada se o estoque estiver OK

frase = "Python é uma linguagem poderosa"
if "poderosa" in frase:
    print("A frase contém a palavra 'poderosa'")
else:
    print("Palavra não encontrada")

logado = False
if not logado:
    print("Por favor, faça login")
else:
    print("Bem-vindo ao sistema")
