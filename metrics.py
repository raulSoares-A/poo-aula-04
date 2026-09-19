import csv
import os
import psutil
from datetime import datetime

#
class Metrica():
    def __init__(self, unidade, valor):
        self.unidade = unidade
        self.valor = valor


class MetricaCPU(Metrica):
    def __init__(self):
        valor = psutil.cpu_percent(interval=1)
        super().__init__("%", valor)


class MetricaMemoria(Metrica):
    def __init__(self):
        memoria = psutil.virtual_memory()
        valor = memoria.used / (1024 * 1024)
        super().__init__("MB", valor)


class MetricaDisco(Metrica):
    def __init__(self):
        disco = psutil.disk_usage('/')
        valor = disco.free / (1024 * 1024)
        super().__init__("MB", valor)


cpu = MetricaCPU()
memoria = MetricaMemoria()
disco = MetricaDisco()

agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Data e hora:", agora)
print("CPU:", cpu.valor, cpu.unidade)
print("Memoria:", memoria.valor, memoria.unidade)
print("Disco:", disco.valor, disco.unidade)

with open("metricas.csv", mode="a", newline="") as arquivo:

    escritor = csv.writer(arquivo)
    if os.path.getsize("metricas.csv") == 0:

        escritor.writerow(["datetime", "metrica", "valor", "unidade"])
        escritor.writerow([agora, "CPU", cpu.valor, cpu.unidade])
        escritor.writerow([agora, "Memoria", memoria.valor, memoria.unidade])
        escritor.writerow([agora, "Disco", disco.valor, disco.unidade])


print("\nMétricas salvas no arquivo metricas.csv")