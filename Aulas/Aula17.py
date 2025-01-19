
import streamlit as st
import pandas as pd

# Configuração de página pra usar a página toda
st.set_page_config(layout='wide')

st.title("Aula 17 - St.columns")
st.subheader('Com Luciano Borba')


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.text_input("Coloque seu nome")

with col2:
    st.text_input("Coloque seu email")

with col3:
    st.number_input("Coloque seu nome", step=1)

with col4:
    st.number_input("Coloque endereço", step=1)

# Se quiser usar a coluna
st.text_area("Justifique pq devo lhe contratar")

# Butão de enviar, falta a logica pra enviar pra alguma lugar
st.button("Enviar")
