import webbrowser
import time
from datetime import datetime
import matplotlib.pyplot as plt

webbrowser.open("https://docs.python.org/3/tutorial/modules.html")

segundos_hoje = time.time()
print(f"Segundos desde a época: {segundos_hoje}")

data_hoje = time.ctime()
print(f"Data e hora atual: {data_hoje}")

print("Começando")
time.sleep(5)
print("Rodou 5 segundos após")

hora_geral = time.gmtime()
hora_local = time.localtime()
print(hora_geral)
print(hora_local)

dia = hora_local.tm_mday
mes = hora_local.tm_mon
ano = hora_local.tm_year
dia_da_semana = hora_local.tm_wday

print("Data: {}/{}/{}".format(dia, mes, ano))
print(f"Data: {dia}/{mes}/{ano}")

agora = datetime.now()
print(agora)
data = agora.date()
hora = agora.time()
print(data)
print(hora)

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
data_atual = datetime.now()

idade = data_atual.year - data_nascimento.year
if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

print(f"Sua idade é: {idade} anos")


vendas = [1500, 1800, 1200, 2200, 2500, 3000, 2800, 3200, 4000, 4500, 5000, 6000]
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

plt.plot(meses, vendas)
plt.title("Vendas Mensais")
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")
plt.axis(0, 11, 0, max(vendas) + 500)
plt.show()
