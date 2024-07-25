import sys
import os

# Añadir rutas al sys.path para poder importar módulos desde directorios específicos
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, simpledialog
from proveedores import Proveedores

class GestionProveedores:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Proveedores - Ferretería Argamasa")  # Establecer el título de la ventana
        self.root.geometry("800x600")  # Establecer el tamaño de la ventana principal
        self.root.resizable(False, False)
        self.root.iconbitmap("recursos/LOGO.ico")

        # Crear una instancia de la clase Proveedores
        self.proveedores = Proveedores()

        # Crear un canvas para colocar elementos gráficos
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Crear el marco para los controles
        self.frame = tk.Frame(self.canvas, bg="")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.9)

        # Cargar y establecer la imagen de fondo
        self.cargar_imagen_fondo()

        # Título de la ventana directamente en el canvas
        self.canvas.create_text(400, 50, text="PROVEEDORES", font=("Arial", 30, "bold"), fill="black", anchor=tk.CENTER)

        self.crear_botones()

        # Contenedor de botones
        self.botones = tk.Frame(self.frame)
        self.botones.pack(pady=10)  # Añadir un espaciado vertical

        # Estilo a Tabla
        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("Treeview", 
                         background="#f0f0f0", 
                         foreground="black", 
                         rowheight=25, 
                         fieldbackground="white", 
                         bordercolor="black",  
                         borderwidth=1,
                         font=("Arial", 8))
        estilo.map("Treeview", 
                   background=[('selected', '#d3d3d3')], 
                   foreground=[('selected', 'black')])
        
        estilo.configure("Treeview.Heading", font=("Arial", 9, "bold"), bordercolor="black", borderwidth=1)

        estilo.layout("Treeview", [
            ('Treeview.treearea', {'sticky': 'nswe'}),
            ('Treeview.padding', {'sticky': 'nswe'}),
            ('Treeview.cell', {'sticky': 'nswe', 'children': [
                ('Treeitem.padding', {'sticky': 'nswe', 'children': [
                    ('Treeitem.indicator', {'side': 'left', 'sticky': ''}),
                    ('Treeitem.image', {'side': 'left', 'sticky': ''}),
                    ('Treeitem.text', {'side': 'left', 'sticky': ''}),
                ]}),
            ]}),
        ])

        # Crear una tabla (Treeview) para mostrar los proveedores
        self.tree = ttk.Treeview(self.frame, columns=("id_proveedor", "nombre_proveedor", "direccion", "contacto", "email"), show='headings')
        self.tree.heading("id_proveedor", text="Codigo")  # Configurar encabezados de columna
        self.tree.heading("nombre_proveedor", text="Proveedor")
        self.tree.heading("direccion", text="Direccion")
        self.tree.heading("contacto", text="Contacto")
        self.tree.heading("email", text="Email")
                # Configuración de las columnas 
        self.tree.column("id_proveedor", width=100, anchor='center')
        self.tree.column("nombre_proveedor", width=150, anchor='center')
        self.tree.column("direccion", width=100, anchor='center')
        self.tree.column("contacto", width=80, anchor='center')
        self.tree.column("email", width=190, anchor='center')

        self.tree.pack(pady=(120, 10), fill=tk.BOTH, expand=False, padx=10)  # Empaquetar la tabla para llenar el espacio disponible

        self.mostrar_logo()
        self.cargar_datos()  # Cargar datos en la tabla al iniciar

    def cargar_imagen_fondo(self):
        try:
            self.bg_image = Image.open("recursos/FONDO.png")
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo, tags="bg_image")
        except Exception as e:
            print(f"Error al cargar la imagen de fondo: {e}")

    def actualizar_imagen_fondo(self, event=None):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        resized_image = self.bg_image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        
        self.canvas.delete("bg_image")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo, tags="bg_image")

    def crear_botones(self):
        # Botón para agregar proveedor
        self.btn_agg = tk.Button(self.canvas, text="AGREGAR PROVEEDOR", command=self.agregar_proveedor, width=19, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
        self.canvas.create_window(200, 130, window=self.btn_agg) # Añadir un espaciado horizontal 
        # Botón para editar proveedor
        self.btn_edit = tk.Button(self.canvas, text="EDITAR PROVEEDOR", command=self.editar_proveedor, width=19, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
        self.canvas.create_window(400, 130, window=self.btn_edit)  # Añadir un espaciado horizontal
        # Botón para eliminar proveedor
        self.btn_eliminar = tk.Button(self.canvas, text="ELIMINAR PROVEEDOR", command=self.eliminar_proveedor, width=19, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
        self.canvas.create_window(600, 130, window=self.btn_eliminar)  # Añadir un espaciado horizontal

    def mostrar_logo(self):
        try:
            # Cargar la imagen del logo
            self.logo_image = Image.open("recursos/ARGAMASA_logo.png")
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)

            # Colocar el logo debajo del widget Treeview
            self.canvas.create_image(400, 525, image=self.logo_photo, anchor=tk.CENTER)
        except Exception as e:
            print(f"Error al cargar el logo: {e}")

    def cargar_datos(self):
        # Limpiar datos actuales de la tabla
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Obtener los proveedores desde la base de datos y agregarlos a la tabla
        proveedor = self.proveedores.obtener_proveedor()
        for i in proveedor:
            self.tree.insert("", tk.END, values=i)

    def agregar_proveedor(self):
        # Abrir un diálogo para agregar un nuevo proveedor
        self.dialogo_producto("Añadir Proveedor", self.proveedores.agregar_proveedor)

    def editar_proveedor(self):
        # Editar el proveedor seleccionado en la tabla
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un proveedor para editar")
            return
        proveedor = self.tree.item(seleccion[0])['values']
        self.dialogo_producto("Editar Proveedor", self.proveedores.editar_proveedor, proveedor)

    def eliminar_proveedor(self):
        # Eliminar el proveedor seleccionado en la tabla
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar")
            return
        ID = self.tree.item(seleccion[0])['values'][0]
        if messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar el Proveedor con código {ID}?"):
            self.proveedores.eliminar_proveedor(ID)
            self.cargar_datos()

    def dialogo_producto(self, titulo, accion, proveedor=None):
        # Abre un diálogo para ingresar o editar datos del proveedor
        dialogo = tk.Toplevel(self.root)
        dialogo.title(titulo)

        # Etiquetas y campos de entrada para los datos del proveedor
        etiquetas = ["Id_proveedor", "nombre_proveedor", "direccion", "contacto", "email"]
        entradas = {}

        for i, etiqueta in enumerate(etiquetas):
            tk.Label(dialogo, text=etiqueta).grid(row=i, column=0, pady=5)  # Etiquetas en la columna 0
            entrada = tk.Entry(dialogo)
            entrada.grid(row=i, column=1, pady=5)  # Campos de entrada en la columna 1
            if proveedor:
                entrada.insert(0, proveedor[i])  # Rellenar campos si se está editando un proveedor
            entradas[etiqueta.lower()] = entrada

        def on_confirmar():
            # Valida y guarda los datos del proveedor
            try:
                datos = {campo: entradas[campo].get() for campo in entradas}
                if proveedor:
                    # Editar proveedor existente
                    accion(proveedor[0], datos["nombre_proveedor"], datos["direccion"], datos["contacto"], datos["email"])
                else:
                    # Agregar nuevo proveedor
                    accion(datos["id_proveedor"], datos["nombre_proveedor"], datos["direccion"], datos["contacto"], datos["email"])
                self.cargar_datos()
                dialogo.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        # Botón para confirmar la acción en el diálogo
        btn_confirmar = tk.Button(dialogo, text="Confirmar", command=on_confirmar)
        btn_confirmar.grid(row=len(etiquetas), column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GestionProveedores(root)
    root.mainloop()
