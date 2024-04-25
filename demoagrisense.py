import random
import pandas as pd
import matplotlib.pyplot as plt

# Simulação de leitura de sensores
def read_temperature():
    return random.uniform(20, 40)

def read_soil_moisture():
    return random.uniform(0, 100)

# Simulação de 20 leituras
num_readings = 20
temperature_readings = [read_temperature() for _ in range(num_readings)]
soil_moisture_readings = [read_soil_moisture() for _ in range(num_readings)]

# Criar DataFrame com os dados
data = {'Temperatura (°C)': temperature_readings, 'Umidade do Solo (%)': soil_moisture_readings}
df = pd.DataFrame(data)

# Salvar os dados em um arquivo CSV
df.to_csv('agrisense_data.csv', index=False)

# Plotar gráficos
plt.figure(figsize=(10, 5))

# Gráfico de temperatura
plt.subplot(2, 1, 1)
plt.plot(temperature_readings, marker='o', color='blue')
plt.title('Leituras de Temperatura')
plt.xlabel('Leituras')
plt.ylabel('Temperatura (°C)')
plt.grid(True)

# Gráfico de umidade do solo
plt.subplot(2, 1, 2)
plt.plot(soil_moisture_readings, marker='o', color='green')
plt.title('Leituras de Umidade do Solo')
plt.xlabel('Leituras')
plt.ylabel('Umidade do Solo (%)')
plt.grid(True)

plt.tight_layout()
plt.show()

# Verificando alertas
for i in range(num_readings):
    if temperature_readings[i] > 35:
        print(f'ALERTA: Temperatura muito alta na leitura {i+1}!')
    if soil_moisture_readings[i] < 20:
        print(f'ALERTA: Umidade do solo muito baixa na leitura {i+1}!')
