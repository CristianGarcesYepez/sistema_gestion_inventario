import sys
import os

# Añadir la ruta del directorio 'app' al sys.path para poder importar módulos desde allí
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

import tkinter as tk  # Importar el módulo tkinter para crear la interfaz gráfica
from producto import Producto  # Importar la clase Producto desde el módulo producto
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, simpledialog  # Importar widgets adicionales y diálogos
from categoria import Categoria  # Importar la clase Categoria desde el módulo categoria

# Clase para gestionar la ventana de categorías
class GestionCategoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Categorías - Ferretería Argamasa")  # Título de la ventana principal
        self.root.geometry("800x600")  # Tamaño de la ventana principal
        self.root.resizable(False, False)
        self.root.iconbitmap("recursos/LOGO.ico")

        # Crear instancias de las clases Categoria y Producto para interactuar con los datos
        self.categoria = Categoria()
        self.producto = Producto()

        # Crear un canvas para colocar elementos gráficos
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Crear el marco para los controles
        self.frame = tk.Frame(self.canvas, bg="")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.9)

        # Cargar y establecer la imagen de fondo
        self.cargar_imagen_fondo()


        # Título de la ventana directamente en el canvas
        self.canvas.create_text(400, 50, text="CATEGORÍAS", font=("Arial", 30, "bold"), fill="black", anchor=tk.CENTER)

        self.crear_botones()

        # Marco para mostrar las categorías
        self.frame_categorias = tk.Frame(self.frame)
        self.frame_categorias.pack(pady=20)  # Agrega el marco de categorías con margen superior e inferior

        self.cargar_categorias()  # Cargar las categorías al iniciar la ventana

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

        # Tabla para mostrar los productos
        self.tree = ttk.Treeview(self.frame, columns=("codigo", "nombre", "categoria", "cantidad", "precio", "proveedor"), show='headings')
        self.tree.heading("codigo", text="Código")  # Encabezado para el código
        self.tree.heading("nombre", text="Nombre")  # Encabezado para el nombre
        self.tree.heading("categoria", text="Categoría")  # Encabezado para la categoría
        self.tree.heading("cantidad", text="Cantidad")  # Encabezado para la cantidad
        self.tree.heading("precio", text="Precio")  # Encabezado para el precio
        self.tree.heading("proveedor", text="Proveedor")  # Encabezado para el proveedor

        # Configuración de las columnas 
        self.tree.column("codigo", width=100, anchor='center')
        self.tree.column("nombre", width=150, anchor='center')
        self.tree.column("categoria", width=100, anchor='center')
        self.tree.column("cantidad", width=80, anchor='center')
        self.tree.column("precio", width=80, anchor='center')
        self.tree.column("proveedor", width=100, anchor='center')

        self.tree.pack(pady=(100, 10), fill=tk.BOTH, expand=False, padx=10)  # Agrega la tabla al marco principal, expandiéndola
        #llamar a la función para mostrar el logo 
        self.mostrar_logo()

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
        
        self.btn_agregar = tk.Button(self.canvas, text="AÑADIR CATEGORÍA", command=self.agregar_categoria, width=17, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
        self.canvas.create_window(200, 130, window=self.btn_agregar)   # Botón para añadir categoría

        self.btn_editar = tk.Button(self.canvas, text="EDITAR CATEGORÍA", command=self.editar_categoria, width=17, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
        self.canvas.create_window(400, 130, window=self.btn_editar)   # Botón para editar categoría

        self.btn_eliminar = tk.Button(self.canvas, text="ELIMINAR CATEGORÍA", command=self.eliminar_categoria, width=17, font=("Arial", 10, "bold"), height=2, bg="#DCD2F0", cursor="hand2")
        self.canvas.create_window(600, 130, window=self.btn_eliminar)   # Botón para eliminar categoría

    def mostrar_logo(self):
        try:
            # Cargar la imagen del logo
            self.logo_image = Image.open("recursos/ARGAMASA_logo.png")
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)

            # Colocar el logo debajo del widget Treeview
            self.canvas.create_image(400, 525, image=self.logo_photo, anchor=tk.CENTER)
        except Exception as e:
            print(f"Error al cargar el logo: {e}")


    def cargar_categorias(self):
        # Obtener la lista de categorías y crear botones para cada una
        categorias = self.categoria.obtener_categorias()
        for widget in self.frame_categorias.winfo_children():
            widget.destroy()  # Eliminar widgets antiguos del marco de categorías
        for cat in categorias:
            # Crear un botón para cada categoría que, al hacer clic, muestra los productos de esa categoría
            btn_categoria = tk.Button(self.frame_categorias, text=cat[1], command=lambda c=cat[1]: self.mostrar_productos_categoria(c))
            btn_categoria.pack(side=tk.LEFT, padx=5)  # Agrega el botón al marco de categorías con margen lateral

    def mostrar_productos_categoria(self, categoria):
        # Mostrar los productos de una categoría seleccionada
        productos = self.producto.obtener_productos_por_categoria(categoria)
        for row in self.tree.get_children():
            self.tree.delete(row)  # Limpiar la tabla antes de insertar nuevos datos
        for prod in productos:
            self.tree.insert("", tk.END, values=prod)  # Insertar productos en la tabla

    def agregar_categoria(self):
        # Mostrar el diálogo para agregar una nueva categoría
        self.dialogo_categoria("Añadir Categoría", self.categoria.agregar_categoria)

    def editar_categoria(self):
        # Mostrar un diálogo para editar una categoría existente
        nombre_categoria = simpledialog.askstring("Editar Categoría", "Ingrese el nombre de la categoría a editar:")
        if nombre_categoria:
            self.dialogo_categoria("Editar Categoría", self.categoria.editar_categoria, nombre_categoria)

    def eliminar_categoria(self):
        # Mostrar un diálogo para confirmar la eliminación de una categoría
        nombre_categoria = simpledialog.askstring("Eliminar Categoría", "Ingrese el nombre de la categoría a eliminar:")
        if nombre_categoria:
            if messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar la categoría '{nombre_categoria}'?"):
                self.categoria.eliminar_categoria(nombre_categoria)
                self.cargar_categorias()  # Recargar las categorías después de eliminar

    def dialogo_categoria(self, titulo, accion, nombre_actual=None):
        # Crear un diálogo para ingresar o editar el nombre de una categoría
        dialogo = tk.Toplevel(self.root)
        dialogo.title(titulo)  # Establecer el título del diálogo

        tk.Label(dialogo, text="Nombre de la Categoría:").grid(row=0, column=0, pady=5)  # Etiqueta para el nombre
        entrada = tk.Entry(dialogo)  # Campo de entrada para el nombre de la categoría
        entrada.grid(row=0, column=1, pady=5)
        if nombre_actual:
            entrada.insert(0, nombre_actual)  # Rellenar el campo si se está editando una categoría

        def on_confirmar():
            # Acción al confirmar el diálogo
            try:
                nombre_categoria = entrada.get()
                if nombre_actual:
                    accion(nombre_actual, nombre_categoria)  # Editar una categoría existente
                else:
                    accion(nombre_categoria)  # Añadir una nueva categoría
                self.cargar_categorias()  # Recargar las categorías después de añadir o editar
                dialogo.destroy()  # Cerrar el diálogo
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")  # Mostrar mensaje de error

        btn_confirmar = tk.Button(dialogo, text="Confirmar", command=on_confirmar)  # Botón para confirmar
        btn_confirmar.grid(row=1, column=0, columnspan=2, pady=10)  # Agregar el botón al diálogo

# Código principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de la aplicación
    app = GestionCategoria(root)  # Crear una instancia de la clase GestionCategoria
    root.mainloop()  # Ejecutar el bucle principal de la aplicación
