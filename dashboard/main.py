import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

import base64

col1, col2 = st.columns([3, 1])

with col1:
    st.title('Gerenciador de atividades pessoal')

with col2:

    st.image('images\lista-de-tarefas.png', width=100)


st.write('Essas são as atividades que você deve fazer! :)')


def conectaBanco():
    conexao = mysql.connector.connect(
        
    host="localhost",
    user="root",
    password="colares9187",
    database="AGENDA"
    )
    
    return conexao

def obtemDados():
    conexao = conectaBanco()
    consulta = "SELECT nome, prazo, tipo FROM atividades"
    df = pd.read_sql(consulta,conexao)
    conexao.close()
    return df

dados = obtemDados()

#st.dataframe(dados)

def insereDados(nome, prazo, tipo):
    conexao = conectaBanco()
    cursor = conexao.cursor()
    consulta = "INSERT INTO atividades (nome, prazo, tipo) VALUES (%s, %s, %s)"
    valores = (nome, prazo, tipo)
    cursor.execute(consulta, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def main():

    st.header("Adicionar Nova Atividade")
    with st.form(key='form_add'):
        nome = st.text_input("Nome da Atividade")
        prazo = st.date_input("Prazo")
        tipo = st.selectbox("Prioridade", ["Importante", "Media", "Normal"])
        submit_button = st.form_submit_button(label='Adicionar')

        if submit_button:
            insereDados(nome, prazo, tipo)
            st.success("Atividade adicionada com sucesso!")



##########################          TAREFAS COM ENTREGA PROXIMA  


def  dataCrescente():
    conexao = conectaBanco()
    consulta = "SELECT * FROM atividades ORDER BY prazo ASC"
    df = pd.read_sql(consulta,conexao)
    conexao.close()
    return df
    
data = dataCrescente()


st.header("Tarefas com due date próximo")
#st.dataframe(data)                  #se quiser ver em formato de tabela

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.markdown("""
    <style>
    .container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);

    }
    .card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
        width: calc(33.333% - 20px);  /* Ocupa 1/3 da linha */
        box-sizing: border-box;
    }
    .card:hover {
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
    }
    .img {
        width: 30px;  /* Ajusta o tamanho da imagem */
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Exibição dos cartões
st.markdown('<div class="container">', unsafe_allow_html=True)
for index, atividade1 in data.iterrows():
    img_html = ''
    if atividade1['tipo'] == 'Importante':
        caminho_img = "images/sirene.png"
        img_base64 = get_img_as_base64(caminho_img)
        img_html = f'<img src="data:image/png;base64,{img_base64}" class="img">'  # Adiciona a classe img para a imagem
    
    st.markdown(f"""
        <div class="card">
            <div>{img_html}</div>
            <h4>{atividade1['nome']}</h4>
            <p><strong>Prazo:</strong> {atividade1['prazo']}</p>
            <p><strong>Prioridade:</strong> {atividade1['tipo']}</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)




##########################


#st.markdown("""
#    <style>
#    .card {
#        background-color: #f0f2f6;
#        border-radius: 10px;
#        padding: 20px;
#        margin: 10px;
#        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#        transition: 0.3s;
#        width: 300px;
#    }
#    .card:hover {
#        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
#    }
#    .container {
#        display: flex;
#        flex-wrap: wrap;
#        justify-content: space-between;
#    }
#    </style>
#""", unsafe_allow_html=True)


#st.markdown('<div class="container">', unsafe_allow_html=True)
#for index, atividade in dados.iterrows():
#    if atividade['tipo'] == 'Importante':
#        caminho_img = "images\sirene.png"
#        img_html = f'<img src= "data:image/png;base64,{st.image(caminho_img, width=30)}">' 
#        
#    st.markdown(f"""
#        <div class="card">
#            <h4>{atividade['nome']}</h4>
#            <p><strong>Prazo:</strong> {atividade['prazo']}</p>
#            <p><strong>Prioridade:</strong> {atividade['tipo']}</p>
#        </div>
#    """, unsafe_allow_html=True)
#st.markdown('</div>', unsafe_allow_html=True)

