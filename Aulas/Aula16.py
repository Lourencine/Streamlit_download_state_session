
import streamlit as st
import pandas as pd


st.title("Aula 16 - Função tabs")
st.subheader('Com Luciano Borba')

tab1, tab2, tab3, tab4 = st.tabs(
    ['Modelagem de Dados', 'SQL', 'Python', 'Power BI'])

with tab1:
    st.header('Modelagem de Dados')
    st.subheader(' É importante de começar pela base!')

with tab2:
    st.header('SQL')
    st.subheader(' É importante que Python para área de Dados!')

with tab3:
    st.header('Python')
    st.subheader(' É importante para área de Dados!')

with tab4:
    st.header('Power BI')
    st.subheader(' É para Visualização de Dados!')
