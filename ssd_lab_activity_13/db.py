import sqlite3  
conn = sqlite3.connect('database.db')  


conn.execute('''CREATE TABLE User
       (ID INT PRIMARY KEY     NOT NULL, 
       NAME           TEXT    NOT NULL, 
       EMAIL            TEXT     NOT NULL, 
       PASSWORD        TEXT NOT NULL);''')

conn.close()
