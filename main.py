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


cursor.execute("create database if not exists education")
cursor.execute("Use education")
cursor.execute("create table if not exists student (id int auto_increment primary key, name varchar(128), grade varchar(12), age int)"
)

cursor.execute(""" insert into student (name, grade, age)
                   values ('amir', 'A', 19), ('lisa', 'B', 18), ('john', 'A', 20), 
                          ('sara', 'C', 19), ('ali', 'B', 21), ('emma', 'A', 20), 
                          ('ryan', 'B', 22), ('nina', 'C', 18), ('jack', 'A', 19), 
                          ('zara', 'B', 20)""")


cursor.execute("select * from student")
rows = cursor.fetchall()
for row in rows:
    print(row)
    

cursor.execute("select * from student order by age DESC")
ages = cursor.fetchall()
for age in ages:
    print(age)
    
cursor.close()
connection.close()










# cursor.execute('''
# CREATE TABLE IF NOT EXISTS hodimlar (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(64),
#     department VARCHAR(128),
#     locaiton TEXT
# )
# ''')



# print(rows)




# # educaiton db
# # students table (id, name, grade, age)
# # 10 students
# # select all
# # filter age increasing


# cursor = connection.cursor()

# cursor.execute("create ")