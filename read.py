# -*- encoding: utf-8 -*-

import mysql.connector


# Cria a conexão com o DB
connection = mysql.connector.connect(
    host='seu_host',
    port=0,  # digite o número correto da porta
    user='seu_usuario',
    password='sua_senha',
    database='teste'
)

# Cria o cursor para executar as querys
cursor = connection.cursor()

# Query a ser executada
sql = "SELECT * FROM users;"

# Executa as querys e lê todas as linhas
cursor.execute(sql)
results = cursor.fetchall()

# Fecha o cursor e a conexão
cursor.close()
connection.close()

for result in results:
    print(result)
