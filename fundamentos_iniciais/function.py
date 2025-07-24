def cadastrar_produto():
    produto = input('Informe o produto: ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto

produto = cadastrar_produto()
print(f'Produto cadastrado: {produto}')

def somar_numeros(num1, num2, num3):
    return num1 + num2 + num3

soma = somar_numeros(10, 20, 30)
print(f'Soma dos números: {soma}')

produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

def eh_da_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False
    
for produto in produtos:
    if eh_da_categoria(produto, 'BEB'):
        print(f'{produto} é uma bebida alcoólica.')
    elif eh_da_categoria(produto, 'BSA'):
        print(f'{produto} não é uma bebida alcoólica.')

preco = 1500
custo = 400
lucro = 785

def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco

print('A carga tributária foi de {:.1%}'.format(carga_tributaria(preco, custo, lucro)))

precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37,2.4,1.72,2,1.69,1.63,2.01,2.25,1.61,1.02,1.19,1.86,2.15,2.03,1.61,1.52,1.56,1.69,1.47,1.09,2.47,1.62,2.15,1.81,2.49,2.08,1.02,1.68,1.53,1.2,1.29,1.88,1.92,2.14,1.95,2.48,2.44,1.41,1.98,1.89,1.69,1.95,1.42,1.57,2.32,1.23,1.43,1.35,1.49,2.39,2.37,1.3,2.25,1.5,1.35,2.06,1.05,1.7,2.29,2.44,2.09,1.81,2.04,2.45,1.42,2.09,2.19,2.09,1,2.23,1.39,2,1.29,1.55,1.67,2.06,1.89,2.07,2.39,1.93,1.51,1.73,1.66,1.18,1.13,1.69,2.48,1.26,1.75, 1.51, 1.73]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147,222,165,184,175,147,217,214,171,86,111,180,211,210,168,156,154,179,163,99,246,162,205,195,263,198,121,149,140,122,119,197,210,218,202,258,256,135,203,173,152,197,145,154,252,141,141,151,133,232,229,134,215,155,138,186,120,152,213,256,219,200,210,238,140,224,233,222,120,233,151,185,111,149,186,194,194,222,223,185,157,154,164,129,128,169,240,136,191, 157, 154]


def separar_listas(precos, tamanhos, fator=0.1):
        if len(precos) == len(tamanhos):
            #executar o codigo
            i = int((1 - fator) * len(precos))
            precos_imoveis_treino = precos[:i]
            precos_imoveis_teste = precos[i:]
            tamanho_imoveis_teste = tamanhos[i:]
            tamanho_imoveis_treino = tamanhos[:i]
            return precos_imoveis_treino, precos_imoveis_teste, tamanho_imoveis_treino, tamanho_imoveis_teste
        else:
            print('As listas de precos e tamanhos dos imoveis não têm a mesma quantidade de itens')
            return


print(len(precos_imoveis))
precos_treino, precos_teste, tamanho_treino, tamanho_teste = separar_listas(precos_imoveis, tamanho_imoveis)

def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
print(minha_soma(1, 2, 3, 4, 5))

def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra'] 
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco
print(preco_final(1000, desconto=0.1, garantia_extra = 100, imposto=0.3))
