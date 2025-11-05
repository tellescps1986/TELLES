import streamlit as st 
import math as mt



TITULO=("CALCULADORA DE DURAÇÃO DE TEMPO")

st.set_page_config(page_title=TITULO)
st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)

#Entrada de Dados
segundos = st.number_input("Digite o tempo em segundos: ", min_value=0, step=1, help="Insira o valor total em segundos, para converção em horas, minutos e segundos")

#Processamento de Dados
horas   = segundos / 3600
minutos = segundos / 60

#Saída de Dados
st.markdown(f"<h2 style='text-align: left;'>Resultados: </h2>", unsafe_allow_html=True)
st.write(f"A quantidade de minutos digitados foi de: {minutos:.6f}.")
st.write(f"A quantidade de horas digitadas foi de: {horas:.6f}.")

st.write(f"{horas:.6f} horas, {minutos} minutos, e {segundos} segundos.")
