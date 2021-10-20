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
sql = "DELETE FROM users WHERE id = %s"

# ID que será deletado
data = (2,)

# Executa as querys e inicia a transação
cursor.execute(sql, data)
connection.commit()

# Variável para identificar quantas linhas foram afetadas
recordsaffected = cursor.rowcount

# Fecha o cursor e termina a transação
cursor.close()
connection.close()

print(recordsaffected, "registros excluídos")
