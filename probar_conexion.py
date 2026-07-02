import os
import time
import pymssql

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "sa")
DB_PASSWORD = os.getenv("DB_PASSWORD", "TuClave_Fuerte123")

ultimo_error = None
for intento in range(1, 11):
    try:
        con = pymssql.connect(server=DB_HOST, user=DB_USER, password=DB_PASSWORD, database="master")
        cur = con.cursor()
        cur.execute("SELECT @@VERSION")
        print("Conexión exitosa a SQL Server")
        print(cur.fetchone()[0])
        con.close()
        break
    except Exception as error:
        ultimo_error = error
        print(f"Intento {intento}/10 fallido. Esperando SQL Server...")
        time.sleep(5)
else:
    raise RuntimeError(f"No fue posible conectar con SQL Server: {ultimo_error}")
