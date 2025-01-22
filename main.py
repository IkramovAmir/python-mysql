import mysql.connector
import settings

connection = mysql.connector.connect(
    host=settings.host,
    user=settings.user,
    password=settings.password,
    port=settings.port
)

if connection.is_connected():
    print("mysql ga muvaffaqiyatli ulandik.")

cursor = connection.cursor()

cursor.execute("create ")