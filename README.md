# Trabalho Computacional de Sinais e Sistemas

_Trabalho desenvolvido para a disciplina **SEL0383** - 2º semestre/2024_

**Autores:**  
- Henrique de Oliveira Araujo - 13863950  
- Gabriela Passos de Andrade - 12625142

---

## Resumo

Este trabalho tem como objetivo desenvolver uma aplicação computacional para a aproximação retangular de sinais, permitindo a interação do usuário por meio de uma interface intuitiva. O projeto foi desenvolvido em **Python** utilizando as bibliotecas [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [IPyWidgets](https://ipywidgets.readthedocs.io/en/latest/) e [IPython Display](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html). Os resultados permitem visualizar a aproximação retangular discreta de funções matemáticas definidas pelo usuário.

---

## Desenvolvimento

O código foi desenvolvido em **Python** e estruturado para permitir a interação do usuário com o sistema. As principais seções do código são:

1. **Interface do Usuário:**  
   - Campos de entrada para a função definida pelo usuário.  
   - Controle deslizante para a quantidade de pontos de aproximação retangular.  
   - Botão para geração da animação.

2. **Animação da Aproximação Retangular:**  
   - Exibição em tempo real do processo de aproximação retangular.  
   - Demonstração do efeito do aumento do número de pontos na qualidade da aproximação.



## Resultado

### 1. Interface de Entrada de Dados

A interface permite que o usuário insira a função desejada e selecione a quantidade de pontos para a aproximação retangular. A seguir, um exemplo visual da tela de entrada de dados:

![GIF 1: Input visual dos dados](caminho/para/gif1.gif)

### 2. Aproximação Retangular de Sinal

Neste exemplo, a função `Sin(x) / x` é aproximada utilizando 100 pontos. À medida que o número de pontos aumenta, a aproximação retangular do sinal melhora continuamente até atingir o limite definido.

![GIF 2: Aproximação retangular do sinal](caminho/para/gif2.gif)
