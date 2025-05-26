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
