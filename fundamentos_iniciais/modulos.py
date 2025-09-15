import webbrowser
import time
from datetime import datetime

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
