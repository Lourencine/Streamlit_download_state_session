
import streamlit as st
import pandas as pd
import io  # Necessário para o buffer em memória

st.set_page_config(page_title="Download and State Session", layout="wide")

# Criação de formulário
with st.form('form_pessoa'):
    nome = st.text_input('Nome: ')
    idade = st.slider('Idade', 0, 120)
    cargo = st.text_input('Cargo: ')

    # Criação do botão para enviar dados para o DataFrame
    if st.form_submit_button('Enviar dados'):
        if 'data' not in st.session_state:
            # DataFrame criado vazio
            st.session_state.data = pd.DataFrame(
                columns=['nome', 'idade', 'cargo'])
        # Dados enviados para o DataFrame
        dados = {'nome': nome, 'idade': idade, 'cargo': cargo}
        df = pd.DataFrame(dados, index=[0])
        st.session_state.data = pd.concat(
            [st.session_state.data, df], ignore_index=True)
        st.success("Funcionário cadastrado com sucesso!")

# Dados salvos no DataFrame
st.write('## Lista de Funcionários')
if 'data' in st.session_state:
    st.write(st.session_state.data)

# Botão de download
st.write("Download")
if 'data' in st.session_state:
    # Criar um buffer de memória
    buffer = io.BytesIO()

    # Salvar os dados do DataFrame no buffer
    st.session_state.data.to_excel(buffer, index=False, engine='openpyxl')
    buffer.seek(0)  # Reiniciar o ponteiro do buffer para o início

    # Botão para baixar o arquivo Excel
    st.download_button(
        label="Download",
        data=buffer,
        file_name="data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
