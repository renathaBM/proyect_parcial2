# ------------------------------------------------------------
# Archivo: products_controller.py
# Función: Controlador CRUD para la tabla "productos"
# ------------------------------------------------------------
# Aquí está toda la lógica para agregar, leer, actualizar y eliminar productos
# directamente desde la base de datos MySQL.

from database import crear_conexion

# --- READ (LEER) ---
def obtener_productos():
    """Obtiene todos los registros de la tabla productos."""
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_producto, nombre_producto, descripcion, stock, precio, status, marca, proveedor
            FROM productos ORDER BY id_producto
        """)
        rows = cursor.fetchall()  # Devuelve una lista de tuplas
        cursor.close()
        conexion.close()
        return rows
    except Exception as e:
        print("Error al obtener productos:", e)
        return []

# --- CREATE (CREAR) ---
def agregar_producto(nombre, descripcion, stock, precio, status, marca, proveedor):
    """Inserta un nuevo producto en la base de datos."""
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión con la base de datos"
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO productos (nombre_producto, descripcion, stock, precio, status, marca, proveedor)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(consulta, (nombre, descripcion, stock, precio, status, marca, proveedor))
        conexion.commit()  # Guarda los cambios
        cursor.close()
        conexion.close()
        return True, "Producto agregado correctamente"
    except Exception as e:
        print("Error al agregar producto:", e)
        return False, str(e)

# --- UPDATE (ACTUALIZAR) ---
def actualizar_producto(id_producto, nombre, descripcion, stock, precio, status, marca, proveedor):
    """Modifica los datos de un producto existente."""
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión con la base de datos"
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE productos
            SET nombre_producto=%s, descripcion=%s, stock=%s, precio=%s, status=%s, marca=%s, proveedor=%s
            WHERE id_producto=%s
        """
        cursor.execute(consulta, (nombre, descripcion, stock, precio, status, marca, proveedor, id_producto))
        conexion.commit()
        affected = cursor.rowcount  # Cantidad de filas afectadas
        cursor.close()
        conexion.close()
        if affected == 0:
            return False, "No se encontró el producto"
        return True, "Producto actualizado correctamente"
    except Exception as e:
        print("Error al actualizar producto:", e)
        return False, str(e)

# --- DELETE (ELIMINAR) ---
def eliminar_producto(id_producto):
    """Elimina un producto por su ID."""
    conexion = crear_conexion()
    if not conexion:
        return False, "Error de conexión con la base de datos"
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        conexion.commit()
        affected = cursor.rowcount
        cursor.close()
        conexion.close()
        if affected == 0:
            return False, "No se encontró el producto"
        return True, "Producto eliminado correctamente"
    except Exception as e:
        print("Error al eliminar producto:", e)
        return False, str(e)
