import streamlit as st 
import math as mt

TITULO=("Problema Retângulo")
st.title(TITULO)

# Entrada de dados
st.write("Digite o comprimento do retângulo")
comprimento = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")

st.write("Digite o comprimento do retângulo")
altura = st.number_input("Altura (m):", min_value=0.0, format="%.2f")

#Processamento de Dados
area = comprimento * altura
perimetro = 2*comprimento + 2*altura
#diagonal = (comprimento**2 + altura**2)**0.5
x = mt.pow(comprimento,2)+mt.pow(altura,2)
diagonal = mt.sqrt(x)

#Saída de dados
st.write(f"A área do terreno é de: {area:.2f}.")
st.write(f"O Perímetro é de: {perimetro:.2f}.")
st.write(f"O Perímetro é de: {diagonal:.2f}.")
