import sqlite3

conn = sqlite3.connect("Data_new.db")
cursor = conn.cursor()

cursor.execute('''
          CREATE TABLE if not exists USERS(
               id integer primary key autoincrement,
               name varchar(128),
               lastname varchar(128)
               )    
               ''')

def add(name, lastname):
    cursor.execute(''' SELECT 
                            count() as cnt
                        from users
                        where name = ?
                        and lastname = ?
                   ''', [name, lastname])
    
    count = cursor.fetchone()[0]

    if count > 0:
            return 
    
    cursor.execute('''
                  INSERT INTO users (name,lastname)
                  VALUES (?, ?)
                  ''', [name, lastname])
    conn.commit()

def showUsers():
    cursor.execute('SELECT * FROM users')

    for row in cursor.fetchall():
        print(row)       
                   
    add('Aнтон', 'Куликов')
    add('Максим', 'Санников')
    add('Кирилл', 'Шмидт')
    add('Aнтон', 'Куликов')
    add('Роман', 'Иванов')
showUsers()
    