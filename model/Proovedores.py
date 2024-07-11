import mysql.connector

class Proveedores:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_argamasa"
        )
        self.cursor = self.conexion.cursor()

    def agregar_proveedor(self,id_proveedor,nombre_proveedor,direccion,contacto,email):
        sql = "INSERT INTO proveedores(id_proveedor,nombre_proveedor,direccion,contacto,email) VALUES (%s,%s,%s,%s,%s)"
        valores = (id_proveedor,nombre_proveedor,direccion,contacto,email)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def editar_proveedor(self,id_proveedor,nombre_proveedor,direccion,contacto,email):
        sql = "UPDATE proveedores SET nombre_proveedor=%s, direccion=%s,contacto=%s,email=%s WHERE id_proveedor=%s"
        valores = (nombre_proveedor,direccion,contacto,email,id_proveedor)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_proveedor(self,id_proveedor):
        sql = "DELETE FROM proveedores WHERE id_proveedor=%s"
        valores = (id_proveedor,)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def obtener_proveedor(self):
        sql = "SELECT * FROM proveedores"
        self.cursor.execute(sql)
        return self.cursor.fetchall()