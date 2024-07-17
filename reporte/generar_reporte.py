import mysql.connector
from fpdf import FPDF

class GenerarReporte:
    def __init__(self, fecha_desde, fecha_hasta, categoria):
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.categoria = categoria

    def obtener_datos(self):
        try:
            # Conectar a la base de datos
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",  
                password="",  
                database="db_argamasa"
            )

            cursor = conexion.cursor()

            # Crear la consulta SQL
            query = """
                SELECT p.codigo, p.descripcion, c.nombre_categoria, p.cantidad, p.precio, p.proveedor
                FROM productos p
                JOIN categorias c ON p.categoria = c.nombre_categoria
                JOIN proveedores pr ON p.proveedor = pr.nombre_proveedor
                WHERE p.fecha_ultimo_ingreso >= %s AND p.fecha_ultimo_ingreso <= %s
            """

            params = [self.fecha_desde, self.fecha_hasta]

            if self.categoria != "Todas":
                query += " AND c.nombre_categoria = %s"
                params.append(self.categoria)

            cursor.execute(query, params)

            datos = cursor.fetchall()
            conexion.close()
            return datos

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def guardar_pdf(self, filename="reporte.pdf"):
        datos = self.obtener_datos()
        if not datos:
            print("No se encontraron datos para el reporte.")
            return

        pdf = FPDF()
        pdf.add_page()

        # Título
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Reporte de Inventario", ln=True, align='C')

        # Tabla
        pdf.set_font("Arial", size=10)
        col_width = pdf.w / 6.5
        row_height = pdf.font_size

        # Column headers
        headers = ["Código", "Descripción", "Categoría", "Cantidad", "Precio", "Proveedor"]
        for header in headers:
            pdf.cell(col_width, row_height * 2, header, border=1)
        pdf.ln(row_height * 2)

        # Data rows
        for row in datos:
            for item in row:
                pdf.cell(col_width, row_height * 2, str(item), border=1)
            pdf.ln(row_height * 2)

        pdf.output(filename)

if __name__ == "__main__":
    # Ejemplo de uso
    reporte = GenerarReporte(fecha_desde="2024-01-01", fecha_hasta="2024-12-31", categoria="Todas")
    reporte.guardar_pdf()
    print("Reporte PDF generado como 'reporte.pdf'")
