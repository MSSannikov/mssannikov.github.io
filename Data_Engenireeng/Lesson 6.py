import sqlite3 as sql

conn = sql.connect("Databasa.db")
cursor = conn.cursor()

def addproduct(title,price):
    cursor.execute('''
                   INSERT INTO products ("title", "price")
                   VALUES (?, ?)

                   ''', [title, price])
    conn.commit()


def showtable():
    cursor.execute('''
    SELECT id, title, price
    FROM products 
    ''')
    for row in cursor.fetchall():
        print(" ".join([str(item) for item in row])) 

def removeproduct (title):
    cursor.execute('''
    DELETE FROM products
    WHERE  title = ? 
    ''',[title])
    conn.commit()


cursor.execute('''
CREATE TABLE if not exists products (
               id integer primary key autoincrement,
               title varchar(128),
               price int
               )

''')


# addproduct('Iphone', 500)
# addproduct('велосипед', 50000)

removeproduct('Iphone')
showtable()

