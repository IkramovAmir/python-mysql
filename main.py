import mysql.connector
import settings

connection = mysql.connector.connect(
    host=settings.host,
    user=settings.user,
    password=settings.password,
    port=settings.port,
    # database=settings.db_name
)

cursor = connection.cursor()

cursor.execute("USE shop")

cursor.execute('''
CREATE TABLE IF NOT EXISTS hodimlar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64),
    department VARCHAR(128),
    locaiton TEXT
)
''')

# cursor.execute("SHOW TABLES")

rows = cursor.fetchall()

print(rows)

cursor.close()
connection.close()


# educaiton db
# students table (id, name, grade, age)
# 10 students
# select all
# filter age increasing


cursor = connection.cursor()

cursor.execute("create ")