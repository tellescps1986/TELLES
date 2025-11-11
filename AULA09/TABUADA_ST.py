import streamlit as st

#Título da página
TITULO = "Tabuada"
st.title(TITULO)

st.set_page_config(TITULO)

#Entrada da Dados
n = None

try:
    n = int(st.text_input("Deseja a tabuada de qual número?"))
    for i in range(1,11):
        saida = f"{n} x {i} = {n*i}"
        st.markdown(f"""{saida}""")


except ValueError:
        if n == None:
            st.warning("Digite algum valor!")
        else:
                     st.error("Digite somente números!")

            
