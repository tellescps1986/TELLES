from streamlit import header, write, text_input, button, warning, success, error
from math import sqrt, pow

#Criação de Função em Python
def calculo(delta):
    valor = (sqrt(delta)) / (2 * a)
    return valor


header('Cálculo Bháskara')
write("Calculadora de raízes de uma equação de segundo grau")
write("ax² + bx + c")

# Entrada de dados
a = text_input('Digite o valor de a:', icon='🍦')#ícone WINDOWNS + .
b = text_input('Digite o valor de b:')
c = text_input('Digite o valor de c:')

# Processamento de dados
if button('Calcular raízes'):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        delta = pow(b, 2) - 4 * a * c
        write(f"Δ = {delta:.4f}")

        if delta < 0:
            warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = (-b + calculo(delta))
            success(f"A equação possui uma raiz real: {raiz:.4f}")
        else:
            raiz1 = (-b + calculo(delta))
            raiz2 = (-b - calculo(delta))
            success(f"As raízes da equação são:\n\n"
                       f"X' : {raiz1:.4f}\n\n"
                       f"X'': {raiz2:.4f}")
    except ValueError:
        error("Por favor, insira valores válidos para a, b e c.")
    except ZeroDivisionError:
        error("O valor do denominador do Δ não pode ser zero")
