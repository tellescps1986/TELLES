import streamlit as st 
import math as mt

TITULO=("TROCO DA MARCENARIA")

st.set_page_config(page_title=TITULO)
st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)

#Entrada de Dados
produto = st.number_input("Digite o valor do produtos: ", min_value=0.0, format="%.2f", help="Insira o valor total dos produtos.")
quantidade = st.number_input("Digite a quantidade de produtos comprados: ", min_value=0, help="Insira quantos produtos foram comprados.")
pagamento = st.number_input("Digite o montante pago: ", min_value=0.0, format="%.2f", help="Insira o valor recebido para o pagamento.")


#Processamento de Dados
troco = pagamento - (quantidade * produto)

#Saída de Dados
st.markdown(f"<h2 style='text-align: left;'>Resultados: </h2>", unsafe_allow_html=True)
st.write(f"Valor total da compra: {(quantidade*produto):.2f}.")
st.write(f"Paramento recevido {pagamento:.2f}.")
st.write(f"Troco a devolver {troco:.2f}.")
