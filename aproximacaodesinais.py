import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

rc('animation', html='jshtml')

x_continuous = np.linspace(-10, 10, 1000)
y_continuous = np.sin(x_continuous) / x_continuous
y_continuous[np.isnan(y_continuous)] = 1

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x_continuous, y_continuous, color='red', label='Função Contínua (sin(x)/x)')

initial_points = 10
x_discrete = np.linspace(-10, 10, initial_points)
y_discrete = np.sin(x_discrete) / x_discrete
y_discrete[np.isnan(y_discrete)] = 1

plot, = ax.step(x_discrete, y_discrete, where='mid', color='blue', label='Aproximação Discreta')

ax.set_xlabel('x')
ax.set_ylabel('sin(x)/x')
ax.set_title('Aproximação com Variação do Número de Pontos Discretos')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

def iteration(frame):
    points = 10 + frame
    x_discrete = np.linspace(-10, 10, points)
    y_discrete = np.sin(x_discrete) / x_discrete
    y_discrete[np.isnan(y_discrete)] = 1
    plot.set_xdata(x_discrete)
    plot.set_ydata(y_discrete)
    return plot,

N = 50
animation.FuncAnimation(fig, iteration, frames=N, blit=False, repeat=True)


