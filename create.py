# -*- encoding: utf-8 -*-

import mysql.connector
import datetime


connection = mysql.connector.connect(
    host='localhost',
    port=3308,
    user='root',
    password='',
    database='teste'
)

cursor = connection.cursor()

sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
    'Primeiro usuário',
    'primeirousuario@teste.com.br',
    datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID: ", userid)
