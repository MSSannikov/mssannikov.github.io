import sqlite3
import pandas as pd
import os

conn = sqlite3.connect('Final_project.db') #Создали курсор
cursor = conn.cursor()

############################################################
#Создаем Таблицы внутри БД
############################################################
def create_table_terminals():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "TERMINALS"(
        terminal_id varchar(5) PRIMARY KEY,
        terminal_type varchar(5),
        terminal_city varchar(20),
        terminal_address varchar(100),
        create_dt date DEFAULT (strftime('%d%m%Y', 'now')),
        update_dt date
               )
                ''')

def create_table_clients():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "CLIENTS"(
        client_id varchar(32) PRIMARY KEY,
        last_name varchar(32),
        first_name varchar(32),
        patrinymic varchar(32),
        date_of_birth date,
        paport_num varchar(15),
        passpot_valid_to date,
        phone varchar(15),
        effective_from date,
        effective_to date,
        deleted_flg binary
               )
                ''')

def create_table_accounts():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "ACCAUNTS"(
        accaunt_num varchar(32) PRIMARY KEY,
        valid_to date,
        client varchar(32),
        FOREIGN KEY (client) REFERENCES CLIENTS(client_id),
        create_dt date DEFAULT (strftime('%d%m%Y', 'now')),
        update_dt date,
               )
                ''')

def create_table_cards():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "CARDS"(
        card_num varchar(32) PRIMARY KEY,
        accaunt_num varchar(32),
        create_dt date DEFAULT (strftime('%d%m%Y', 'now')),
        update_dt date,
        FOREIGN KEY (accaunt_num) REFERENCES ACCAUNTS(accaunt_num)
               )
                ''')

def create_table_transactions():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "TRANSACTIONS"(
        trans_id varchar(32),
        trans_date date,
        card_num varchar(32),
        order_type varchar(32),
        amt decimal(10,2),
        oper_result varchar(32),
        terminal varchar(32),
        effective_from date,
        effective_to date,
        deleted_flg binary,
        FOREIGN KEY (card_num) REFERENCES CARDS(card_num),
        FOREIGN KEY (terminal) REFERENCES ACCAUNTS(terminal_id)
               )
                ''')

def create_table_passport_blk():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "PASSPORT BLACKLIST"(
        passport_num varchar(32) PRIMARY KEY,
        entry_dt date
               )
                ''')

############################################################
#Поиск данных
############################################################

today = '01032021'

create_table_passport_blk()
create_table_terminals()

ter = pd.read_excel('/Users/maksim/Documents/Coding/mssannikov.github.io/Data_Engenireeng/Increment_download/terminals_01032021.xlsx', sheet_name='terminals')
bl = pd.read_excel('/Users/maksim/Documents/Coding/mssannikov.github.io/Data_Engenireeng/Increment_download/passport_blacklist_01032021.xlsx', sheet_name='blacklist')
tr= pd.read_csv('/Users/maksim/Documents/Coding/mssannikov.github.io/Data_Engenireeng/Increment_download/transactions_01032021.txt', sep=';')

# Specify the directory path
directory = "./Data_Engenireeng/Increment_download"

############################################################
#Вставка данных
############################################################

for dt in range(len(bl)):
    # Преобразуем дату в строку формата YYYY-MM-DD
    date_str = pd.to_datetime(bl['date'][dt]).strftime('%Y-%m-%d')
    passport = str(bl['passport'][dt])
    
    cursor.execute('''
        INSERT INTO "PASSPORT BLACKLIST" (passport_num, entry_dt)
        VALUES (?, ?)
    ''', (passport, date_str))

for dt in range(len(ter)):  
    cursor.execute('''
        INSERT INTO "TERMINALS" (terminal_id, terminal_type, terminal_city, terminal_address)
        VALUES (?, ?, ?, ?)
    ''', (ter['terminal_id'][dt], ter['terminal_type'][dt], ter['terminal_city'][dt], ter['terminal_address'][dt]))


#print(type(ter['terminal_id'][1]))
     # ter['terminal_type'], ter['terminal_city'], ter['terminal_address'])

# List all files and directories
#contents = os.listdir(directory)
#print(contents)

## 

#
# Сохраняем изменения и закрываем соединение
#conn.commit()#

#def showUsers():
#    cursor.execute('SELECT * FROM "passport blacklist"')
#
#    for row in cursor.fetchall():
#        print(row)     
    
#showUsers()
