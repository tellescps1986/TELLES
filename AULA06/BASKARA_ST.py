from streamlit import header, write, text_input, button, warning, success, error
from math import sqrt, pow

header('Cálculo Bháskara')
write("Calculadora de raízes de uma equação de segundo grau")
write("ax² + bx + c")

# Entrada de dados
a = text_input('Digite o valor de a:')
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
            raiz = (-b + sqrt(delta)) / (2 * a)
            success(f"A equação possui uma raiz real: {raiz:.4f}")
        else:
            raiz1 = (-b + sqrt(delta)) / (2 * a)
            raiz2 = (-b - sqrt(delta)) / (2 * a)
            success(f"As raízes da equação são:\n"
                       f"X': {raiz1:.4f}\n"
                       f"X'': {raiz2:.4f}")
    except:
        error("Por favor, insira valores válidos para a, b e c.")
