import pyodbc
import os
from dotenv import load_dotenv

# se cargan las variables de entorno
load_dotenv()

# credenciales de la base de datos
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
trusted_connection = os.getenv("SQL_TRUSTED_CONNECTION", "no").lower() == "yes"

# se arma la cadena de conexión
if trusted_connection:
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )
else:
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )

# Conectar y consultar
try:
    conexion = pyodbc.connect(conn_str)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM empleados")  
    for fila in cursor.fetchall():
        print(fila)
    conexion.close()
    
except Exception as e:
    print("Error al conectar: ", e)
