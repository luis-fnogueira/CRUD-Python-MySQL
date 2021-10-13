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

sql = "SELECT * FROM users;"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
    print(result)
