import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

col1, col2 = st.columns([3, 1])

with col1:
    st.title('Gerenciador de atividades pessoal')

with col2:

    st.image('dashboard\images\lista-de-tarefas.png', width=100)

st.subheader('Atividades')

st.write('Essas são as atividades que você deve fazer! :)')


st.header("Topico 1")


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
    consulta = "SELECT * FROM atividades"
    df = pd.read_sql(consulta,conexao)
    conexao.close()
    return df

dados = obtemDados()

#st.dataframe(dados)





st.markdown("""
    <style>
    .card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
        width: 300px;
    }
    .card:hover {
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
    }
    .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    </style>
""", unsafe_allow_html=True)

dados['prazo'] = pd.to_datetime(dados['prazo'])

atividades = dados.sort_values(by='prazo')


st.markdown('<div class="container">', unsafe_allow_html=True)
for index, atividade in dados.iterrows():
    st.markdown(f"""
        <div class="card">
            <h4>{atividade['nome']}</h4>
            <p><strong>Prazo:</strong> {atividade['prazo']}</p>
            <p><strong>Prioridade:</strong> {atividade['tipo']}</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


