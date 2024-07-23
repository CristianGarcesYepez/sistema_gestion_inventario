import mysql.connector  # Importa el módulo mysql.connector para trabajar con MySQL

class Producto:
    def __init__(self):
        # Inicializa la conexión a la base de datos MySQL
        self.conexion = mysql.connector.connect(
            host="localhost",  # El servidor de la base de datos
            user="root",       # El nombre de usuario para conectarse a la base de datos
            password="",       # La contraseña para el usuario de la base de datos
            database="db_argamasa"  # El nombre de la base de datos a la que conectar
        )
        # Crea un cursor para ejecutar consultas SQL
        self.cursor = self.conexion.cursor()

    def agregar_producto(self, codigo, nombre, categoria, cantidad, precio, proveedor):
        # Consulta SQL para insertar un nuevo producto en la base de datos
        sql = "INSERT INTO productos (codigo, descripcion, categoria, cantidad, precio, proveedor) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (codigo, nombre, categoria, cantidad, precio, proveedor)  # Valores a insertar
        # Ejecuta la consulta SQL con los valores proporcionados
        self.cursor.execute(sql, valores)
        # Confirma los cambios en la base de datos
        self.conexion.commit()

    def editar_producto(self, codigo, nombre, categoria, cantidad, precio, proveedor):
        # Consulta SQL para actualizar un producto existente en la base de datos
        sql = "UPDATE productos SET descripcion=%s, categoria=%s, cantidad=%s, precio=%s, proveedor=%s WHERE codigo=%s"
        valores = (nombre, categoria, cantidad, precio, proveedor, codigo)  # Valores a actualizar
        # Ejecuta la consulta SQL con los valores proporcionados
        self.cursor.execute(sql, valores)
        # Confirma los cambios en la base de datos
        self.conexion.commit()

    def eliminar_producto(self, codigo):
        # Consulta SQL para eliminar un producto de la base de datos
        sql = "DELETE FROM productos WHERE codigo=%s"
        valores = (codigo,)  # Valor para identificar el producto a eliminar
        # Ejecuta la consulta SQL con el valor proporcionado
        self.cursor.execute(sql, valores)
        # Confirma los cambios en la base de datos
        self.conexion.commit()
    
    def obtener_productos(self):
        # Consulta SQL para seleccionar todos los productos de la base de datos
        sql = "SELECT * FROM productos"
        # Ejecuta la consulta SQL
        self.cursor.execute(sql)
        # Devuelve todos los resultados de la consulta
        return self.cursor.fetchall()
    
    def buscar_producto(self, nombre):
        # Consulta SQL para buscar productos cuyo nombre contenga el término proporcionado
        sql = "SELECT * FROM productos WHERE descripcion LIKE %s"
        nombre_busqueda = f"%{nombre}%"  # Añadir % para buscar coincidencias parciales
        # Ejecuta la consulta SQL con el término de búsqueda
        self.cursor.execute(sql, (nombre_busqueda,))
        # Devuelve todos los resultados de la búsqueda
        return self.cursor.fetchall()
    
    def obtener_productos_por_categoria(self, categoria):
        # Consulta SQL para seleccionar productos de una categoría específica
        sql = "SELECT * FROM productos WHERE categoria=%s"
        valores = (categoria,)  # Valor para filtrar productos por categoría
        # Ejecuta la consulta SQL con el valor proporcionado
        self.cursor.execute(sql, valores)
        # Devuelve todos los productos que coincidan con la categoría
        return self.cursor.fetchall()
