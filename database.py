import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=3300,
    user="root",
    passwd="root"
)

print(db)