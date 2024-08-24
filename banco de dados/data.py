import mysql.connector


meudb = mysql.connector.connect(
    
  host="localhost",
  user="root",
  password="colares9187",
  database="AGENDA"
)

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
         
cklneslclk