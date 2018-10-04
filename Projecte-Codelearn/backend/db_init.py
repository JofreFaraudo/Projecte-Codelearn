import sqlite3
conn = sqlite3.connect("todos.db")
c = conn.cursor()
a = c.execute('''CREATE TABLE todos (id INTEGER primary key, desc BOOL, fet BOOl)''')
