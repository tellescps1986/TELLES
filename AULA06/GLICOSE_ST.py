import streamlit as st
import math as mt

st.title("Classificação de níveis de glicose no sangue")
st.markdown(
    """
    | Nível de glicose |  Classificação  |
    |------------------|-----------------|
    |      0 -  70     |  Hipoglicêmica  |
    |     71 - 100     |     Normal      |
    |    101 - 140     |  Pré-diabetes   |
    |    141 ou mais   |    Diabetes     |
    """)

#Entrada de Dados
glicose = st.number_input("Insira o nível de glicose no sangue (mg/dL):", min_value=0)

# Processamento de Dados
if st.button("Classificar"): # Botão para classificar o nível de glicose
    if glicose <= 70:
        classificacao = "Hipoglicemia"
    elif glicose <= 100:
        classificacao = "Glicemia Normal"
        st.balloons()
    elif glicose <=140:
        classificacao = "Pré-Diabetes"
    else:
        classificacao ="Diabetes"
        st.balloons()

    st.write(f"{classificacao}")


