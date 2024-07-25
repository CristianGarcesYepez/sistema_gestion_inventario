import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from producto import Producto

class GestionInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario - Ferretería Argamasa")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.iconbitmap("recursos/LOGO.ico")

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
        self.canvas.create_text(400, 50, text="INVENTARIO", font=("Arial", 30, "bold"), fill="black", anchor=tk.CENTER)

        # Contenedor de botones de acción
        self.frame_botones = tk.Frame(self.frame)
        self.frame_botones.pack(pady=60)

        # Botones de acción
        self.crear_botones()

        # Contenedor para la búsqueda de productos
        self.frame_busqueda = tk.Frame(self.frame, bg="#DCD2F0")
        self.frame_busqueda.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        # Etiqueta para el campo de búsqueda
        self.label_buscar = tk.Label(self.frame_busqueda, text="Buscar Producto", bg="#DCD2F0", font=("Arial", 12, "bold"))
        self.label_buscar.grid(row=0, column=0, padx=20, pady=5, sticky=tk.W)

        # Campo de entrada para el nombre del producto a buscar
        self.entry_buscar = tk.Entry(self.frame_busqueda, width=70)
        self.entry_buscar.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

        # Botón para ejecutar la búsqueda
        self.btn_buscar = tk.Button(self.frame_busqueda, text="Buscar", command=self.buscar_producto)
        self.btn_buscar.grid(row=0, column=2, padx=10, pady=5, sticky=tk.E)

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
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("proveedor", text="Proveedor")

        # Configuración de las columnas 
        self.tree.column("codigo", width=100, anchor='center')
        self.tree.column("nombre", width=150, anchor='center')
        self.tree.column("categoria", width=100, anchor='center')
        self.tree.column("cantidad", width=80, anchor='center')
        self.tree.column("precio", width=80, anchor='center')
        self.tree.column("proveedor", width=100, anchor='center')

        # Coloca la tabla con un espacio reducido alrededor 
        self.tree.pack(pady=(50, 10), fill=tk.BOTH, expand=False, padx=10)

        # Llamar a la función para mostrar el logo
        self.mostrar_logo()

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


    
    def crear_botones(self):
      # Botones para añadir, editar, eliminar y actualizar productos
       self.boton_agregar = tk.Button(self.canvas, text="AÑADIR PRODUCTO", command=self.agregar_producto, width=17, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
       self.canvas.create_window(150, 160, window=self.boton_agregar) 
    
       self.boton_editar = tk.Button(self.canvas, text="EDITAR PRODUCTO", command=self.editar_producto, width=17, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
       self.canvas.create_window(310, 160, window=self.boton_editar)  
    
       self.boton_eliminar = tk.Button(self.canvas, text="ELIMINAR PRODUCTO", command=self.eliminar_producto, width=17, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
       self.canvas.create_window(470, 160, window=self.boton_eliminar)  
    
       self.boton_actualizar = tk.Button(self.canvas, text="ACTUALIZAR TABLA", command=self.actualizar_tabla, width=17, height=2, font=("Arial", 10, "bold"), bg="#DCD2F0", cursor="hand2")
       self.canvas.create_window(630, 160, window=self.boton_actualizar) 

    def mostrar_logo(self):
        try:
            # Cargar la imagen del logo
            self.logo_image = Image.open("recursos/ARGAMASA_logo.png")
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)

            # Colocar el logo debajo del widget Treeview
            self.canvas.create_image(400, 525, image=self.logo_photo, anchor=tk.CENTER)
        except Exception as e:
            print(f"Error al cargar el logo: {e}")

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

