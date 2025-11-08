# ------------------------------------------------------
# Archivo: auth_controller.py
# Función: Validar las credenciales del usuario (Login)
# ------------------------------------------------------
from database import crear_conexion

def validar_credenciales(usuario, password):
    """Valida si el usuario y contraseña existen en la base."""
    conexion = crear_conexion()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        consulta = "SELECT id FROM usuarios WHERE usuario = %s AND password = %s"
        cursor.execute(consulta, (usuario, password))  # Busca coincidencias
        result = cursor.fetchone()  # Obtiene el primer resultado
        cursor.close()
        conexion.close()
        return bool(result)  # Devuelve True si encontró coincidencia
    except Exception as e:
        print("Error al validar credenciales:", e)
        return False
