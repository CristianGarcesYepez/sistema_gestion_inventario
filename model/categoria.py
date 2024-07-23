import mysql.connector  # Importa el módulo para conectar con bases de datos MySQL

class Categoria:
    def __init__(self):
        # Establece una conexión con la base de datos MySQL
        self.conexion = mysql.connector.connect(
            host="localhost",  # Dirección del servidor de base de datos
            user="root",       # Usuario de la base de datos
            password="",       # Contraseña del usuario (vacía por defecto)
            database="db_argamasa"  # Nombre de la base de datos a utilizar
        )
        # Crea un cursor para ejecutar comandos SQL en la base de datos
        self.cursor = self.conexion.cursor()

    def agregar_categoria(self, nombre):
        # Inserta una nueva categoría en la tabla 'categorias'
        sql = "INSERT INTO categorias (nombre) VALUES (%s)"  # Sentencia SQL para insertar datos
        valores = (nombre,)  # Valores a insertar (tupla con un solo elemento)
        self.cursor.execute(sql, valores)  # Ejecuta la sentencia SQL con los valores proporcionados
        self.conexion.commit()  # Confirma la transacción para guardar los cambios en la base de datos

    def editar_categoria(self, nombre_actual, nuevo_nombre):
        # Actualiza el nombre de una categoría existente
        sql = "UPDATE categorias SET nombre=%s WHERE nombre=%s"  # Sentencia SQL para actualizar datos
        valores = (nuevo_nombre, nombre_actual)  # Valores a actualizar (tupla con nombre nuevo y nombre actual)
        self.cursor.execute(sql, valores)  # Ejecuta la sentencia SQL con los valores proporcionados
        self.conexion.commit()  # Confirma la transacción para guardar los cambios en la base de datos

    def eliminar_categoria(self, nombre):
        # Elimina una categoría de la tabla 'categorias'
        sql = "DELETE FROM categorias WHERE nombre=%s"  # Sentencia SQL para eliminar datos
        valores = (nombre,)  # Valor a eliminar (tupla con un solo elemento)
        self.cursor.execute(sql, valores)  # Ejecuta la sentencia SQL con el valor proporcionado
        self.conexion.commit()  # Confirma la transacción para guardar los cambios en la base de datos

    def obtener_categorias(self):
        # Obtiene todas las categorías de la tabla 'categorias'
        sql = "SELECT * FROM categorias"  # Sentencia SQL para seleccionar todos los datos
        self.cursor.execute(sql)  # Ejecuta la sentencia SQL
        return self.cursor.fetchall()  # Devuelve todos los resultados de la consulta como una lista de tuplas

