import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user='root',
    password='test'
    )
cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE IF NOT EXISTS test_django_db')

print("ALL DONE !!!")