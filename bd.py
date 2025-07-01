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
trusted_connection = os.getenv("SQL_TRUSTED_CONNECTION")

# se arma la cadena de conexión
conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
)

# Conectar y consultar
try:
    def obtenerConexion():
        conexion = pyodbc.connect(conn_str)
        conexion.close()
        
except Exception as e:
    print("Error al conectar: ", e)
    
def consulta(query, params=None, fetch=True):
    conexion = obtenerConexion()
    if conexion == None:
        print("No se conectó a la base de datos.")
        return
    try:
        cursor = conexion.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        resultados = cursor.fetchall() if fetch else None #fetch es si querés que la función devuelva los resultados de la consulta o no.

        cursor.close()
        conexion.commit()  # Para operaciones insert, update, delete
        conexion.close()

        return resultados

    except Exception as e:
        print("Error al ejecutar la consulta:", e)
        return None
    
    
    

