import streamlit as st 
import math as mt

TITULO=("CÁLCULO DE ÁREA DE UM QUADRADO, TRIÂNGULO E TRAPÉZIO")
st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)

# Entrada de Dados
st.write("Digite a medida A")
medida_A = st.number_input("Medida A", min_value=0.0, format="%.2f")

st.write("Digite a medida B")
medida_B = st.number_input("Medida B", min_value=0.0, format="%.2f")

st.write("Digite a medida C")
medida_C = st.number_input("Medida C", min_value=0.0, format="%.2f")

# Processamento de Dados
area_do_quadrado = mt.pow(medida_A,2)

area_do_triangulo = (medida_A * medida_B)/2

area_do_trapezio = ((medida_A+medida_B)*medida_C)/2

# Saída de Dados
st.markdown(f"<h2 style='text-align: left;'>Resultados: </h2>", unsafe_allow_html=True)
st.write(f"A área do quadrado é de: {area_do_quadrado:.2f}.")
st.write(f"A área do triângulo é de: {area_do_triangulo:.2f}.")
st.write(f"A área do trapézio é de: {area_do_trapezio:.2f}.")



