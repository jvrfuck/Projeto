import mysql.connector
from mysql.connector import Error


# def criar_conexao(host, usuario, password, banco):
#     return mysql.connector.connect(host=host, usuer=usuario, password=password, database=banco)


# def fechar_conexao(con):
#     return con.close()


connection = mysql.connector.connect(host="jdbc:mysql://localhost:3306",
                                     user="<root>",
                                     passwd="<doug>",
                                     db="<projeto_entra21_db>"
                                     )

try:
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        db = cursor.fetchone()
        print("Você está conectado ao banco de dados: ", db)
except Error as e:
    print("Erro ao conectar ao MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("A conexão MySQL está fechada")
