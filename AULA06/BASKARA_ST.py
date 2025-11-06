import streamlit as st
import math as mt

st.header('Cálculo Bháskara')
st.write("Calculadora de raízes de uma equação de segundo grau")
st.write("ax² + bx + c")

# Entrada de dados
a = st.text_input('Digite o valor de a:')
b = st.text_input('Digite o valor de b:')
c = st.text_input('Digite o valor de c:')

# Processamento de dados
if st.button('Calcular raízes'):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        delta = mt.pow(b, 2) - 4 * a * c
        st.write(f"Δ = {delta:.4f}")

        if delta < 0:
            st.warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = (-b + mt.sqrt(delta)) / (2 * a)
            st.success(f"A equação possui uma raiz real: {raiz:.4f}")
        else:
            raiz1 = (-b + mt.sqrt(delta)) / (2 * a)
            raiz2 = (-b - mt.sqrt(delta)) / (2 * a)
            st.success(f"As raízes da equação são:\n"
                       f"X': {raiz1:.4f}\n"
                       f"X'': {raiz2:.4f}")
    except:
        st.error("Por favor, insira valores válidos para a, b e c.")
