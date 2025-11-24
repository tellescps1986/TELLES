import streamlit as st
import nome_idadeOPP as p

st.title("Nome e Idade")

# ---- Divisão da Tela ----
col1, col2 = st.columns(2)

# ----------------- COLUNA ESQUERDA -----------------
with col1:
    st.header("Cadastro de Pessoas")

    nome1 = st.text_input("Nome da primeira pessoa:", key="nome1")
    idade1 = st.number_input("Idade da primeira pessoa:", key="idade1", step=1, min_value=0)

    nome2 = st.text_input("Nome da segunda pessoa:", key="nome2")
    idade2 = st.number_input("Idade da segunda pessoa:", key="idade2", step=1, min_value=0)

    botao = st.button("Calcular", key="btn_calcular1")

    if botao:
        ps = p.Nome_Idade(nome1, nome2, idade1, idade2)
        st.success(ps.pessoaMaisVelha())


# ----------------- COLUNA DIREITA -----------------
with col2:
    st.header("Cadastro de Pessoas")

    nome1 = st.text_input("Nome da primeira pessoa:", key="nome3")
    salario1 = st.number_input("O salário da primeira pessoa", key="salario1", step=1, min_value=0)

    nome2 = st.text_input("Nome da segunda pessoa:", key="nome4")
    salario2 = st.number_input("O salário da segunda pessoa", key="salário2", step=1, min_value=0)

    botao = st.button("Calcular", key="btn_calcular2")

    if botao:
        ps = p.Nome_Salario(nome1, nome2, salario1, salario2)
        st.success(ps.mediaSalario())
