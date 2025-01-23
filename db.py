import mysql.connector
import settings

# Connected to database
connection = mysql.connector.connect(
    user=settings.user,
    password=settings.password
)

cursor = connection.cursor()    
cursor.execute("CREATE DATABASE IF NOT EXISTS Homework") # Created database
cursor.execute("USE Homework") # Homework is used
# connection.commit()  # U can use it to store new tables to mysql database

# Book table is created
def create_books_table(cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS Books ( id INT AUTO_INCREMENT PRIMARY KEY, title  VARCHAR(128),author VARCHAR(128),published_year INT,genre VARCHAR(64),price FLOAT,available BOOL)")
        print("Books table created successfully!")
    except:
        print("\nThis table is available!!!")

# Adding new books 
def insert_book(title, author, published_year, genre, price, available):
    

    cursor.execute("""INSERT INTO Books (title, author, published_year, genre, price, available) VALUES(%s, %s, %s, %s, %s, %s)""", 
                   (title, author, published_year, genre, float(price), bool(available)))
    print("\nBook added successfully!")

# Seeing all books infos
def show_all_books(cursor):
    cursor.execute("SELECT id, title, author, published_year, genre, price, IF(available, 'True', 'False') FROM Books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        

# Cheking book by category and value   
def search_books_by_author_or_genre(cursor, search_type, search_value):
    cursor.execute(f"SELECT * FROM Books WHERE { 'genre' if search_type == "1" else 'author' } = %s", (search_value,))
    rows = cursor.fetchall()
    
    w = 0
    for row in rows:
        w = 1
        print(row)

    if w == 0:
        print("\nValue is not found!!!")

# Updating the price of book        
def update_book_price(cursor, book_id, new_price):
    cursor.execute("UPDATE Books SET price = %s WHERE id = %s", (new_price, book_id))
    if cursor.rowcount > 0:
        print("\nPrice changed successfully!")
    else:
        print("\nId is not found!!!")
        
        
# Updating avaibality of books    
def update_book_availability(cursor, book_id, availability):
    cursor.execute("UPDATE Books SET available = %s WHERE id = %s ", (availability, book_id))
    

# Deleting unnecessery book
def delete_book(cursor, book_id):
    cursor.execute(f"DELETE FROM Books WHERE id = {book_id}")
    if cursor.rowcount > 0:
        print("\nBook deleted successfully!")
    else:
        print("\nBook is not found!!!")


# Sorting books by year
def sort_books_by_year(cursor, order):

    cursor.execute(f"SELECT * FROM Books ORDER BY published_year {'ASC' if order == "1" else 'DESC'}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Counting books
def count_books(cursor):
    cursor.execute("SELECT COUNT(title) FROM Books")
    rows = cursor.fetchall()
    print("\nAll books: ")
    for row in rows:
        print(row)
    

# Seeeing max, min and average of prices    
def price_statistics(cursor):
    cursor.execute("SELECT MAX(price) FROM Books")
    max_price = cursor.fetchall()
    print(f"Maximum price is {max_price[0][0]}")

    cursor.execute("SELECT MIN(price) FROM Books")
    min_price = cursor.fetchall()
    print(f"Minimum price is {min_price[0][0]}")
    
    cursor.execute("SELECT AVG(price) FROM Books")
    avg_price = cursor.fetchall()
    print(f"Average price is {avg_price[0][0]}")
    
n = 1
while n != 0:
    pass
    print("\nCreate table - 1",
          "Insert a new book - 2",
          "Show all books - 3",
          "Search books by author or genre - 4",
          "Update book price - 5",
          "Update book availability - 6",
          "Delete book - 7",
          "Sorting by year - 8",
          "Count books - 9",
          "Price statistics - 10",
          "Exit - 0", sep="\n")
    
    n = int(input("Your choice-> "))
    
    if n == 1:
        create_books_table(cursor)
        
    elif n == 2:
        title = input("\nEnter title: ")
        author = input("Enter author: ")
        year = int(input("Enter published year: "))
        genre = input("Enter genre: ")
        price = input("Enter price: ")
        
        count_ava = 0
        while count_ava != 1:
            print("Enter true if available else enter false : ", end="")
            availability = input("Available (True/False): ").capitalize()
            if availability == "True":
                count_ava = 1
                availability = True
            elif availability == "False":
                count_ava = 1
                availability = False
            else:
                print("Invalid command!!!")
              
        insert_book(title=title,author=author,published_year= year, genre = genre, price= price, available= availability)
        
    elif n == 3:
        show_all_books(cursor)
        
    elif n == 4:
        count_type = 0
        
        while count_type != 1:
            search_type = input("\nEnter 1 for genre or 2 for author: ")
            if search_type == "1":
                count_type = 1
            elif search_type == "2":
                count_type = 1
            else: 
                count_type = 0
                print("\nWrong number!!!")
                
        search_value = input("Enter value: ")
            
        search_books_by_author_or_genre(cursor, search_type, search_value)
    
    elif n == 5:
        book_id = int(input("\nEnter book id: "))
        new_price = int(input("Enter new price: "))
        update_book_price(cursor, book_id, new_price)
        
    elif n == 6:
        books_id = int(input("\nEnter book id: "))
        available = input("If available enter 1 else enter other number: ")
        if available == "1":
            available = True
        else:
            available = False
        
        update_book_availability(cursor, books_id, available)
    
    elif n == 7:
        book_id = int(input("\nEnter book id: "))
        delete_book(cursor, book_id)
        
    elif n == 8:
        order_by = input("\nTo Order by ASC enter 1 or for DESC enter 2: ")
        
        i = 0
        while i != 1:
            if order_by == "1":
                i = 1
            elif order_by == "2":
                i = 1
            else:
                print("You can write 1 or 2 !!!")
            
        sort_books_by_year(cursor, order_by)
        
    elif n == 9:
        count_books(cursor)
        
    elif n == 10:
        price_statistics(cursor)

if n == 0:
    print("Exiting...")
    
connection.close()