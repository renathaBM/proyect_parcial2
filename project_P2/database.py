# --------------------------------------------
# Archivo: database.py
# Función: Crea y devuelve una conexión MySQL
# --------------------------------------------
import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """Establece una conexión con la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',     # Servidor local (XAMPP)
            user='root',          # Usuario por defecto de MySQL
            password='',          # Contraseña (vacía si no has puesto una)
            database='POO_project_P2'  # Nombre de la base de datos
        )

        if conexion.is_connected():
            return conexion
    except Error as e:
        print("Error al conectar con la base de datos:", e)
        return None
