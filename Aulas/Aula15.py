
import streamlit as st
import pandas as pd


st.set_page_config(page_title="Download and State Session", layout="wide")


# Criação de formulario
with st.form('form_pessoa'):
    nome = st.text_input('Nome: ')
    idade = st.slider('Idade, ', 0, 120)
    cargo = st.text_input('Cargo: ')

# Criação de butão para enviar dados para o dateframe
    if st.form_submit_button('Enviar dados'):
        if 'data' not in st.session_state:
            # dateframe criado vazio
            st.session_state.data = pd.DataFrame(
                columns=['nome', 'idade', 'cargo'])
        # dados enviado para o dateframe
        dados = {'nome': nome, 'idade': idade, 'cargo': cargo}
        df = pd.DataFrame(dados, index=[0])
        st.session_state.data = pd.concat(
            [st.session_state.data, df], ignore_index=True)
        st.success("Funcionário cadastrdado com sucess!!!!")

# dados salvos no dateframe
st.write('## Lista de Funcionários')
if 'data' in st.session_state:
    st.write(st.session_state.data)

# Botão de doawload
st.write("Download")
if 'data' in st.session_state:
    st.download_button("Download", st.session_state.data.to_excel(
        "Downloads", index=False, engine='openpyxl'), "data.xlsx", mime="texte/xlsx")
