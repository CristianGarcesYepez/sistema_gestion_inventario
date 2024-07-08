import mysql.connector

class Categoria:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="db_argamasa"
        )
        self.cursor = self.conexion.cursor()

    def agregar_categoria(self, nombre):
        sql = "INSERT INTO categoria (nombre) VALUES (%s)"
        valores = (nombre,)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def editar_categoria(self, nombre_actual, nuevo_nombre):
        sql = "UPDATE categoria SET nombre=%s WHERE nombre=%s"
        valores = (nuevo_nombre, nombre_actual)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_categoria(self, nombre):
        sql = "DELETE FROM categoria WHERE nombre=%s"
        valores = (nombre,)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def obtener_categorias(self):
        sql = "SELECT * FROM categoria"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def obtener_productos_por_categoria(self, id_categoria):
        sql = "SELECT * FROM productos WHERE id_categoria=%s"
        valores = (id_categoria,)
        self.cursor.execute(sql, valores)
        return self.cursor.fetchall()
