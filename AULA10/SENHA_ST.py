import streamlit as st

#Problemas senha fixa
st.title("Sistema de log simples")

#Declaração de Constantes

#Credenciais
USUARIO ="Telles"
SENHA = "mortadela1"

usuario_entrada = st.text_input("Nome do Usuário: ")
senha_entrada = st.text_input("Senha: ", type="password")   

botao = st.button("Logar")

#Teste de Entradas
MAXIMO_TENTATIVAS = 3

if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0

if botao is True:
    if st.session_state.tentativas >= MAXIMO_TENTATIVAS:
        st.error("Limite de Tentativas Atingida. Acesso Bloqueado!")
    else:
        #Estrutura de Controle em Loop
        while st.session_state.tentativas < MAXIMO_TENTATIVAS:
            if usuario_entrada == usuario_entrada and senha_entrada == SENHA:
                st.success("Usuário logado!")
                st.session_state.tentativas = 0
                break
            else:
                st.session_state.tentativas +=1
                st.warning(f"Credenciais Inválidas. Tentativa {st.session_state.tentativas} de {MAXIMO_TENTATIVAS}")
                break