import sqlite3 
import pandas as pd 

conn = sqlite3.connect("Databasa.db")
cursor = conn.cursor()

def csv2sql(filePath, tableName):
    df = pd.read_csv(filePath)
    df.to_sql(tableName, con=conn, if_exists="replace")

def showtable(tableName):

    cursor.execute(f'SELECT * FROM {tableName}')
    print("_-"*10)
    print(tableName)
    print("_-"*10)
    for row in cursor.fetchall():
        print(row)
    print("_-"*10 + '\n')

def sql2csv(filePath,tableName):
    df = pd.read_sql_query(con=conn, sql =f'SELECT * FROM {tableName}') 
    df.to_csv(filePath, index=False)

def init():
    cursor.execute('''
    CREATE TABLE if not exists hist_auto(
                   id integer primary key autoincrement,
                   model varchar(128),
                   transmission varchar(128),
                   body_type varchar(128),
                   drive_type varchar(128),
                   color varchar(128),
                   production_year int,
                   auto_key int,
                   engine_capacity number(2,1),
                   horsepower int,
                   engine_type varchar(128),
                   price int,
                   milage int,
                   deleted_flg int default 0,
                   start_dttm datetime current_timestamp,
                   end_dttm datetime default (datetime('2999-12-31 23:59:59'))
        )
    ''')

def newRows():
    cursor.execute('''
    CREATE TABLE tmp_new_rows as 
--                   select 
--                   from tmp_auto
--                  where auto_key not in (
--                                        select tmp_auto
--                                        from hist_auto
--                                            )
                   select 
                        t1.*
                   from tmp_auto as t1
                   left join hist_auto as t2 
                   on t1.auto_key=t2.auto_key
                   where t2.auto_key is null
    ''')

def deletedRows():
    cursor.execute('''
    CREATE TABLE tmp_deleted_rows as 
                   select 
                        t1.*
                   from hist_auto as t1
                   left join tmp_auto as t2 
                   on t1.auto_key=t2.auto_key
                   where t2.auto_key is null
    ''')

def changedRows():
    cursor.execute('''
    CREATE TABLE tmp_changed_rows as 
                   select 
                        t1.*
                   from tmp_auto  as t1
                   inner join hist_auto as t2 
                   on t1.auto_key=t2.auto_key
                   where t1.model <> t2.model
                        or t1.transmission <> t2.transmission
                        or t1.body_type <> t2.body_type
                        or t1.drive_type <> t2.drive_type
                        or t1.color <> t2.color
                        or t1.production_year <> t2.production_year
                        or t1.engine_capacity <> t2.engine_capacity
                        or t1.horsepower <> t2.horsepower
                        or t1.engine_type <> t2.engine_type
                        or t1.price <> t2.price
                        or t1.milage <> t2.milage
    ''')
#Удаляет все временные таблицы
def delete_temp_tables():
    cursor.execute('DROP TABLE if exists tmp_auto')
    cursor.execute('DROP TABLE if exists tmp_new_rows')
    cursor.execute('DROP TABLE if exists tmp_changed_rows')
    cursor.execute('DROP TABLE if exists tmp_deleted_rows')

def change_hist_auto():
    cursor.execute('''
        INSERT INTO hist_auto(
                   model,
                   transmission,
                   body_type,
                   drive_type,
                   color,
                   production_year,
                   auto_key,
                   engine_capacity,
                   horsepower,
                   engine_type,
                   price,
                   milage  
                    )
        SELECT 
                   model,
                   transmission,
                   body_type,
                   drive_type ,
                   color ,
                   production_year ,
                   auto_key ,
                   engine_capacity,
                   horsepower ,
                   engine_type,
                   price ,
                   milage
        FROM tmp_new_rows
                    ''')
    

    cursor.execute('''
        UPDATE hist_auto
        SET end_dttm = datetime('now', '-1 second')
        WHERE auto_key IN (SELECT auto_key
                        FROM tmp_changed_rows)
                   ''')
    
    cursor.execute('''
        INSERT INTO hist_auto(
                   model,
                   transmission,
                   body_type,
                   drive_type ,
                   color,
                   production_year,
                   auto_key,
                   engine_capacity,
                   horsepower,
                   engine_type,
                   price,
                   milage  
                    )
        SELECT 
                   model,
                   transmission,
                   body_type,
                   drive_type,
                   color,
                   production_year,
                   auto_key,
                   engine_capacity,
                   horsepower,
                   engine_type,
                   price,
                   milage
        FROM   tmp_changed_rows
                    ''')

    cursor.execute('''
        UPDATE hist_auto
        SET end_dttm = datetime('now', '-1 second')
        WHERE auto_key IN (SELECT auto_key
                        FROM tmp_deleted_rows)
                   ''')

    cursor.execute('''
        INSERT INTO hist_auto(
                   model,
                   transmission,
                   body_type,
                   drive_type ,
                   color ,
                   production_year ,
                   auto_key ,
                   engine_capacity,
                   horsepower ,
                   engine_type,
                   price ,
                   milage ,
                   deleted_flg 
                    )
        SELECT 
                   model,
                   transmission,
                   body_type,
                   drive_type ,
                   color ,
                   production_year ,
                   auto_key ,
                   engine_capacity,
                   horsepower ,
                   engine_type,
                   price ,
                   milage,
                   1
        FROM   tmp_deleted_rows
                    ''')


delete_temp_tables()
init()
csv2sql('Data Engenireeng/store/data_1.csv', 'tmp_auto')
changedRows()
newRows()
deletedRows()
change_hist_auto()

change_hist_auto()
showtable('tmp_auto')
showtable('tmp_new_rows')
showtable('tmp_changed_rows')
showtable('tmp_deleted_rows')
showtable('tmp_deleted_rows')
showtable('hist_auto')







    #df = pd.read_csv(filePath)
    #df.to_sql(tableName, con=conn, if_exists="replace")



#showtable('tmp_auto')

#sql2csv('Data Engenireeng/store/test.csv', 'tmp_auto')

