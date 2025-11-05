import streamlit as st
import math as mt

st.header('Cálculo Bháskara')
st.write("Calculadora de raízes \n de uma equação de segundo grau")
st.write("ax² + bx + c")

#Entrada de dados
a = st.text_input('Digite o valor de a: ')
b = st.text_input('Digite o valor de b: ')
c = st.text_input('Digite o valor de c: ')

#Processamento de dados
if st.button('Calcular raízes'):
    
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        delta = mt.pow(b,2)-(4*a*c)
    
        if delta < 0:
            st.warning("A Equação não produz raízes reais.")

        elif delta == 0:
            raiz = (-b + mt.sqrt(delta) / (2*a))
            st.success(f"A Equação possui uma raíz real: {raiz}")

        else:
            raiz1 = (-b + mt.sqrt(delta) / (2*a))
            raiz2 = (-b - mt.sqrt(delta) / (2*a))
            st.raizes(f"As raízes da equação são: \n Raiz 1:{raiz1:.4f} \n Raiz 2:{raiz2:.4f}")


    except:
        st.error("Por favor insira valores válidos, para a, b e c.")


