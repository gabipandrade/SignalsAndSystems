# Henrique de Oliveira Araujo - 13863950
# Gabriela Passos de Andrade - 12625142

# Trabalho de Sinais e Sistemas - SEL0383/SEL0604 - 2º semestre/2024
# Este código tem como objetivo a aproximação de sinais, conforme descrito no trabalho computacional da disciplina de Sinais e Sistemas.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
import ipywidgets as widgets
from IPython.display import display, clear_output
import time  # Para forçar o tempo de espera

# Dicionário para disponibilizar as funções NumPy para uso em expressões de entrada do usuário
available_functions = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'exp': np.exp,
    'log': np.log,
    'sqrt': np.sqrt,
    'abs': np.abs,
    'pi': np.pi
}

# Configuração para que a animação seja exibida no formato HTML
rc('animation', html='jshtml')

# Configuração para ignorar warnings de divisão por zero e operações inválidas
np.seterr(divide='ignore', invalid='ignore')

# Função para avaliar a expressão inserida pelo usuário
# Recebe a string da função e o vetor x para calcular y
# Retorna os valores de y correspondentes a x

def evaluate_function(func_str, x):
    try:
        y = eval(func_str, {"__builtins__": None}, {**available_functions, 'x': x})
        y = np.nan_to_num(y)  # Substitui NaN e inf por 0
        return y
    except Exception as e:
        print(f"Erro ao avaliar a função: {e}")
        return np.zeros_like(x)

# Função para atualizar os dados da animação
# Calcula os novos pontos x e y e atualiza o gráfico

def update_animation(frame, plot, func_str, max_points):
    points = 5 + frame  # Aumenta de 5 até o máximo escolhido no slider
    if points > max_points:
        points = max_points  # Garante que não ultrapassa o máximo
    x_discrete = np.linspace(-10, 10, points)
    y_discrete = evaluate_function(func_str, x_discrete)
    plot.set_xdata(x_discrete)
    plot.set_ydata(y_discrete)
    return plot,

# Função principal para criar a animação
# Plota a função contínua e a aproximação discreta

def create_animation(func_str, max_points, status_label):
    x_continuous = np.linspace(-10, 10, 1000)
    y_continuous = evaluate_function(func_str, x_continuous)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Plotar a função contínua
    ax.plot(x_continuous, y_continuous, color='red', label=f'Função Contínua: {func_str}')
    
    # Configuração inicial dos pontos discretos
    x_discrete = np.linspace(-10, 10, 5)
    y_discrete = evaluate_function(func_str, x_discrete)
    plot, = ax.step(x_discrete, y_discrete, where='mid', color='blue', label='Aproximação Discreta')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y(x)')
    ax.set_title(f'Aproximação de {func_str} com Pontos Discretos')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()

    ani = animation.FuncAnimation(fig, update_animation, frames=max_points-5, fargs=(plot, func_str, max_points), blit=False, repeat=True)
    plt.close(fig)  # Fecha a figura para evitar duplicação
    return ani

# Função para atualizar a visualização quando o usuário interagir
# Exibe a interface para o usuário inserir os parâmetros da função

def on_button_click(_):
    clear_output(wait=True)
    display(ui)  # Exibe novamente a interface completa
    func_str = func_input.value
    max_points = points_slider.value
    
    status_label.value = "O gráfico está sendo gerado, aguarde um momento!\nTempo de carregamento: 8 - 20 segundos"
    time.sleep(0.1)  # Garantir que a mensagem seja exibida antes do cálculo começar
    
    ani = create_animation(func_str, max_points, status_label)
    display(ani)

# Widgets interativos para entrada de dados
# Campo de texto para a função do usuário
func_input = widgets.Text(
    value='sin(x) / x',
    placeholder='Digite a função aqui (ex: sin(x), cos(x), exp(-x), etc.)',
    description='Função:',
    layout=widgets.Layout(width='400px')
)

# Slider para o número de pontos na aproximação
points_slider = widgets.IntSlider(
    value=50,
    min=10,
    max=100,
    step=1,
    description='Pontos:',
    layout=widgets.Layout(width='400px')
)

# Botão para gerar a animação
button = widgets.Button(
    description='Gerar Animação',
    button_style='success'
)

# Mensagem de status que informa o estado do gráfico
status_label = widgets.Label(value='')

# Conectar o evento do botão para executar a função on_button_click
button.on_click(on_button_click)

# Interface de usuário para entrada e controle de parâmetros
ui = widgets.VBox([func_input, points_slider, button, status_label])
display(ui)
