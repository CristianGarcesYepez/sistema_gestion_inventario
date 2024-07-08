import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from producto import Producto

class GestionInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario - Ferretería Argamasa")
        self.root.geometry("800x600")

        self.producto = Producto()

        # Configuración del marco principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Título
        self.label_titulo = tk.Label(self.frame, text="INVENTARIO", font=("Arial", 24))
        self.label_titulo.pack(pady=10)

        # Botones de acciones
        self.frame_botones = tk.Frame(self.frame)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="AÑADIR PRODUCTO", command=self.agregar_producto)
        self.btn_agregar.grid(row=0, column=0, padx=10)

        self.btn_editar = tk.Button(self.frame_botones, text="EDITAR PRODUCTO", command=self.editar_producto)
        self.btn_editar.grid(row=0, column=1, padx=10)

        self.btn_eliminar = tk.Button(self.frame_botones, text="ELIMINAR PRODUCTO", command=self.eliminar_producto)
        self.btn_eliminar.grid(row=0, column=2, padx=10)

        self.btn_actualizar = tk.Button(self.frame_botones, text="ACTUALIZAR TABLA", command=self.actualizar_tabla)
        self.btn_actualizar.grid(row=0, column=3, padx=10)

        # Frame para la búsqueda de productos
        self.frame_busqueda = tk.Frame(self.frame)
        self.frame_busqueda.pack(pady=10)

        self.label_buscar = tk.Label(self.frame_busqueda, text="Buscar Producto:")
        self.label_buscar.grid(row=0, column=0, padx=10)

        self.entry_buscar = tk.Entry(self.frame_busqueda, width=30)
        self.entry_buscar.grid(row=0, column=1, padx=10)

        self.btn_buscar = tk.Button(self.frame_busqueda, text="Buscar", command=self.buscar_producto)
        self.btn_buscar.grid(row=0, column=2, padx=10)

        # Tabla de productos
        self.tree = ttk.Treeview(self.frame, columns=("codigo", "nombre", "categoria", "cantidad", "precio", "proveedor"), show='headings')
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("proveedor", text="Proveedor")

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.cargar_datos()

    def cargar_datos(self):
        # Limpiar tabla actual
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Cargar productos desde la base de datos
        productos = self.producto.obtener_productos()
        for prod in productos:
            self.tree.insert("", tk.END, values=prod)

    def agregar_producto(self):
        self.dialogo_producto("Añadir Producto", self.producto.agregar_producto)

    def editar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Selecciona un producto para editar")
            return
        producto = self.tree.item(selected_item[0])['values']
        self.dialogo_producto("Editar Producto", self.producto.editar_producto, producto)

    def eliminar_producto(self):
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

        etiquetas = ["Código", "Nombre", "Categoría", "Cantidad", "Precio", "Proveedor"]
        entradas = {}

        for idx, etiqueta in enumerate(etiquetas):
            tk.Label(dialogo, text=etiqueta).grid(row=idx, column=0, pady=5)
            entrada = tk.Entry(dialogo)
            entrada.grid(row=idx, column=1, pady=5)
            if producto:
                entrada.insert(0, producto[idx])
            entradas[etiqueta.lower()] = entrada

        def on_confirmar():
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

        btn_confirmar = tk.Button(dialogo, text="Confirmar", command=on_confirmar)
        btn_confirmar.grid(row=len(etiquetas), column=0, columnspan=2, pady=10)

    def buscar_producto(self):
        nombre_producto = self.entry_buscar.get()
        if nombre_producto:
            productos_encontrados = self.producto.buscar_producto(nombre_producto)
            # Limpiar tabla actual
            for row in self.tree.get_children():
                self.tree.delete(row)
            # Mostrar productos encontrados en la tabla
            for prod in productos_encontrados:
                self.tree.insert("", tk.END, values=prod)
        else:
            messagebox.showwarning("Advertencia", "Ingresa un nombre de producto para buscar")

    def actualizar_tabla(self):
        self.cargar_datos()

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionInventario(root)
    root.mainloop()
