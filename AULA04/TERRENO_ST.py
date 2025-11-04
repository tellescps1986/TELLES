import streamlit as st

st.title("Problema Terreno")

# Entrada de dados
st.write("Digite a largura do terreno (em metros):")
largura = st.number_input("Largura (m):")

st.write("Dig. o comprimento do terreno (m):")
comprimento = st.number_input("Comprimento (m):")

st.write("Dig. o comprimento do terreno (m):")
valor_m2 = st.number_input("Valor do m² (R$)")

#Processamento de Dados
area = largura * comprimento
valor_terreno = area * valor_m2


#Saída de dados
st.write(f"A área do terreno é de {area} metros quadrados.")


st.write(f"O valor do terreno é de R$: {valor_terreno} metros quadrados.")#Processamento de Dados
area = largura * comprimento

