import socket
import mysql.connector as sql

HOST = "vh380.timeweb.ru"
PORT = 3306

def check_tcp():
    print("TCP тест:", HOST, PORT)
    with socket.create_connection((HOST, PORT), timeout=5) as s:
        print("Порт 3306 доступен")

def run_db():
    print("Пробуем подключиться к MySQL…")
    try:
        conn = sql.connect(
            host=HOST,
            port=PORT,
            user="cn58768",
            password="Kmechte1!",
            database="cn58768_stock",
            autocommit=True,
            connection_timeout=10,
            raise_on_warnings=True
        )
        print("is_connected():", conn.is_connected())
        cur = conn.cursor()
        cur.execute("SELECT NOW(), DATABASE(), USER();")
        row = cur.fetchone()
        print("Проверка запроса:", row)
        cur.close()
        conn.close()
        print("ОК")
    except sql.Error as err:
        # Детальный разбор ошибок коннектора MySQL
        print("MySQL error -> ERRNO:", getattr(err, "errno", None),
              "SQLSTATE:", getattr(err, "sqlstate", None),
              "MSG:", getattr(err, "msg", str(err)))
    except Exception as e:
        print("Unexpected error:", repr(e))

if __name__ == "__main__":
    try:
        check_tcp()
    except Exception as e:
        print("TCP недоступен:", repr(e))
    run_db()