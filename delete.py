# -*- encoding: utf-8 -*-

import mysql.connector

connection = mysql.connector.connect(
    host='seu_host',
    port=0,  # digite o número correto da porta
    user='seu_usuario',
    password='sua_senha',
    database='teste'
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (2,)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, "registros excluídos")
