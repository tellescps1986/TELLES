import streamlit as st 

st.title("Problema Retângulo")

# Entrada de dados
st.write("Digite o comprimento do retângulo")
comprimento = st.number_input("Comprimento (m):")

st.write("Digite o comprimento do retângulo")
altura = st.number_input("Altura (m):")

#Processamento de Dados
area = comprimento * altura
perimetro = 2*comprimento + 2*altura
diagonal = (comprimento**2 + altura**2)**0.5

#Saída de dados
st.write(f"A área do terreno é de: {area}.")
st.write(f"O Perímetro é de: {perimetro}.")
st.write(f"O Perímetro é de: {diagonal}.")
