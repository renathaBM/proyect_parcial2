# -----------------------------------------------------------
# Archivo: user_controlller.py
# Función: CRUD para la tabla usuarios
# -----------------------------------------------------------
from database import crear_conexion

# --- READ ---
def obtener_usuarios():
    """Consulta todos los usuarios en la base de datos."""
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, usuario, password FROM usuarios ORDER BY id")
        rows = cursor.fetchall()
        conexion.close()
        return rows
    except Exception as e:
        print("Error al obtener usuarios:", e)
        return []

# --- CREATE ---
def agregar_usuario(usuario, password):
    """Agrega un nuevo usuario."""
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión"
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (%s, %s)", (usuario, password))
        conexion.commit()
        conexion.close()
        return True, "Usuario agregado correctamente"
    except Exception as e:
        print("Error al agregar usuario:", e)
        return False, str(e)

# --- UPDATE ---
def actualizar_usuario(user_id, usuario, password):
    """Actualiza datos de un usuario existente."""
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión"
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET usuario=%s, password=%s WHERE id=%s", (usuario, password, user_id))
        conexion.commit()
        conexion.close()
        return True, "Usuario actualizado correctamente"
    except Exception as e:
        print("Error al actualizar usuario:", e)
        return False, str(e)

# --- DELETE ---
def eliminar_usuario(user_id):
    """Elimina un usuario de la base de datos."""
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión"
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id=%s", (user_id,))
        conexion.commit()
        conexion.close()
        return True, "Usuario eliminado correctamente"
    except Exception as e:
        print("Error al eliminar usuario:", e)
        return False, str(e)
