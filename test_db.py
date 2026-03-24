import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",   # use your correct password
    database="attendance_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM attendance")

rows = cursor.fetchall()

for row in rows:
    print(row)