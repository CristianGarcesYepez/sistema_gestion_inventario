import mysql.connector

class Producto:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_argamasa"
        )
        self.cursor = self.conexion.cursor()

    def agregar_producto(self, codigo, nombre, categoria, cantidad, precio, proveedor):
        sql = "INSERT INTO productos (codigo, descripcion, categoria, cantidad, precio, proveedor) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (codigo, nombre, categoria, cantidad, precio, proveedor)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def editar_producto(self, codigo, nombre, categoria, cantidad, precio, proveedor):
        sql = "UPDATE productos SET descripcion=%s, categoria=%s, cantidad=%s, precio=%s, proveedor=%s WHERE codigo=%s"
        valores = (nombre, categoria, cantidad, precio, proveedor, codigo)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar_producto(self, codigo):
        sql = "DELETE FROM productos WHERE codigo=%s"
        valores = (codigo,)
        self.cursor.execute(sql, valores)
        self.conexion.commit()
    
    def obtener_productos(self):
        sql = "SELECT * FROM productos"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def buscar_producto(self, nombre):
        sql = "SELECT * FROM productos WHERE descripcion LIKE %s"
        nombre_busqueda = f"%{nombre}%"  # Añadir % para buscar coincidencias parciales
        self.cursor.execute(sql, (nombre_busqueda,))
        return self.cursor.fetchall()
    
    def obtener_productos_por_categoria(self, categoria):
        sql = "SELECT * FROM productos WHERE categoria=%s"
        valores = (categoria,)
        self.cursor.execute(sql, valores)
        return self.cursor.fetchall()

