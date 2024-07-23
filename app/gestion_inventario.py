import tkinter as tk  # Importar el módulo tkinter para crear la interfaz gráfica
from tkinter import ttk, messagebox  # Importar widgets adicionales y diálogos
from PIL import Image, ImageTk
from producto import Producto

class GestionInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario - Ferretería Argamasa") # Título de la ventana principal
        self.root.geometry("990x780")   # Tamaño de la ventana principal
        
        
        self.producto = Producto()
        
        # Crear un canvas para colocar elementos gráficos
        self.canvas = tk.Canvas(self.root, width=990, height=780)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Cargar y establecer la imagen de fondo
        self.cargar_imagen_fondo()
        self.actualizar_imagen_fondo()
        
        # Crear el marco para los controles
        self.frame = tk.Frame(self.canvas, bg="#FFFFFF")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.9)
        
        # Título de la ventana
        self.label_titulo = tk.Label(self.frame, text="INVENTARIO", font=("Arial", 24, "bold"), bg="#FFFFFF")
        self.label_titulo.pack(pady=10)
        
        # Contenedor de botones de acción
        self.frame_botones = tk.Frame(self.frame, bg="#FFFFFF")
        self.frame_botones.pack(pady=10)
        
        # Botones de acción
        self.create_buttons()
        
        # Contenedor para la búsqueda de productos
        self.frame_busqueda = tk.Frame(self.frame, bg="#FFFFFF")
        self.frame_busqueda.pack(pady=10)
        
        # Etiqueta para el campo de búsqueda
        self.label_buscar = tk.Label(self.frame_busqueda, text="Buscar Producto:", bg="#FFFFFF")
        self.label_buscar.grid(row=0, column=0, padx=10)
        
        # Campo de entrada para el nombre del producto a buscar
        self.entry_buscar = tk.Entry(self.frame_busqueda, width=30)
        self.entry_buscar.grid(row=0, column=1, padx=10)
        
        # Botón para ejecutar la búsqueda
        self.btn_buscar = tk.Button(self.frame_busqueda, text="Buscar", command=self.buscar_producto, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_buscar.grid(row=0, column=2, padx=10)
        
        # Tabla para mostrar los productos
        self.tree = ttk.Treeview(self.frame, columns=("codigo", "nombre", "categoria", "cantidad", "precio", "proveedor"), show='headings')
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("proveedor", text="Proveedor")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Cargar los datos iniciales
        self.cargar_datos()

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
    
    def create_buttons(self):
        # Botones para añadir, editar, eliminar y actualizar productos
        self.btn_agregar = tk.Button(self.frame_botones, text="AÑADIR PRODUCTO", command=self.agregar_producto, width=20, height=2, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_agregar.grid(row=0, column=0, padx=10)
        
        self.btn_editar = tk.Button(self.frame_botones, text="EDITAR PRODUCTO", command=self.editar_producto, width=20, height=2, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_editar.grid(row=0, column=1, padx=10)
        
        self.btn_eliminar = tk.Button(self.frame_botones, text="ELIMINAR PRODUCTO", command=self.eliminar_producto, width=20, height=2, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_eliminar.grid(row=0, column=2, padx=10)
        
        self.btn_actualizar = tk.Button(self.frame_botones, text="ACTUALIZAR TABLA", command=self.actualizar_tabla, width=20, height=2, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_actualizar.grid(row=0, column=3, padx=10)

    def cargar_datos(self): # Obtiene los productos desde la base de datos y los agrega a la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)
        productos = self.producto.obtener_productos()
        for prod in productos:
            self.tree.insert("", tk.END, values=prod)

    def agregar_producto(self):  # Abre un diálogo para agregar un nuevo producto
        self.dialogo_producto("Añadir Producto", self.producto.agregar_producto)

    def editar_producto(self):   # Edita el producto seleccionado en la tabla
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Selecciona un producto para editar")
            return
        producto = self.tree.item(selected_item[0])['values']
        self.dialogo_producto("Editar Producto", self.producto.editar_producto, producto)

    def eliminar_producto(self):  # Elimina el producto seleccionado en la tabla
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar")
            return
        codigo = self.tree.item(selected_item[0])['values'][0]
        if messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar el producto con código {codigo}?"):
            self.producto.eliminar_producto(codigo)
            self.cargar_datos()

    def dialogo_producto(self, titulo, accion, producto=None):
        dialogo = tk.Toplevel(self.root)
        dialogo.title(titulo)
        # Establecer tamaño inicial de la ventana emergente
        dialogo.geometry("300x300")  # Ajusta el tamaño a tus necesidades
        dialogo.minsize(300, 300)  # Establecer tamaño mínimo

        # Etiquetas y campos de entrada para los datos del producto
        etiquetas = ["Código", "Nombre", "Categoría", "Cantidad", "Precio", "Proveedor"]
        entradas = {}

        for idx, etiqueta in enumerate(etiquetas):
            tk.Label(dialogo, text=etiqueta).grid(row=idx, column=0, pady=5)
            entrada = tk.Entry(dialogo)
            entrada.grid(row=idx, column=1, pady=5)
            if producto:
                entrada.insert(0, producto[idx])
            entradas[etiqueta.lower()] = entrada

        def on_confirmar(): # Valida y guarda los datos del producto
            try:
                datos = {campo: entradas[campo].get() for campo in entradas}
                datos["cantidad"] = int(datos["cantidad"])
                datos["precio"] = float(datos["precio"])
                if producto:
                    accion(producto[0], datos["nombre"], datos["categoría"], datos["cantidad"], datos["precio"], datos["proveedor"])
                else:
                    accion(datos["código"], datos["nombre"], datos["categoría"], datos["cantidad"], datos["precio"], datos["proveedor"])
                self.cargar_datos()
                dialogo.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

         # Botón para confirmar la acción en el diálogo
        btn_confirmar = tk.Button(dialogo, text="Confirmar", command=on_confirmar, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        btn_confirmar.grid(row=len(etiquetas), column=0, columnspan=2, pady=10)

    def buscar_producto(self):  # Busca productos en base al nombre ingresado y actualiza la tabla
        nombre_producto = self.entry_buscar.get()
        if nombre_producto:
            productos_encontrados = self.producto.buscar_producto(nombre_producto)
            for row in self.tree.get_children():
                self.tree.delete(row)
            for prod in productos_encontrados:
                self.tree.insert("", tk.END, values=prod)
        else:
            messagebox.showwarning("Advertencia", "Ingresa un nombre de producto para buscar")

    def actualizar_tabla(self): # Actualiza la tabla cargando los datos nuevamente
        self.cargar_datos()

# Ejecuta la pantalla sin necesidad del Menú
if __name__ == "__main__":
    root = tk.Tk()
    app = GestionInventario(root)
    root.mainloop()
