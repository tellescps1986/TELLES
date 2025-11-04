import streamlit as st 

st.title("Problema Terreno")

# Entrada de dados
st.write("Digite o comprimento do retângulo")
comprimento = st.number_input("Comprimento (m):")

st.write("Digite o comprimento do retângulo")
altura = st.number_input("Comprimento (m):")

#Processamento de Dados
area = comprimento * altura

#Saída de dados
st.write(f"A área do terreno é de: {area}.")