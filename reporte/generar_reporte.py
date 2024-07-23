import mysql.connector  # Importa el módulo para conectar con MySQL
from fpdf import FPDF  # Importa la clase FPDF para generar PDFs

class GenerarReporte:
    def __init__(self, fecha_desde, fecha_hasta, categoria):
        # Inicializa el objeto con las fechas y la categoría para el reporte
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.categoria = categoria

    def obtener_datos(self):
        try:
            # Conectar a la base de datos MySQL
            conexion = mysql.connector.connect(
                host="localhost",      # Dirección del servidor de base de datos
                user="root",           # Usuario para conectar a la base de datos
                password="",           # Contraseña del usuario
                database="db_argamasa" # Nombre de la base de datos
            )

            cursor = conexion.cursor()  # Crear un cursor para ejecutar consultas

            # Crear la consulta SQL para obtener datos
            query = """
                SELECT p.codigo, p.descripcion, c.nombre_categoria, p.cantidad, p.precio, p.proveedor
                FROM productos p
                JOIN categorias c ON p.categoria = c.nombre_categoria
                JOIN proveedores pr ON p.proveedor = pr.nombre_proveedor
                WHERE p.fecha_ultimo_ingreso >= %s AND p.fecha_ultimo_ingreso <= %s
            """

            params = [self.fecha_desde, self.fecha_hasta]  # Parámetros para la consulta

            # Añadir condición adicional si se especifica una categoría
            if self.categoria != "Todas":
                query += " AND c.nombre_categoria = %s"
                params.append(self.categoria)

            cursor.execute(query, params)  # Ejecutar la consulta con los parámetros

            datos = cursor.fetchall()  # Obtener todos los resultados de la consulta
            conexion.close()  # Cerrar la conexión a la base de datos
            return datos

        except mysql.connector.Error as err:
            # Manejo de errores en caso de fallo de la consulta o conexión
            print(f"Error: {err}")
            return []

    def guardar_pdf(self, filename="reporte.pdf"):
        datos = self.obtener_datos()  # Obtener los datos a incluir en el reporte
        if not datos:
            print("No se encontraron datos para el reporte.")
            return

        pdf = FPDF()  # Crear un objeto FPDF para generar el PDF
        pdf.add_page()  # Añadir una página al PDF

        # Configurar el título del reporte
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Reporte de Inventario", ln=True, align='C')

        # Configurar la tabla
        pdf.set_font("Arial", size=10)
        col_width = pdf.w / 6.5  # Ancho de cada columna
        row_height = pdf.font_size  # Altura de cada fila

        # Encabezados de columna
        headers = ["Código", "Descripción", "Categoría", "Cantidad", "Precio", "Proveedor"]
        for header in headers:
            pdf.cell(col_width, row_height * 2, header, border=1)  # Añadir encabezado con borde
        pdf.ln(row_height * 2)  # Nueva línea después de los encabezados

        # Filas de datos
        for row in datos:
            for item in row:
                pdf.cell(col_width, row_height * 2, str(item), border=1)  # Añadir cada dato con borde
            pdf.ln(row_height * 2)  # Nueva línea después de cada fila

        pdf.output(filename)  # Guardar el PDF con el nombre especificado

if __name__ == "__main__":
    # Ejemplo de uso de la clase GenerarReporte
    reporte = GenerarReporte(fecha_desde="2024-01-01", fecha_hasta="2024-12-31", categoria="Todas")
    reporte.guardar_pdf()  # Generar y guardar el PDF
    print("Reporte PDF generado como 'reporte.pdf'")
