# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

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
sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"

# Dados que serão inseridos
data = (
    'Primeiro usuário',
    'primeirousuario@teste.com.br',
    datetime.datetime.today()
)

# Executa as querys e inicia a transação
cursor.execute(sql, data)
connection.commit()

# Pega o último ID da tabela
userid = cursor.lastrowid

# Fecha o cursor e termina a transação
cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID: ", userid)
