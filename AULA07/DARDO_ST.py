import streamlit as st

st.title("🎯 Simulação de Lançamento de Dardos 🎯")
'''
O objetivo do aplicativo é mostrar o dardo com maior distância.
'''

#Entrada de Dados
st.header("Inserir as três distânicas dos dados lançados pelo jogador.")

coluna1, coluna2, coluna3 = st.columns(3)


with coluna1:
    dardo1 = st.number_input("Distância do 1º dardo", step=1, min_value=0)

with coluna2:
    dardo2 = st.number_input("Distância do 2º dardo", step=1, min_value=0)

with coluna3:
    dardo3 = st.number_input("Distância do 3º dardo", step=1, min_value=0)

#Estrutura de Controle
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "Dardo 1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo 2"
else:
    dardo_vencedor = "Dardo 3"

if st.button ("Apresentar resultados de lançamento"):
    st.write(f"O dardo com a maior distância é: {dardo_vencedor}")
