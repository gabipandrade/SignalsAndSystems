import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo contínuo para todos os gráficos
x_continuous = np.linspace(-10, 10, 1000)
y_continuous = np.sin(x_continuous) / x_continuous
y_continuous[np.isnan(y_continuous)] = 1  # Tratar o ponto x=0 para evitar divisão por zero

# Lista de quantidade de pontos para o linspace
points_list = [10, 30, 50, 70, 100]

# Criar a figura com 5 gráficos lado a lado
fig, axes = plt.subplots(1, 5, figsize=(20, 4))

# Loop para criar cada gráfico
for i, points in enumerate(points_list):
    x_discrete = np.linspace(-10, 10, points)
    y_discrete = np.sin(x_discrete) / x_discrete
    y_discrete[np.isnan(y_discrete)] = 1  # Tratar o ponto x=0 para evitar divisão por zero

    # Gráfico contínuo em vermelho
    axes[i].plot(x_continuous, y_continuous, color='red', label='Contínuo')

    # Gráfico discreto estilo "degrau" em azul
    axes[i].step(x_discrete, y_discrete, where='mid', color='blue', label='Aproximação Retangular')

    # Configurações do gráfico
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('sin(x)/x')
    axes[i].set_title(f'{points} Pontos')
    axes[i].grid(True, linestyle='--', alpha=0.6)

# Ajustar layout
plt.tight_layout()
plt.show()
