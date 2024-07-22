import mysql.connector

class Categoria:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_argamasa"
        )
        self.cursor = self.conexion.cursor()

    def agregar_categoria(self, nombre):
        sql = "INSERT INTO categorias (nombre) VALUES (%s)"
        valores = (nombre,)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def editar_categoria(self, nombre_actual, nuevo_nombre):
        sql = "UPDATE categorias SET nombre=%s WHERE nombre=%s"
        valores = (nuevo_nombre, nombre_actual)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_categoria(self, nombre):
        sql = "DELETE FROM categorias WHERE nombre=%s"
        valores = (nombre,)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def obtener_categorias(self):
        sql = "SELECT * FROM categorias"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
