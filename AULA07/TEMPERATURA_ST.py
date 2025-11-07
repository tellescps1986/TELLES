import streamlit as st

def Celsius_Fahrenheit(temp):
    return ((temp * 1.8)+32)

def Celsius_Kelvin(temp):
    return (temp + 273.15)

def Fahrenheit_Celsius(temp):
    return ((temp - 32)*(5/9))

def Fahrenheit_Kelvin(temp):
    return(((temp - 32)*(5/9))+273.15)

def Kevin_Celsius(temp):
    return (temp - 273.15)

def Kevin_Fahrenheit(temp):
    return((temp - 273.15) * 1.8 + 32)


#Problema Temperatura
st.sidebar.title("Conversor de Temperatura")

st.title("Conversor de Temperatura")

st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")

celsius_selecionado = st.sidebar.checkbox("Celsius", key="temp_celsius")
fahrenheit_selecionado = st.sidebar.checkbox("Fahrenheit", key="temp_farenheit")
kelvin_selecionado = st.sidebar.checkbox("Kelvin", key="temp_kelvin")

#Entrada de Dados
temp = st.number_input("Valor da Temperatura", format="%2.f", step=0.5)

#Processamento de Dados
if st.button("Conveter", icon="🌡"):
    if celsius_selecionado:
        st.write(f"{temp}°C em {Celsius_Fahrenheit(temp):.2f}°F.")
        st.write(f"{temp}°C em {Celsius_Kelvin(temp):.2f}K.")

    if fahrenheit_selecionado:
        st.write(f"{temp}°F em {Fahrenheit_Celsius(temp):.2f}°C.")
        st.write(f"{temp}°F em {Fahrenheit_Kelvin(temp):.2f}K.")
    
    if kelvin_selecionado:
        st.write(f"{temp}K em {Kevin_Celsius(temp):.2f}°C.")
        st.write(f"{temp}K em {Kevin_Fahrenheit(temp):.2f}°F.")