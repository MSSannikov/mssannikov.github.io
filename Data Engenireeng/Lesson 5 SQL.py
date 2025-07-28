import sqlite3 as sql

conn = sql.connect("Databasa.db")
cursor = conn.cursor()

#cursor.execute('''
#CREATE TABLE users (
#               name varchar(128),
#               lastname varchar(128)
#               )


#''')


def add_user(name, lastname):
    cursor.execute('''
    INSERT INTO users (
                name,
                lastname
                )
    VALUES (?, ?)


    ''', [name, lastname])

conn.commit()

add_user("Maksim", "Sannikov")

cursor.execute('SELECT * FROM users')

for row in cursor.fetchall():
    print(row)