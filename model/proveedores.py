import mysql.connector  # Importa el módulo para conectar con MySQL

class Proveedores:
    def __init__(self):
        # Inicializa la conexión a la base de datos MySQL
        self.conexion = mysql.connector.connect(
            host="localhost",  # Dirección del servidor MySQL
            user="root",       # Nombre de usuario para la conexión
            password="",       # Contraseña para la conexión (vacío por defecto)
            database="db_argamasa"  # Nombre de la base de datos
        )
        self.cursor = self.conexion.cursor()  # Crea un cursor para ejecutar comandos SQL

    def agregar_proveedor(self, id_proveedor, nombre_proveedor, direccion, contacto, email):
        # Inserta un nuevo proveedor en la base de datos
        sql = "INSERT INTO proveedores (id_proveedor, nombre_proveedor, direccion, contacto, email) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_proveedor, nombre_proveedor, direccion, contacto, email)  # Tupla con los valores a insertar
        self.cursor.execute(sql, valores)  # Ejecuta la consulta SQL con los valores proporcionados
        self.conexion.commit()  # Confirma los cambios en la base de datos

    def editar_proveedor(self, id_proveedor, nombre_proveedor, direccion, contacto, email):
        # Actualiza la información de un proveedor existente en la base de datos
        sql = "UPDATE proveedores SET nombre_proveedor=%s, direccion=%s, contacto=%s, email=%s WHERE id_proveedor=%s"
        valores = (nombre_proveedor, direccion, contacto, email, id_proveedor)  # Tupla con los nuevos valores y el ID del proveedor
        self.cursor.execute(sql, valores)  # Ejecuta la consulta SQL con los valores proporcionados
        self.conexion.commit()  # Confirma los cambios en la base de datos

    def eliminar_proveedor(self, id_proveedor):
        # Elimina un proveedor de la base de datos usando su ID
        sql = "DELETE FROM proveedores WHERE id_proveedor=%s"
        valores = (id_proveedor,)  # Tupla con el ID del proveedor a eliminar
        self.cursor.execute(sql, valores)  # Ejecuta la consulta SQL con el ID proporcionado
        self.conexion.commit()  # Confirma los cambios en la base de datos

    def obtener_proveedor(self):
        # Obtiene todos los proveedores de la base de datos
        sql = "SELECT * FROM proveedores"  # Consulta SQL para seleccionar todos los registros
        self.cursor.execute(sql)  # Ejecuta la consulta SQL
        return self.cursor.fetchall()  # Devuelve todos los resultados de la consulta como una lista de tuplas
