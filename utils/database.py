from typing import List, Tuple
from utils.database_connection import DatabaseConnection


Book=Tuple[int,str,str,int]

def create_book_table()-> None :
    with DatabaseConnection('data.db') as dbConnection :
        cursor = dbConnection.cursor() #objet used for manipulating the result set database
        #with if not exist let us to remove the problem in case of duplicatomg tables ignoring the errors
        cursor.execute('CREATE TABLE IF NOT EXISTS books (id integer primary key, name text, author text, read integer default 0)')

def delete_book(name: str)-> None :
    with DatabaseConnection('data.db') as dbConnection :
        cursor = dbConnection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?',(name,))

def mark_book_as_read(name: str)-> None :
    with DatabaseConnection('data.db') as dbConnection:
        cursor = dbConnection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))

def insert_book(name: str,author: str)-> None :
    with DatabaseConnection('data.db') as dbConnection :
        cursor = dbConnection.cursor()
        cursor.execute('INSERT INTO books (name, author) VALUES (?, ?)',(name,author))

def get_all_books()->List[Book]:
    with DatabaseConnection('data.db') as dbConnection:
        cursor=dbConnection.cursor()
        cursor.execute('SELECT * from books')
        books=cursor.fetchall()
        #print(f'{books}')
    return books