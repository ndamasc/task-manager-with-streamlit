import mysql.connector


meudb = mysql.connector.connect(
    
  host="localhost",
  user="root",
  password="colares9187",
  database="AGENDA"
)

def criaBD():

    mycursor = meudb.cursor()
    mycursor.execute("CREATE DATABASE AGENDA")
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)


def criaTabela():
    mycursor = meudb.cursor()
    mycursor.execute("CREATE TABLE atividades (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), prazo DATE, tipo VARCHAR(255) )")



def alteraTabela():
    
    mycursor = meudb.cursor()
    mycursor.execute("ALTER TABLE atividades ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    

atv = input("Nome da atividade: ")
tempo = input("DUE DATE   ex:30-08-2024  ")
tip = input("Relevância:   ALTA/MEDIO/BAIXA   ")
 
def insereDados(atv,tempo, tip):
    
    mycursor = meudb.cursor()
    #mycursor.execute("INSERT INTO atividades (nome, prazo, tipo) VALUES (%s, %s, %s)")
    #valor = (atv, tempo, tip)
    
    sql = "INSERT INTO atividades (nome, prazo, tipo) VALUES (%s, %s, %s)"
    valor = (atv, tempo, tip)
    mycursor.execute(sql, valor)
    meudb.commit()
    
    
def insereVariosDados():
    
    mycursor = meudb.cursor()
    sql = "INSERT INTO atividades (nome ,prazo, tipo) VALUES (%s, %s, %s)"
    val = [
        ('estudar SQL', '01/05/25'),
        ('estudar docker', '09/10/24'),
        ('estudar C', '01/11/24'),
        ('estudar React', '01/09/24'),
        ('estudar para o mestrado', '01/02/25'),
        ('estudar linux', '31/08/24')
    ]
    
    mycursor.executemany(sql, val)
    print(mycursor.rowcount, " was inserted!")
         

 
 
insereDados(atv,tempo,tip)
    
#criaTabela()