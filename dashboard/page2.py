import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

import base64

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

    # Formulário para adicionar uma nova atividade
    st.header("Adicionar Nova Atividade")
    with st.form(key='form_add'):
        nome = st.text_input("Nome da Atividade")
        prazo = st.date_input("Prazo")
        tipo = st.selectbox("Prioridade", ["Importante","Média", "Normal"])
        submit_button = st.form_submit_button(label='Adicionar')

        if submit_button:
            insereDados(nome, prazo, tipo)
            st.success("Atividade adicionada com sucesso!")



if __name__ == "__main__":
    main()

