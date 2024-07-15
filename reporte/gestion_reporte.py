import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

import tkinter as tk
from producto import Producto
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from generar_reporte import GenerarReporte
from gestion_proveedores import GestionProveedores

class GestionReporte:
    def __init__(self, root):
        self.root = root
        self.root.title("Reportes - Ferretería Argamasa")
        self.root.geometry("800x600")

        # Título
        self.label_titulo = tk.Label(self.root, text="REPORTES", font=("Arial", 24))
        self.label_titulo.pack(pady=10)

        # Filtros de fecha y categoría
        self.frame_filtros = tk.Frame(self.root)
        self.frame_filtros.pack(pady=10)

        tk.Label(self.frame_filtros, text="Fecha: [Desde: ").grid(row=0, column=0)
        self.fecha_desde = DateEntry(self.frame_filtros, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_desde.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_filtros, text="] [Hasta: ").grid(row=0, column=2)
        self.fecha_hasta = DateEntry(self.frame_filtros, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_hasta.grid(row=0, column=3, padx=5)
        tk.Label(self.frame_filtros, text="]").grid(row=0, column=4)

        tk.Label(self.frame_filtros, text="Categoría:").grid(row=1, column=0, pady=5)
        self.categoria = ttk.Combobox(self.frame_filtros, values=["Todas", "Herramientas", "Accesorios", "Medición"], state="readonly")
        self.categoria.grid(row=1, column=1, pady=5)
        self.categoria.set("Todas")

        # Botones de acciones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        self.btn_inventario = tk.Button(self.frame_botones, text="INVENTARIO", command=self.mostrar_inventario)
        self.btn_inventario.grid(row=0, column=0, padx=10)

        self.btn_proveedor = tk.Button(self.frame_botones, text="PROVEEDOR", command=self.mostrar_proveedor)
        self.btn_proveedor.grid(row=0, column=1, padx=10)

        self.btn_generar = tk.Button(self.frame_botones, text="GENERAR REPORTE", command=self.generar_reporte)
        self.btn_generar.grid(row=0, column=2, padx=10)

        self.btn_descargar = tk.Button(self.frame_botones, text="DESCARGAR REPORTE", command=self.descargar_reporte)
        self.btn_descargar.grid(row=0, column=3, padx=10)

        # Tabla de reporte
        self.frame_tabla = tk.Frame(self.root)
        self.frame_tabla.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame_tabla, columns=("codigo", "nombre", "contacto", "direccion"), show='headings')
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("contacto", text="Contacto")
        self.tree.heading("direccion", text="Dirección")

        self.tree.pack(fill=tk.BOTH, expand=True)
        #self.cargar_datos_iniciales()

        

    def cargar_datos_iniciales(self):
        # Cargar datos de ejemplo al iniciar
        datos = [
            (1010, "CRISTIAN G", "12345", "SUBURBIO"),
            (2020, "SAMUEL A", "6789", "SUBURBIO"),
            (3030, "MELANIE S", "101112", "CENTRO"),
            (4040, "JESSICA M", "131415", "SUBURBIO")
        ]
        for dato in datos:
            self.tree.insert("", tk.END, values=dato)

    def mostrar_inventario(self):
        # Limpiar tabla y cargar datos de inventario (placeholder)
        self.tree.delete(*self.tree.get_children())
        datos_inventario = [
            (1010, "Martillo", "50", "Almacén 1"),
            (2020, "Taladro", "30", "Almacén 2"),
            (3030, "Tornillos", "200", "Almacén 1"),
            (4040, "Llave Inglesa", "15", "Almacén 2"),
            (5050, "Cinta Métrica", "40", "Almacén 1")
        ]
        for dato in datos_inventario:
            self.tree.insert("", tk.END, values=dato)

    def mostrar_proveedor(self):
        self.gestion_proveedores = GestionProveedores(root)
        self.gestion_proveedores.cargar_datos()

    def on_closing(self, window):
        window.destroy()
        self.root.deiconify()  # Mostrar el menú principal nuevamente

    def generar_reporte(self):
        # Lógica para generar reporte basado en los filtros
        fecha_desde = self.fecha_desde.get_date()
        fecha_hasta = self.fecha_hasta.get_date()
        categoria = self.categoria.get()
        reporte = GenerarReporte(fecha_desde, fecha_hasta, categoria)
        reporte.guardar_pdf()

        messagebox.showinfo("Generar Reporte", "Reporte generado exitosamente.")

    def descargar_reporte(self):
        # Obtener los datos de la tabla y descargar el reporte
        datos = [self.tree.item(item)['values'] for item in self.tree.get_children()]
        reporte = GenerarReporte(datos)
        reporte.guardar_pdf()
        messagebox.showinfo("Descargar Reporte", "Reporte descargado exitosamente como 'reporte.pdf'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionReporte(root)
    root.mainloop()
