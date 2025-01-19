
import streamlit as st
import pandas as pd

# Configuração de página pra usar a página toda
st.set_page_config(layout='wide')

st.title("Cadastro de Visitas")
st.subheader('Visitas Gerador de Demanda')


col1, col2, col3, col4 = st.columns(4)

with col1:
    select = st.multiselect('Selecione o cliente', ("ATAKAREJO", "ASSAI", "REDEMIX", "NOVO MIX"))
    st.write(f' Cliente selecionado')

with col2:
    select = st.multiselect('Selecione o Produto', ("QUEIJO", "MANTEIGA", "CARNE", "PÃO"))
    st.write(f' Cliente selecionado')

with col3:
    st.number_input("Informe a Quantidade de Produtos", step=1)


# Se quiser usar a coluna
st.text_area("Informações da Visita")

# Butão de enviar, falta a logica pra enviar pra alguma lugar
st.button("Enviar")
