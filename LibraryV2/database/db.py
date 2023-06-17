import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yarte123700",
    database="library_v2"
)

cursor = connection.cursor(False)


