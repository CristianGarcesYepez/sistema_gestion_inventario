import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from producto import Producto
from categoria import Categoria  # Asegúrate de tener esta clase para gestionar las categorías

class GestionCategoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Categorías - Ferretería Argamasa")
        self.root.geometry("800x600")

        self.categoria = Categoria()
        self.producto = Producto()

        # Configuración del marco principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Título
        self.label_titulo = tk.Label(self.frame, text="CATEGORÍAS", font=("Arial", 24))
        self.label_titulo.pack(pady=10)

        # Botones de acciones
        self.frame_botones = tk.Frame(self.frame)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="AÑADIR CATEGORÍA", command=self.agregar_categoria)
        self.btn_agregar.grid(row=0, column=0, padx=10)

        self.btn_editar = tk.Button(self.frame_botones, text="EDITAR CATEGORÍA", command=self.editar_categoria)
        self.btn_editar.grid(row=0, column=1, padx=10)

        self.btn_eliminar = tk.Button(self.frame_botones, text="ELIMINAR CATEGORÍA", command=self.eliminar_categoria)
        self.btn_eliminar.grid(row=0, column=2, padx=10)

        self.frame_categorias = tk.Frame(self.frame)
        self.frame_categorias.pack(pady=20)

        self.cargar_categorias()

        # Tabla de productos
        self.tree = ttk.Treeview(self.frame, columns=("codigo", "nombre", "categoria", "cantidad", "precio", "proveedor"), show='headings')
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("proveedor", text="Proveedor")

        self.tree.pack(fill=tk.BOTH, expand=True)

    def cargar_categorias(self):
        categorias = self.categoria.obtener_categorias()
        for widget in self.frame_categorias.winfo_children():
            widget.destroy()
        for cat in categorias:
            btn_categoria = tk.Button(self.frame_categorias, text=cat[1], command=lambda c=cat[0]: self.mostrar_productos_categoria(c))
            btn_categoria.pack(side=tk.LEFT, padx=5)

    def mostrar_productos_categoria(self, id_categoria):
        productos = self.producto.obtener_productos_por_categoria(id_categoria)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for prod in productos:
            self.tree.insert("", tk.END, values=prod)

    def agregar_categoria(self):
        self.dialogo_categoria("Añadir Categoría", self.categoria.agregar_categoria)

    def editar_categoria(self):
        nombre_categoria = simpledialog.askstring("Editar Categoría", "Ingrese el nombre de la categoría a editar:")
        if nombre_categoria:
            self.dialogo_categoria("Editar Categoría", self.categoria.editar_categoria, nombre_categoria)

    def eliminar_categoria(self):
        nombre_categoria = simpledialog.askstring("Eliminar Categoría", "Ingrese el nombre de la categoría a eliminar:")
        if nombre_categoria:
            if messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar la categoría '{nombre_categoria}'?"):
                self.categoria.eliminar_categoria(nombre_categoria)
                self.cargar_categorias()

    def dialogo_categoria(self, titulo, accion, nombre_actual=None):
        dialogo = tk.Toplevel(self.root)
        dialogo.title(titulo)

        tk.Label(dialogo, text="Nombre de la Categoría:").grid(row=0, column=0, pady=5)
        entrada = tk.Entry(dialogo)
        entrada.grid(row=0, column=1, pady=5)
        if nombre_actual:
            entrada.insert(0, nombre_actual)

        def on_confirmar():
            try:
                nombre_categoria = entrada.get()
                if nombre_actual:
                    accion(nombre_actual, nombre_categoria)
                else:
                    accion(nombre_categoria)
                self.cargar_categorias()
                dialogo.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        btn_confirmar = tk.Button(dialogo, text="Confirmar", command=on_confirmar)
        btn_confirmar.grid(row=1, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionCategoria(root)
    root.mainloop()
