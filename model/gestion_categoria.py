import sys
import os

# Añadir la ruta del directorio 'app' al sys.path para poder importar módulos desde allí
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

import tkinter as tk  # Importar el módulo tkinter para crear la interfaz gráfica
from producto import Producto  # Importar la clase Producto desde el módulo producto
from tkinter import ttk, messagebox, simpledialog  # Importar widgets adicionales y diálogos
from categoria import Categoria  # Importar la clase Categoria desde el módulo categoria

# Clase para gestionar la ventana de categorías
class GestionCategoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Categorías - Ferretería Argamasa")  # Título de la ventana principal
        self.root.geometry("800x600")  # Tamaño de la ventana principal

        # Crear instancias de las clases Categoria y Producto para interactuar con los datos
        self.categoria = Categoria()
        self.producto = Producto()

        # Configuración del marco principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)  # Expande el marco para llenar la ventana

        # Título
        self.label_titulo = tk.Label(self.frame, text="CATEGORÍAS", font=("Arial", 24))
        self.label_titulo.pack(pady=10)  # Agrega el título al marco con margen superior e inferior

        # Botones de acciones para gestionar categorías
        self.frame_botones = tk.Frame(self.frame)
        self.frame_botones.pack(pady=10)  # Agrega el marco de botones con margen superior e inferior

        self.btn_agregar = tk.Button(self.frame_botones, text="AÑADIR CATEGORÍA", command=self.agregar_categoria)
        self.btn_agregar.grid(row=0, column=0, padx=10)  # Botón para añadir categoría

        self.btn_editar = tk.Button(self.frame_botones, text="EDITAR CATEGORÍA", command=self.editar_categoria)
        self.btn_editar.grid(row=0, column=1, padx=10)  # Botón para editar categoría

        self.btn_eliminar = tk.Button(self.frame_botones, text="ELIMINAR CATEGORÍA", command=self.eliminar_categoria)
        self.btn_eliminar.grid(row=0, column=2, padx=10)  # Botón para eliminar categoría

        # Marco para mostrar las categorías
        self.frame_categorias = tk.Frame(self.frame)
        self.frame_categorias.pack(pady=20)  # Agrega el marco de categorías con margen superior e inferior

        self.cargar_categorias()  # Cargar las categorías al iniciar la ventana

        # Tabla para mostrar los productos
        self.tree = ttk.Treeview(self.frame, columns=("codigo", "nombre", "categoria", "cantidad", "precio", "proveedor"), show='headings')
        self.tree.heading("codigo", text="Código")  # Encabezado para el código
        self.tree.heading("nombre", text="Nombre")  # Encabezado para el nombre
        self.tree.heading("categoria", text="Categoría")  # Encabezado para la categoría
        self.tree.heading("cantidad", text="Cantidad")  # Encabezado para la cantidad
        self.tree.heading("precio", text="Precio")  # Encabezado para el precio
        self.tree.heading("proveedor", text="Proveedor")  # Encabezado para el proveedor

        self.tree.pack(fill=tk.BOTH, expand=True)  # Agrega la tabla al marco principal, expandiéndola

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
